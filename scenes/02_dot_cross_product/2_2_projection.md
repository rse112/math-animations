# 2.2 벡터 사영 (Vector Projection)

## 도입

맑은 날 오후, 막대기를 땅에 수직으로 세워 보자. 태양이 정수리 바로 위에 있다면 그림자는 점 하나에 불과하다. 태양이 지평선 쪽으로 기울수록 그림자는 길어진다. 이때 그림자의 길이는 막대기의 길이와 태양 방향이 이루는 각도에 따라 결정된다. 빛이 특정 방향에서 비출 때, 어떤 벡터가 다른 벡터 위에 드리우는 그림자의 길이와 방향을 계산하는 것이 바로 **벡터 사영(Vector Projection)**이다.

이 개념은 생각보다 훨씬 자주 쓰인다. 물리에서 경사면 위의 힘 분해, 신호 처리에서 특정 주파수 성분 추출, 머신러닝에서 차원 축소까지, 벡터 사영은 "한 방향의 성분만 골라내는" 핵심 도구다.

---

## 스칼라 사영

### 정의

벡터 $\vec{v}$를 벡터 $\vec{u}$ 방향 위에 사영했을 때의 **길이(스칼라 값)**를 스칼라 사영이라 한다. 기호로는 $\text{comp}_{\vec{u}}\vec{v}$로 나타낸다.

내적의 기하학적 정의 $\vec{v} \cdot \vec{u} = \|\vec{v}\| \|\vec{u}\| \cos\theta$를 이용하면:

$$\text{comp}_{\vec{u}}\vec{v} = \|\vec{v}\| \cos\theta = \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}$$

$\vec{u}$ 방향의 단위벡터 $\hat{u} = \dfrac{\vec{u}}{\|\vec{u}\|}$를 이용하면 더 간결하게 쓸 수 있다.

$$\text{comp}_{\vec{u}}\vec{v} = \vec{v} \cdot \hat{u}$$

스칼라 사영은 부호를 가진다. $\theta < 90°$이면 양수, $\theta > 90°$이면 음수다.

### 예시

$\vec{v} = (3, 4)$, $\vec{u} = (1, 0)$ (x축 방향 단위벡터)일 때:

$$\text{comp}_{\vec{u}}\vec{v} = \frac{(3)(1) + (4)(0)}{\sqrt{1^2 + 0^2}} = \frac{3}{1} = 3$$

x축 위의 그림자 길이가 3임을 직관적으로 확인할 수 있다.

---

## 벡터 사영

### 정의

스칼라 사영은 길이만 알려준다. 실제 공간에서 그림자에 해당하는 **벡터 자체**를 구하려면, 스칼라 사영에 $\vec{u}$ 방향의 단위벡터 $\hat{u}$를 곱하면 된다.

$$\text{proj}_{\vec{u}}\vec{v} = \left(\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}\right)\hat{u} = \left(\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}\right)\frac{\vec{u}}{\|\vec{u}\|} = \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\,\vec{u}$$

이 벡터는 $\vec{u}$와 **평행**하며, $\vec{v}$의 $\vec{u}$ 방향 성분을 나타낸다.

### 예시

$\vec{v} = (2, 3)$, $\vec{u} = (4, 0)$일 때:

$$\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2} = \frac{(2)(4) + (3)(0)}{16} = \frac{8}{16} = \frac{1}{2}$$

$$\text{proj}_{\vec{u}}\vec{v} = \frac{1}{2}(4, 0) = (2, 0)$$

---

## 수직 성분 (직교 성분)

$\vec{v}$는 항상 $\vec{u}$ 방향의 성분과 $\vec{u}$에 수직인 성분으로 **분해**할 수 있다.

$$\vec{v} = \underbrace{\text{proj}_{\vec{u}}\vec{v}}_{\vec{u}\text{ 방향 성분}} + \underbrace{(\vec{v} - \text{proj}_{\vec{u}}\vec{v})}_{\vec{u}\text{에 수직인 성분}}$$

수직 성분을 $\vec{v}_\perp$라 하면:

$$\vec{v}_\perp = \vec{v} - \text{proj}_{\vec{u}}\vec{v} = \vec{v} - \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\,\vec{u}$$

$\vec{v}_\perp$와 $\vec{u}$가 실제로 직교하는지 확인해 보자:

$$\vec{v}_\perp \cdot \vec{u} = \left(\vec{v} - \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\vec{u}\right) \cdot \vec{u} = \vec{v} \cdot \vec{u} - \frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}(\vec{u} \cdot \vec{u}) = \vec{v} \cdot \vec{u} - \vec{v} \cdot \vec{u} = 0 \checkmark$$

---

## 활용

### 물리: 일(Work)

힘 벡터 $\vec{F}$가 이동 방향 $\vec{d}$와 각도 $\theta$를 이룰 때, 실제 일에 기여하는 힘은 $\vec{d}$ 방향의 사영이다.

$$W = \vec{F} \cdot \hat{d} \cdot \|\vec{d}\| = \vec{F} \cdot \vec{d}$$

### 그림자 길이 계산

임의 방향 $\hat{n}$으로 평행광이 비출 때, 벡터 $\vec{v}$의 그림자 길이는 스칼라 사영 $|\text{comp}_{\hat{n}}\vec{v}|$이다.

### 그람-슈미트 과정

수직이 아닌 벡터들의 집합을 서로 직교하는 기저로 바꿀 때, 각 단계마다 벡터 사영을 빼는 과정을 반복한다. 이것이 **그람-슈미트 정규직교화**의 핵심 아이디어다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 스칼라 사영 | $\text{comp}_{\vec{u}}\vec{v} = \dfrac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|}$ |
| 벡터 사영 | $\text{proj}_{\vec{u}}\vec{v} = \dfrac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\,\vec{u}$ |
| 수직 성분 | $\vec{v}_\perp = \vec{v} - \text{proj}_{\vec{u}}\vec{v}$ |
| 벡터 분해 | $\vec{v} = \text{proj}_{\vec{u}}\vec{v} + \vec{v}_\perp$ |
| 단위벡터로 표현 | $\text{comp}_{\vec{u}}\vec{v} = \vec{v} \cdot \hat{u}$, $\text{proj}_{\vec{u}}\vec{v} = (\vec{v} \cdot \hat{u})\hat{u}$ |
| 직교 검증 | $\vec{v}_\perp \cdot \vec{u} = 0$ |

> 다음 글에서는 **외적(Cross Product)**을 알아본다. 두 벡터로부터 새로운 벡터를 만드는, 3차원에서만 정의되는 연산을 다룬다.
