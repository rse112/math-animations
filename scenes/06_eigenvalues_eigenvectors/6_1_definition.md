# 6.1 고유값과 고유벡터란?

## 도입

거울 앞에 서서 팔을 들어 올리면, 거울 속 나도 팔을 들어 올린다. 하지만 거울은 좌우를 바꾼다. 이처럼 대부분의 변환은 벡터의 방향을 바꿔버린다. 그런데 특별한 벡터들이 있다. 변환을 가해도 방향이 전혀 달라지지 않고, 오직 크기만 변하는 벡터들이다. 이 특별한 벡터가 바로 **고유벡터(eigenvector)**이고, 크기가 얼마나 변했는지를 나타내는 값이 **고유값(eigenvalue)**이다.

이 개념은 단순한 수학적 호기심을 넘어 매우 실용적이다. 구조물이 진동할 때의 공명 주파수, 구글의 페이지랭크 알고리즘, 얼굴 인식 기술, 양자역학에서 에너지 상태 계산까지 --- 고유값과 고유벡터는 현대 과학기술의 근간을 이루는 핵심 도구다. 이번 글에서는 그 정의와 기하학적 의미를 직관적으로 이해해 보자.

---

## 고유값과 고유벡터의 정의

### 핵심 정의

정방행렬 $A$에 대해, 다음 조건을 만족하는 영이 아닌 벡터 $\vec{v}$와 스칼라 $\lambda$가 존재할 때:

$$A\vec{v} = \lambda\vec{v}, \quad \vec{v} \neq \vec{0}$$

이때 $\lambda$를 행렬 $A$의 **고유값(eigenvalue)**, $\vec{v}$를 $\lambda$에 대응하는 **고유벡터(eigenvector)**라고 한다.

이 식을 풀어보면, $A$라는 선형변환을 $\vec{v}$에 적용했을 때 결과가 $\vec{v}$의 상수배($\lambda$배)라는 뜻이다. 방향은 그대로(또는 정반대), 크기만 $|\lambda|$배 변한다.

### 왜 $\vec{v} \neq \vec{0}$ 조건이 필요한가?

영벡터 $\vec{0}$는 항상 $A\vec{0} = \lambda\vec{0} = \vec{0}$를 만족하므로, 모든 $\lambda$에 대해 trivial하게 성립한다. 이는 아무런 정보를 주지 않으므로 배제한다.

---

## 기하학적 의미

### 변환 후 같은 직선 위에 있는 벡터

고유벡터의 기하학적 의미는 매우 직관적이다. 벡터 $\vec{v}$를 행렬 $A$로 변환했을 때, 결과 벡터 $A\vec{v}$가 원래 $\vec{v}$와 **같은 직선 위**에 놓인다는 것이다.

- $\lambda > 0$이면: 같은 방향으로 $\lambda$배 늘어남(또는 줄어듦)
- $\lambda < 0$이면: 반대 방향으로 $|\lambda|$배 변함
- $\lambda = 1$이면: 변환 후에도 벡터가 전혀 변하지 않음(고정점)
- $\lambda = 0$이면: 변환 후 영벡터가 됨(해당 방향이 "압축"됨)

$$\vec{v} \xrightarrow{A} \lambda\vec{v}$$

### 고유공간(Eigenspace)

하나의 고유값 $\lambda$에 대해 모든 고유벡터의 집합(영벡터 포함)은 부분공간을 이루며, 이를 **고유공간(eigenspace)**이라 한다:

$$E_\lambda = \ker(A - \lambda I) = \{\vec{v} : A\vec{v} = \lambda\vec{v}\}$$

---

## 예시: 대각행렬의 고유값

### 대각행렬은 고유값과 고유벡터를 바로 읽을 수 있다

대각행렬 $D = \begin{pmatrix} 3 & 0 \\ 0 & 5 \end{pmatrix}$를 생각해 보자.

표준기저벡터 $\vec{e}_1 = \begin{pmatrix}1\\0\end{pmatrix}$, $\vec{e}_2 = \begin{pmatrix}0\\1\end{pmatrix}$에 대해:

$$D\vec{e}_1 = \begin{pmatrix} 3 & 0 \\ 0 & 5 \end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}3\\0\end{pmatrix} = 3\vec{e}_1$$

$$D\vec{e}_2 = \begin{pmatrix} 3 & 0 \\ 0 & 5 \end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\5\end{pmatrix} = 5\vec{e}_2$$

따라서 대각행렬의 고유값은 **대각 성분**이고, 고유벡터는 **표준기저벡터**다.

일반적으로 $n \times n$ 대각행렬 $D = \text{diag}(d_1, d_2, \ldots, d_n)$의 고유값은 $\lambda_i = d_i$이다.

### 3×3 대각행렬 예시

$$D = \begin{pmatrix} -2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \end{pmatrix}$$

고유값: $\lambda_1 = -2$, $\lambda_2 = 1$, $\lambda_3 = 4$

대응 고유벡터:
- $\lambda_1 = -2$: $\vec{v}_1 = \begin{pmatrix}1\\0\\0\end{pmatrix}$ (x축 방향은 반대로 2배)
- $\lambda_2 = 1$: $\vec{v}_2 = \begin{pmatrix}0\\1\\0\end{pmatrix}$ (y축 방향은 변하지 않음)
- $\lambda_3 = 4$: $\vec{v}_3 = \begin{pmatrix}0\\0\\1\end{pmatrix}$ (z축 방향은 4배 늘어남)

---

## 고유벡터의 스칼라 배

고유벡터는 스칼라 배를 해도 여전히 고유벡터다. $\vec{v}$가 $\lambda$에 대한 고유벡터라면, $c\vec{v}$ ($c \neq 0$)도 같은 $\lambda$에 대한 고유벡터다:

$$A(c\vec{v}) = c(A\vec{v}) = c(\lambda\vec{v}) = \lambda(c\vec{v})$$

그러므로 고유벡터를 구할 때는 보통 특정 방향을 대표하는 단위벡터 또는 간단한 정수 성분의 벡터로 표현한다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 고유벡터 정의 | $A\vec{v} = \lambda\vec{v}$, $\vec{v} \neq \vec{0}$ |
| 고유값 $\lambda$ | 변환 후 크기 변화 비율 |
| 고유벡터 $\vec{v}$ | 변환 후 방향이 유지되는 벡터 |
| 기하학적 의미 | 변환 후 같은 직선 위에 놓임 |
| $\lambda > 1$ | 해당 방향으로 늘어남 |
| $0 < \lambda < 1$ | 해당 방향으로 줄어듦 |
| $\lambda < 0$ | 방향 반전 후 크기 변화 |
| $\lambda = 0$ | 해당 방향이 영벡터로 압축 |
| 대각행렬의 고유값 | 대각 성분 그 자체 |
| 고유공간 | $E_\lambda = \ker(A - \lambda I)$ |

> 다음 글에서는 **특성방정식**을 이용해 임의의 행렬에서 고유값을 실제로 구하는 방법을 알아본다.
