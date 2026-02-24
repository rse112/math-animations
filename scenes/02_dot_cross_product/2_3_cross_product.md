# 2.3 외적 (Cross Product)

## 도입

나사를 조일 때를 생각해 보자. 드라이버를 손으로 잡고 힘을 가해 회전시키면 나사가 조여진다. 이때 손이 가하는 힘의 방향과 드라이버 축의 방향, 그리고 그 결과로 나타나는 회전 효과의 방향은 서로 수직 관계에 있다. 오른손을 펴서 네 손가락이 첫 번째 벡터에서 두 번째 벡터 쪽으로 감기도록 하면, 엄지손가락이 가리키는 방향이 바로 외적의 방향이다. 이것이 **오른손 법칙(Right-Hand Rule)**이다.

내적이 두 벡터로부터 스칼라를 만들어냈다면, **외적(Cross Product)**은 두 벡터로부터 새로운 **벡터**를 만들어낸다. 그 벡터는 입력한 두 벡터 모두에 수직이다. 이 특성 덕분에 외적은 물리의 토크, 컴퓨터 그래픽스의 법선벡터 계산 등 3차원 공간 전반에서 필수 도구로 쓰인다.

---

## 외적의 정의

### 행렬식을 이용한 정의

3차원 벡터 $\vec{u} = (u_1, u_2, u_3)$와 $\vec{v} = (v_1, v_2, v_3)$의 외적은 다음 행렬식으로 정의한다.

$$\vec{u} \times \vec{v} = \det\begin{pmatrix} \hat{i} & \hat{j} & \hat{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix}$$

이것을 첫 번째 행에 대해 전개하면:

$$\vec{u} \times \vec{v} = \hat{i}(u_2 v_3 - u_3 v_2) - \hat{j}(u_1 v_3 - u_3 v_1) + \hat{k}(u_1 v_2 - u_2 v_1)$$

성분으로 정리하면:

$$\vec{u} \times \vec{v} = (u_2 v_3 - u_3 v_2,\ u_3 v_1 - u_1 v_3,\ u_1 v_2 - u_2 v_1)$$

### 예시

$\vec{u} = (1, 2, 3)$, $\vec{v} = (4, 5, 6)$일 때:

$$\vec{u} \times \vec{v} = (2 \cdot 6 - 3 \cdot 5,\ 3 \cdot 4 - 1 \cdot 6,\ 1 \cdot 5 - 2 \cdot 4) = (12-15,\ 12-6,\ 5-8) = (-3, 6, -3)$$

결과 벡터가 $\vec{u}$와 $\vec{v}$ 모두에 수직인지 내적으로 확인:

$$(-3,6,-3) \cdot (1,2,3) = -3 + 12 - 9 = 0 \checkmark$$
$$(-3,6,-3) \cdot (4,5,6) = -12 + 30 - 18 = 0 \checkmark$$

---

## 외적의 크기

### 기하학적 의미 — 평행사변형의 넓이

$$\|\vec{u} \times \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta$$

여기서 $\theta$는 두 벡터 사이의 각도 ($0 \leq \theta \leq \pi$)다. 이 값은 $\vec{u}$와 $\vec{v}$가 이루는 **평행사변형의 넓이**와 같다.

$$\text{평행사변형의 넓이} = \|\vec{u} \times \vec{v}\|$$

삼각형의 넓이는 그 절반이다.

$$\text{삼각형의 넓이} = \frac{1}{2}\|\vec{u} \times \vec{v}\|$$

두 벡터가 평행하면 $\sin\theta = 0$이 되어 외적이 영벡터가 된다. 반대로 두 벡터가 직교하면 $\sin 90° = 1$로 외적의 크기가 최대가 된다.

---

## 외적의 성질

### 반교환법칙 (Anti-commutativity)

$$\vec{v} \times \vec{u} = -(\vec{u} \times \vec{v})$$

순서를 바꾸면 방향이 반대인 벡터가 나온다. 이것이 외적이 교환법칙을 따르지 않는 이유다.

### 자기 자신과의 외적

$$\vec{u} \times \vec{u} = \vec{0}$$

$\sin 0° = 0$이므로 자기 자신과의 외적은 항상 영벡터다.

### 분배법칙

$$\vec{u} \times (\vec{v} + \vec{w}) = \vec{u} \times \vec{v} + \vec{u} \times \vec{w}$$

### 스칼라 결합

$$(c\vec{u}) \times \vec{v} = c(\vec{u} \times \vec{v}) = \vec{u} \times (c\vec{v})$$

### 표준 기저 벡터들의 외적

$$\hat{i} \times \hat{j} = \hat{k}, \quad \hat{j} \times \hat{k} = \hat{i}, \quad \hat{k} \times \hat{i} = \hat{j}$$

순환 순서를 거스르면 부호가 바뀐다: $\hat{j} \times \hat{i} = -\hat{k}$

---

## 활용

### 법선벡터 계산

3D 공간에서 평면을 정의하는 두 벡터 $\vec{u}$, $\vec{v}$가 있을 때, 그 평면에 수직인 **법선벡터(Normal Vector)**는:

$$\vec{n} = \vec{u} \times \vec{v}$$

컴퓨터 그래픽스에서 조명 계산, 충돌 감지 등에 필수적으로 사용된다.

### 토크 (Torque)

물리에서 토크(회전력) $\vec{\tau}$는 위치벡터 $\vec{r}$과 힘 $\vec{F}$의 외적이다.

$$\vec{\tau} = \vec{r} \times \vec{F}$$

토크의 크기는 $\|\vec{r}\|\|\vec{F}\|\sin\theta$이며, 방향은 오른손 법칙을 따른다.

### 부피 계산 (스칼라 삼중적)

세 벡터 $\vec{u}$, $\vec{v}$, $\vec{w}$가 만드는 평행육면체의 부피는 스칼라 삼중적으로 계산한다.

$$V = |\vec{u} \cdot (\vec{v} \times \vec{w})|$$

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 외적 정의 | $\vec{u} \times \vec{v} = \det\begin{pmatrix}\hat{i}&\hat{j}&\hat{k}\\u_1&u_2&u_3\\v_1&v_2&v_3\end{pmatrix}$ |
| 크기 | $\|\vec{u} \times \vec{v}\| = \|\vec{u}\|\|\vec{v}\|\sin\theta$ |
| 방향 | 두 입력 벡터 모두에 수직 (오른손 법칙) |
| 반교환법칙 | $\vec{v} \times \vec{u} = -\vec{u} \times \vec{v}$ |
| 평행사변형 넓이 | $\|\vec{u} \times \vec{v}\|$ |
| 삼각형 넓이 | $\frac{1}{2}\|\vec{u} \times \vec{v}\|$ |
| 주요 활용 | 법선벡터, 토크, 넓이/부피 계산 |

> 다음 글에서는 **행렬(Matrix)**을 알아본다. 여러 벡터와 방정식을 하나의 표 형태로 묶어 다루는 강력한 도구를 소개한다.
