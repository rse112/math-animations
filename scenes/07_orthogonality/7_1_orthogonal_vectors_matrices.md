# 7.1 직교 벡터와 직교 행렬

## 도입

지도에서 북쪽과 동쪽은 서로 완전히 독립적이다. 북쪽으로 이동해도 동쪽 좌표는 전혀 바뀌지 않는다. 이 직교 좌표계 덕분에 지도 읽기, GPS 계산, 건물 설계가 단순해진다. 이처럼 서로 수직인 벡터들로 이루어진 좌표계는 계산을 엄청나게 단순화시킨다.

선형대수에서 이 아이디어가 **직교 벡터(orthogonal vectors)**와 **직교 행렬(orthogonal matrix)**로 정형화된다. 직교 행렬은 단순한 수학적 도구가 아니라 컴퓨터 그래픽의 회전 변환, 신호 처리의 푸리에 변환, 양자역학의 유니터리 변환 등 수많은 응용의 기반이다. 직교성은 수치 안정성(numerical stability)을 보장하는 핵심 성질이기도 하다.

---

## 직교 벡터

### 정의: 내적이 0

두 벡터 $\vec{u}$, $\vec{v}$가 **직교(orthogonal)**하다는 것은 내적이 0임을 의미한다:

$$\vec{u} \cdot \vec{v} = \vec{u}^T\vec{v} = \sum_{i=1}^{n} u_i v_i = 0$$

이는 두 벡터가 기하학적으로 90도 각도를 이룬다는 것과 동치다(단, 둘 다 비영벡터인 경우).

### 예시

$$\vec{u} = \begin{pmatrix}1\\2\\3\end{pmatrix}, \quad \vec{v} = \begin{pmatrix}1\\1\\-1\end{pmatrix}$$

$$\vec{u} \cdot \vec{v} = (1)(1) + (2)(1) + (3)(-1) = 1 + 2 - 3 = 0 \checkmark$$

따라서 $\vec{u}$와 $\vec{v}$는 직교한다.

### 피타고라스 정리의 일반화

직교 벡터에 대해 피타고라스 정리가 성립한다:

$$\|\vec{u} + \vec{v}\|^2 = \|\vec{u}\|^2 + \|\vec{v}\|^2 \quad (\vec{u} \perp \vec{v}일 때)$$

**증명:**

$$\|\vec{u} + \vec{v}\|^2 = (\vec{u}+\vec{v})\cdot(\vec{u}+\vec{v}) = \|\vec{u}\|^2 + 2\underbrace{\vec{u}\cdot\vec{v}}_{=0} + \|\vec{v}\|^2 = \|\vec{u}\|^2 + \|\vec{v}\|^2$$

---

## 정규직교 집합 (Orthonormal Set)

### 직교 + 단위벡터

벡터들의 집합 $\{\vec{u}_1, \vec{u}_2, \ldots, \vec{u}_k\}$가 **정규직교(orthonormal)**하다는 것은:

1. **직교 조건**: $i \neq j$이면 $\vec{u}_i \cdot \vec{u}_j = 0$
2. **정규화 조건**: 모든 $i$에 대해 $\|\vec{u}_i\| = 1$

이를 한 번에 표현하면:

$$\vec{u}_i \cdot \vec{u}_j = \delta_{ij} = \begin{cases} 1 & (i = j) \\ 0 & (i \neq j) \end{cases}$$

여기서 $\delta_{ij}$는 **크로네커 델타(Kronecker delta)**다.

### 직교 집합의 선형독립성

직교 집합(영벡터를 포함하지 않는)은 항상 **선형독립**이다. 이 성질 덕분에 정규직교기저는 좌표 표현을 매우 단순하게 만든다.

**증명 스케치:** $c_1\vec{u}_1 + c_2\vec{u}_2 + \cdots + c_k\vec{u}_k = \vec{0}$이라 하면, 양변과 $\vec{u}_i$의 내적을 취하면 $c_i = 0$임을 바로 알 수 있다.

---

## 직교 행렬 (Orthogonal Matrix)

### 정의

정방행렬 $Q$가 **직교 행렬(orthogonal matrix)**이라는 것은:

$$Q^T Q = Q Q^T = I$$

즉, $Q$의 역행렬이 전치행렬과 같다:

$$Q^{-1} = Q^T$$

직교 행렬의 열벡터들은 정규직교 집합을 이루고, 행벡터들도 마찬가지로 정규직교 집합을 이룬다.

### 직교 행렬의 핵심 성질

**길이 보존 (Length-preserving):**

$$\|Q\vec{x}\| = \|\vec{x}\| \quad \text{모든 } \vec{x} \text{에 대해}$$

**증명:**

$$\|Q\vec{x}\|^2 = (Q\vec{x})^T(Q\vec{x}) = \vec{x}^T Q^T Q \vec{x} = \vec{x}^T I \vec{x} = \|\vec{x}\|^2$$

**각도 보존 (Angle-preserving):**

$$\cos\theta = \frac{(Q\vec{x}) \cdot (Q\vec{y})}{\|Q\vec{x}\|\|Q\vec{y}\|} = \frac{\vec{x}^TQ^TQ\vec{y}}{\|\vec{x}\|\|\vec{y}\|} = \frac{\vec{x}\cdot\vec{y}}{\|\vec{x}\|\|\vec{y}\|}$$

즉, 직교 행렬은 **등거리 변환(isometry)**이다. 도형의 모양과 크기를 보존한다.

**행렬식:**

$$\det(Q) = \pm 1$$

$\det(Q) = 1$이면 회전(rotation), $\det(Q) = -1$이면 반사(reflection)를 포함한다.

---

## 예시: 2차원 회전 행렬

각도 $\theta$만큼의 회전을 나타내는 행렬:

$$Q = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

직교 행렬 검증:

$$Q^T Q = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

$$= \begin{pmatrix} \cos^2\theta + \sin^2\theta & 0 \\ 0 & \sin^2\theta + \cos^2\theta \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \checkmark$$

$\det(Q) = \cos^2\theta + \sin^2\theta = 1$ (순수 회전이므로).

---

## 직교 행렬의 열벡터 조건

$Q = [\vec{q}_1 \; \vec{q}_2 \; \cdots \; \vec{q}_n]$이라 하면, $Q^TQ = I$는 다음과 동치:

$$\vec{q}_i^T \vec{q}_j = \delta_{ij}$$

즉, 열벡터들이 정규직교 집합을 이룬다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 직교 벡터 | $\vec{u} \cdot \vec{v} = 0$ |
| 정규직교 | 직교 + 단위벡터: $\vec{u}_i \cdot \vec{u}_j = \delta_{ij}$ |
| 직교 행렬 정의 | $Q^T Q = Q Q^T = I$ |
| 역행렬 간단화 | $Q^{-1} = Q^T$ |
| 길이 보존 | $\|Q\vec{x}\| = \|\vec{x}\|$ |
| 각도 보존 | 내적 보존 |
| 행렬식 | $\det(Q) = \pm 1$ |
| 회전 행렬 | $\det(Q) = 1$인 직교 행렬 |
| 열벡터 조건 | 열들이 정규직교 집합 |

> 다음 글에서는 **그람-슈미트 과정(Gram-Schmidt process)**을 통해 임의의 선형독립 벡터 집합에서 정규직교기저를 체계적으로 만드는 방법을 알아본다.
