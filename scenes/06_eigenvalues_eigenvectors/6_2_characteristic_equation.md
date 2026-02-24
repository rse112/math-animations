# 6.2 특성방정식

## 도입

이전 글에서 고유값과 고유벡터의 개념을 배웠다. $A\vec{v} = \lambda\vec{v}$를 만족하는 $\lambda$와 $\vec{v}$가 존재한다는 것은 알겠는데, 막상 실제 행렬이 주어졌을 때 이것을 어떻게 구할까? 주먹구구식으로 "혹시 이 벡터가 고유벡터일까?" 하며 하나씩 대입해 볼 수는 없다.

다행히도 선형대수학은 고유값을 체계적으로 구하는 방법을 제공한다. 핵심 아이디어는 $A\vec{v} = \lambda\vec{v}$를 변형하면 **행렬식(determinant)**이 등장한다는 것이다. 이 행렬식을 0으로 놓은 방정식이 바로 **특성방정식(characteristic equation)**이며, 이를 풀면 고유값을 구할 수 있다. 이번 글에서는 특성방정식의 유도 과정과 실제 계산 방법을 단계별로 살펴보자.

---

## 특성방정식의 유도

### 핵심 아이디어: 연립방정식이 비자명해를 가지려면

고유값 정의식 $A\vec{v} = \lambda\vec{v}$를 변형하면:

$$A\vec{v} - \lambda\vec{v} = \vec{0}$$

$$A\vec{v} - \lambda I\vec{v} = \vec{0}$$

$$(A - \lambda I)\vec{v} = \vec{0}$$

이것은 행렬 $(A - \lambda I)$를 계수행렬로 하는 동차 연립방정식이다. $\vec{v} \neq \vec{0}$인 해(비자명해, nontrivial solution)가 존재하려면, 행렬 $(A - \lambda I)$가 **역행렬을 가지면 안 된다**. 역행렬이 존재하면 유일한 해 $\vec{v} = (A-\lambda I)^{-1}\vec{0} = \vec{0}$만 나오기 때문이다.

역행렬이 존재하지 않는다는 것은 행렬식이 0임을 의미하므로:

$$\det(A - \lambda I) = 0$$

이것이 **특성방정식(characteristic equation)**이다.

### 특성다항식

$\det(A - \lambda I)$를 $\lambda$에 대한 다항식으로 전개한 것을 **특성다항식(characteristic polynomial)**이라 한다. $n \times n$ 행렬에 대해 특성다항식의 차수는 $n$이며, 따라서 (복소수 범위에서) 정확히 $n$개의 고유값이 존재한다(중복 포함).

---

## 2×2 행렬 예시: 고유값 구하기

### 예시 행렬

$$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$

### 1단계: $(A - \lambda I)$ 구성

$$A - \lambda I = \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix}$$

### 2단계: 특성방정식 세우기

$$\det(A - \lambda I) = (4-\lambda)(3-\lambda) - (1)(2) = 0$$

$$= 12 - 4\lambda - 3\lambda + \lambda^2 - 2 = 0$$

$$= \lambda^2 - 7\lambda + 10 = 0$$

### 3단계: 특성다항식 인수분해

$$(\lambda - 5)(\lambda - 2) = 0$$

$$\therefore \quad \lambda_1 = 5, \quad \lambda_2 = 2$$

---

## 각 고유값에 대한 고유벡터 구하기

### $\lambda_1 = 5$에 대한 고유벡터

$(A - 5I)\vec{v} = \vec{0}$를 풀면:

$$A - 5I = \begin{pmatrix} 4-5 & 1 \\ 2 & 3-5 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}$$

행 축소하면 두 행이 같은 비율이므로(종속):

$$\begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} \rightarrow -v_1 + v_2 = 0 \rightarrow v_1 = v_2$$

자유변수 $v_2 = t$로 놓으면: $\vec{v} = t\begin{pmatrix}1\\1\end{pmatrix}$

고유벡터: $\vec{v}_1 = \begin{pmatrix}1\\1\end{pmatrix}$

**검증:** $A\vec{v}_1 = \begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix} = \begin{pmatrix}5\\5\end{pmatrix} = 5\begin{pmatrix}1\\1\end{pmatrix}$ ✓

### $\lambda_2 = 2$에 대한 고유벡터

$(A - 2I)\vec{v} = \vec{0}$를 풀면:

$$A - 2I = \begin{pmatrix} 4-2 & 1 \\ 2 & 3-2 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$$

행 축소:

$$\begin{pmatrix} 2 & 1 \\ 0 & 0 \end{pmatrix} \rightarrow 2v_1 + v_2 = 0 \rightarrow v_2 = -2v_1$$

자유변수 $v_1 = t$로 놓으면: $\vec{v} = t\begin{pmatrix}1\\-2\end{pmatrix}$

고유벡터: $\vec{v}_2 = \begin{pmatrix}1\\-2\end{pmatrix}$

**검증:** $A\vec{v}_2 = \begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}1\\-2\end{pmatrix} = \begin{pmatrix}2\\-4\end{pmatrix} = 2\begin{pmatrix}1\\-2\end{pmatrix}$ ✓

---

## 중복 고유값과 특수한 경우

### 대수적 중복도와 기하학적 중복도

고유값 $\lambda$가 특성다항식에서 $k$번 반복되어 나타날 때 **대수적 중복도(algebraic multiplicity)**가 $k$라고 한다. 이때 대응하는 선형독립 고유벡터의 수가 **기하학적 중복도(geometric multiplicity)**이며, 이는 항상 대수적 중복도 이하다:

$$1 \leq \text{기하학적 중복도} \leq \text{대수적 중복도}$$

### 2×2 특성방정식의 일반 공식

임의의 2×2 행렬 $A = \begin{pmatrix}a&b\\c&d\end{pmatrix}$에 대해:

$$\det(A - \lambda I) = \lambda^2 - (a+d)\lambda + (ad-bc) = 0$$

$$= \lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$$

여기서 $\text{tr}(A) = a + d$는 **대각합(trace)**, $\det(A) = ad - bc$는 행렬식이다. 고유값의 합과 곱에 대해 유용한 성질이 있다:

$$\lambda_1 + \lambda_2 = \text{tr}(A), \qquad \lambda_1 \cdot \lambda_2 = \det(A)$$

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 유도 과정 | $A\vec{v}=\lambda\vec{v} \Rightarrow (A-\lambda I)\vec{v}=\vec{0}$ |
| 특성방정식 | $\det(A - \lambda I) = 0$ |
| 특성다항식 차수 | $n \times n$ 행렬 $\Rightarrow$ $n$차 다항식 |
| 고유값 개수 | 복소수 범위에서 $n$개 (중복 포함) |
| 2×2 공식 | $\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$ |
| 고유값의 합 | $\lambda_1 + \cdots + \lambda_n = \text{tr}(A)$ |
| 고유값의 곱 | $\lambda_1 \cdots \lambda_n = \det(A)$ |
| 고유벡터 구하기 | 각 $\lambda$에 대해 $(A-\lambda I)\vec{v}=\vec{0}$ 풀기 |

> 다음 글에서는 **대각화(Diagonalization)**를 통해 고유값과 고유벡터를 활용해 행렬의 거듭제곱을 효율적으로 계산하는 방법을 알아본다.
