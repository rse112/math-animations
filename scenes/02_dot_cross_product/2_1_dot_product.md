# 2.1 내적 (Dot Product)

## 도입

물체를 밀어서 이동시킬 때, 힘의 방향과 이동 방향이 완전히 같다면 힘이 100% 일로 전환된다. 반대로 힘을 옆 방향으로 가했는데 물체가 앞으로만 움직인다면, 그 힘은 이동에 전혀 기여하지 못한다. 물리학에서 **일(Work)**은 바로 이 관계를 수식으로 표현한 것이다.

$$W = \|\vec{F}\|\|\vec{d}\|\cos\theta$$

여기서 $\theta$는 힘 벡터 $\vec{F}$와 변위 벡터 $\vec{d}$ 사이의 각도다. 두 벡터가 이루는 각도가 작을수록(방향이 비슷할수록) 일의 양이 커진다. 이 수식의 핵심 연산이 바로 **내적(Dot Product)**이다. 내적은 두 벡터가 얼마나 "같은 방향을 향하는지"를 하나의 스칼라 값으로 측정해 준다.

---

## 내적의 정의

### 대수적 정의

$n$차원 벡터 $\vec{u} = (u_1, u_2, \ldots, u_n)$와 $\vec{v} = (v_1, v_2, \ldots, v_n)$의 내적은 대응하는 성분끼리 곱한 뒤 모두 더한 값이다.

$$\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n = \sum_{k=1}^{n} u_k v_k$$

**예시** — 2차원 벡터 $\vec{u} = (3, 4)$, $\vec{v} = (1, 2)$:

$$\vec{u} \cdot \vec{v} = 3 \times 1 + 4 \times 2 = 3 + 8 = 11$$

계산 결과는 스칼라(숫자)이다. 벡터를 입력받아 숫자를 반환하는 연산이라는 점을 기억하자.

### 기하학적 정의

두 벡터 사이의 각도 $\theta$ ($0 \leq \theta \leq \pi$)를 이용하면 내적을 기하학적으로 표현할 수 있다.

$$\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$$

여기서 $\|\vec{u}\|$는 벡터 $\vec{u}$의 크기(길이)다. 두 정의는 완전히 동등하며, 코사인 법칙을 이용하면 하나로부터 다른 하나를 유도할 수 있다.

---

## 내적의 성질

### 교환법칙 (Commutativity)

$$\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$$

성분별 곱셈의 순서를 바꿔도 합은 변하지 않으므로, 내적은 교환법칙이 성립한다.

### 분배법칙 (Distributivity)

$$\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$$

덧셈에 대한 분배가 성립하므로, 내적을 전개하거나 묶는 대수적 조작이 자유롭다.

### 자기 자신과의 내적 — 크기의 제곱

$$\vec{v} \cdot \vec{v} = v_1^2 + v_2^2 + \cdots + v_n^2 = \|\vec{v}\|^2$$

따라서 벡터의 크기는 다음과 같이 내적으로 표현된다.

$$\|\vec{v}\| = \sqrt{\vec{v} \cdot \vec{v}}$$

### 스칼라 결합

스칼라 $c$에 대해 다음이 성립한다.

$$(c\vec{u}) \cdot \vec{v} = c(\vec{u} \cdot \vec{v}) = \vec{u} \cdot (c\vec{v})$$

---

## 직교 조건

두 벡터가 **직교(orthogonal)**한다는 것은 $\theta = 90°$를 의미한다. $\cos 90° = 0$이므로:

$$\vec{u} \cdot \vec{v} = 0 \quad \Leftrightarrow \quad \vec{u} \perp \vec{v}$$

이 조건은 선형대수 전반에서 매우 자주 등장한다. 예를 들어 표준 기저 벡터들은 서로 직교한다.

$$\hat{i} \cdot \hat{j} = (1,0,0) \cdot (0,1,0) = 0$$

영벡터 $\vec{0}$은 관례상 모든 벡터에 직교한다고 정의한다.

---

## 각도 계산

기하학적 정의를 $\cos\theta$에 대해 풀면, 두 벡터 사이의 각도를 계산할 수 있다.

$$\cos\theta = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$

$$\theta = \arccos\!\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\right)$$

**예시** — $\vec{u} = (1, 0)$, $\vec{v} = (1, 1)$:

$$\cos\theta = \frac{1 \cdot 1 + 0 \cdot 1}{\sqrt{1} \cdot \sqrt{2}} = \frac{1}{\sqrt{2}} \implies \theta = 45°$$

내적의 부호만으로도 방향 관계를 빠르게 파악할 수 있다.

| 내적 값 | 각도 범위 | 의미 |
|---------|-----------|------|
| $> 0$ | $0° \leq \theta < 90°$ | 같은 방향 성분 존재 |
| $= 0$ | $\theta = 90°$ | 직교 |
| $< 0$ | $90° < \theta \leq 180°$ | 반대 방향 성분 존재 |

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 대수적 정의 | $\vec{u} \cdot \vec{v} = \sum_{k=1}^{n} u_k v_k$ |
| 기하학적 정의 | $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$ |
| 교환법칙 | $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$ |
| 크기와의 관계 | $\vec{v} \cdot \vec{v} = \|\vec{v}\|^2$ |
| 직교 조건 | $\vec{u} \cdot \vec{v} = 0 \Leftrightarrow \vec{u} \perp \vec{v}$ |
| 각도 공식 | $\cos\theta = \dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$ |
| 물리적 의미 | 두 벡터가 얼마나 같은 방향인지를 나타내는 스칼라 |

> 다음 글에서는 **벡터 사영(Vector Projection)**을 알아본다. 내적을 활용해 한 벡터를 다른 벡터 위에 "투영"하는 방법을 다룬다.
