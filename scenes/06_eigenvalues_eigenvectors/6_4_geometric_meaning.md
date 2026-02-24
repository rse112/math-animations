# 6.4 고유값의 기하학적 의미

## 도입

지금까지 고유값과 고유벡터를 대수적으로 계산하는 방법을 배웠다. 이번 글에서는 한 발짝 물러서서 "이것이 기하학적으로 무엇을 의미하는가?"를 깊이 생각해 보자. 사실 고유값과 고유벡터는 선형변환의 **주요 축(principal axes)**을 찾는 것이다. 마치 타원의 장축과 단축을 찾듯이, 선형변환이 가장 강하게 작용하는 방향과 얼마나 늘리거나 줄이는지를 정확히 파악할 수 있다.

이 기하학적 관점은 단순히 시각적 이해를 위한 것이 아니다. 데이터 분석에서 가장 중요한 방향을 찾는 PCA(주성분 분석), 진동 시스템에서 공명 모드를 찾는 것, 그래프 이론에서 구조를 파악하는 것 모두 고유값의 기하학적 의미에 기반한다.

---

## 기하학적 해석: 늘림, 줄임, 반전

### 고유값의 크기와 방향

고유벡터 $\vec{v}$는 변환 $A$ 아래에서 방향이 유지되는 특별한 방향이다. 고유값 $\lambda$는 그 방향에서 어떤 일이 일어나는지를 알려준다:

| 고유값 범위 | 기하학적 효과 |
|-------------|---------------|
| $\lambda > 1$ | 해당 방향으로 늘어남 |
| $\lambda = 1$ | 해당 방향 변화 없음 |
| $0 < \lambda < 1$ | 해당 방향으로 줄어듦 |
| $\lambda = 0$ | 해당 방향이 영벡터로 붕괴 |
| $\lambda < 0$ | 방향 반전 후 $|\lambda|$배 변화 |

### 직관적 그림

2차원 공간에서 두 개의 고유벡터 $\vec{v}_1$, $\vec{v}_2$ (서로 다른 방향)가 있다고 하자. 행렬 $A$를 적용하면:

- $\vec{v}_1$ 방향으로 $\lambda_1$배
- $\vec{v}_2$ 방향으로 $\lambda_2$배

단위원(unit circle)을 $A$로 변환하면 **타원(ellipse)**이 된다. 타원의 반축 길이는 $|\lambda_1|$과 $|\lambda_2|$이고, 반축 방향이 바로 고유벡터 방향이다.

---

## 대칭행렬의 특별한 성질

### 실수 고유값과 직교 고유벡터

대칭행렬 $A = A^T$는 다음 두 가지 특별한 성질을 갖는다:

1. **모든 고유값이 실수다**: 복소수 고유값이 나타나지 않는다.
2. **서로 다른 고유값에 대응하는 고유벡터들은 서로 직교한다**.

즉, $\lambda_i \neq \lambda_j$이면 $\vec{v}_i \cdot \vec{v}_j = 0$이다.

이를 증명해 보자. $A\vec{v}_i = \lambda_i \vec{v}_i$, $A\vec{v}_j = \lambda_j \vec{v}_j$라 하면:

$$\lambda_i (\vec{v}_i \cdot \vec{v}_j) = (A\vec{v}_i)^T \vec{v}_j = \vec{v}_i^T A^T \vec{v}_j = \vec{v}_i^T A \vec{v}_j = \lambda_j (\vec{v}_i \cdot \vec{v}_j)$$

$$(\lambda_i - \lambda_j)(\vec{v}_i \cdot \vec{v}_j) = 0$$

$\lambda_i \neq \lambda_j$이므로 $\vec{v}_i \cdot \vec{v}_j = 0$. 직교가 증명된다.

### 스펙트럴 정리 (Spectral Theorem)

실수 대칭행렬 $A$는 반드시 대각화 가능하며, 직교 고유벡터들로 이루어진 직교행렬 $Q$에 의해:

$$A = QDQ^T = QDQ^{-1}$$

여기서 $Q^T = Q^{-1}$이다 (직교행렬이므로).

---

## 스펙트럴 분해 (Spectral Decomposition)

### 행렬을 고유벡터와 고유값으로 분해

대칭행렬 $A$를 정규화된 고유벡터 $\vec{u}_1, \vec{u}_2, \ldots, \vec{u}_n$과 대응 고유값 $\lambda_1, \lambda_2, \ldots, \lambda_n$으로 표현하면:

$$A = \sum_{i=1}^{n} \lambda_i \vec{u}_i \vec{u}_i^T$$

각 항 $\lambda_i \vec{u}_i \vec{u}_i^T$는 $\vec{u}_i$ 방향으로의 정사영(projection)에 $\lambda_i$를 곱한 **랭크-1 행렬**이다.

이 표현은 $A$를 "원시적인 변환들의 합"으로 분해한 것이다. 각 항은 하나의 방향으로만 작용하는 단순한 변환이고, $A$는 이들을 모두 더한 것이다.

### 스펙트럴 분해 예시

$$A = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$$

특성방정식: $\lambda^2 - 6\lambda + 8 = 0 \Rightarrow \lambda_1 = 4, \lambda_2 = 2$

정규화된 고유벡터:

$$\vec{u}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}, \quad \vec{u}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$$

스펙트럴 분해:

$$A = 4 \cdot \frac{1}{2}\begin{pmatrix}1\\1\end{pmatrix}\begin{pmatrix}1&1\end{pmatrix} + 2 \cdot \frac{1}{2}\begin{pmatrix}1\\-1\end{pmatrix}\begin{pmatrix}1&-1\end{pmatrix}$$

$$= 2\begin{pmatrix}1&1\\1&1\end{pmatrix} + 1\begin{pmatrix}1&-1\\-1&1\end{pmatrix} = \begin{pmatrix}3&1\\1&3\end{pmatrix} \checkmark$$

---

## 고유값으로 알 수 있는 정보들

### 행렬의 성질과 고유값

| 행렬 성질 | 고유값 조건 |
|-----------|------------|
| 가역 행렬 | 모든 고유값 $\neq 0$ |
| 양정치(positive definite) | 모든 고유값 $> 0$ |
| 반양정치(positive semidefinite) | 모든 고유값 $\geq 0$ |
| 직교 행렬 | 모든 고유값의 절댓값 $= 1$ |
| 대각합(trace) | $\text{tr}(A) = \sum \lambda_i$ |
| 행렬식(determinant) | $\det(A) = \prod \lambda_i$ |

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 기하학적 의미 | 고유벡터 방향 = 변환의 주요 축 |
| $\|\lambda\| > 1$ | 해당 방향으로 늘어남 |
| $\|\lambda\| < 1$ | 해당 방향으로 줄어듦 |
| $\lambda < 0$ | 방향 반전 발생 |
| 대칭행렬 성질 | 실수 고유값 + 직교 고유벡터 |
| 스펙트럴 정리 | $A = QDQ^T$ (대칭행렬) |
| 스펙트럴 분해 | $A = \sum \lambda_i \vec{u}_i\vec{u}_i^T$ |
| $\text{tr}(A)$ | 고유값의 합 |
| $\det(A)$ | 고유값의 곱 |

> 다음 글에서는 **직교 벡터와 직교 행렬**의 정의와 성질을 살펴보며, 직교성이 왜 수치 계산에서 중요한지 알아본다.
