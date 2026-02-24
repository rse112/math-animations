# 6.3 대각화 (Diagonalization)

## 도입

$A^{30}$을 계산해야 한다고 상상해 보자. 행렬 곱셈을 30번 반복하는 것은 매우 번거롭고 오류가 생기기 쉽다. 하지만 만약 $A$가 대각행렬이라면? $D^{30}$은 각 대각 성분을 30제곱하기만 하면 된다. **대각화(Diagonalization)**는 이 아이디어를 일반 행렬로 확장한다. 고유값과 고유벡터를 이용해 복잡한 행렬을 본질적으로 대각행렬처럼 다룰 수 있게 해주는 강력한 기법이다.

대각화는 수학적 아름다움뿐만 아니라 응용에서도 핵심적이다. 미분방정식의 연립 시스템 풀기, 마르코프 연쇄에서 장기 확률 예측, 물리학에서 결합된 진동자 문제까지 --- 대각화는 복잡한 반복 계산을 단순하게 만들어주는 핵심 도구다.

---

## 대각화의 정의

### $A = PDP^{-1}$

$n \times n$ 행렬 $A$가 다음과 같이 분해될 때 $A$는 **대각화 가능(diagonalizable)**하다고 한다:

$$A = PDP^{-1}$$

여기서:
- $D$: 고유값들을 대각 성분으로 갖는 대각행렬
- $P$: 대응하는 고유벡터들을 열로 갖는 가역행렬
- $P^{-1}$: $P$의 역행렬

$$D = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}, \qquad P = \begin{pmatrix} | & | & & | \\ \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \\ | & | & & | \end{pmatrix}$$

---

## 대각화의 조건

### $n$개의 선형독립 고유벡터

$n \times n$ 행렬 $A$가 대각화 가능할 조건: **$n$개의 선형독립 고유벡터를 가져야 한다.**

이때 $P$의 열을 이 고유벡터들로 구성하면 $P$가 가역행렬이 된다.

**충분 조건**: $A$가 $n$개의 서로 다른 고유값을 가지면 대각화 가능하다. (서로 다른 고유값에 대응하는 고유벡터들은 항상 선형독립이다.)

하지만 중복 고유값이 있어도 대각화가 가능한 경우가 있고(각 고유값의 기하학적 중복도가 대수적 중복도와 같을 때), 불가능한 경우도 있다.

### 대각화가 불가능한 예

$$B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

특성방정식: $(1-\lambda)^2 = 0 \Rightarrow \lambda = 1$ (중복도 2)

$(B - I)\vec{v} = \begin{pmatrix}0&1\\0&0\end{pmatrix}\vec{v} = \vec{0}$의 해: $\vec{v} = t\begin{pmatrix}1\\0\end{pmatrix}$

선형독립 고유벡터가 1개뿐이므로 $B$는 **대각화 불가능**이다.

---

## 대각화 계산 예시

### 예시 행렬

앞서 6.2에서 다룬 행렬을 대각화해 보자:

$$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$

고유값: $\lambda_1 = 5$, $\lambda_2 = 2$

고유벡터: $\vec{v}_1 = \begin{pmatrix}1\\1\end{pmatrix}$, $\vec{v}_2 = \begin{pmatrix}1\\-2\end{pmatrix}$

### $P$, $D$, $P^{-1}$ 구성

$$P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}, \qquad D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}$$

$P^{-1}$ 계산: $\det(P) = (1)(-2) - (1)(1) = -3$

$$P^{-1} = \frac{1}{-3}\begin{pmatrix} -2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2/3 & 1/3 \\ 1/3 & -1/3 \end{pmatrix}$$

### 검증: $A = PDP^{-1}$

$$PDP^{-1} = \begin{pmatrix}1&1\\1&-2\end{pmatrix}\begin{pmatrix}5&0\\0&2\end{pmatrix}\begin{pmatrix}2/3&1/3\\1/3&-1/3\end{pmatrix}$$

$$= \begin{pmatrix}5&2\\5&-4\end{pmatrix}\begin{pmatrix}2/3&1/3\\1/3&-1/3\end{pmatrix} = \begin{pmatrix}4&1\\2&3\end{pmatrix} = A \checkmark$$

---

## 대각화의 핵심 활용: 행렬의 거듭제곱

### $A^k = PD^kP^{-1}$

대각화의 가장 강력한 응용은 행렬 거듭제곱의 효율적 계산이다:

$$A^k = (PDP^{-1})^k = PD^kP^{-1}$$

이 식이 성립하는 이유:

$$A^2 = (PDP^{-1})(PDP^{-1}) = PD(P^{-1}P)DP^{-1} = PD^2P^{-1}$$

$$A^k = PD^kP^{-1}$$

대각행렬의 거듭제곱은 각 대각 성분을 $k$제곱하면 된다:

$$D^k = \begin{pmatrix} \lambda_1^k & 0 & \cdots & 0 \\ 0 & \lambda_2^k & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n^k \end{pmatrix}$$

### 예시: $A^{10}$ 계산

$$A^{10} = PD^{10}P^{-1} = \begin{pmatrix}1&1\\1&-2\end{pmatrix}\begin{pmatrix}5^{10}&0\\0&2^{10}\end{pmatrix}\begin{pmatrix}2/3&1/3\\1/3&-1/3\end{pmatrix}$$

$5^{10} = 9{,}765{,}625$, $2^{10} = 1{,}024$

행렬 곱을 30번 반복하는 것 대신, 단 몇 번의 계산으로 끝난다.

---

## 대각화와 선형 점화식

### 피보나치 수열에의 응용

피보나치 수열 $F_{n+2} = F_{n+1} + F_n$을 행렬 형태로 표현하면:

$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix}$$

이 행렬을 대각화하면 $F_n$의 닫힌 형태(closed form) 공식을 유도할 수 있다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 대각화 정의 | $A = PDP^{-1}$ |
| $P$ 구성 | 열 = 선형독립 고유벡터 $\vec{v}_1, \ldots, \vec{v}_n$ |
| $D$ 구성 | 대각 = 대응 고유값 $\lambda_1, \ldots, \lambda_n$ |
| 대각화 조건 | $n \times n$ 행렬이 $n$개의 선형독립 고유벡터 보유 |
| 충분 조건 | $n$개의 서로 다른 고유값 존재 |
| 거듭제곱 | $A^k = PD^kP^{-1}$ |
| $D^k$ 계산 | 각 대각 성분의 $k$제곱 |
| 대각화 불가 | 선형독립 고유벡터가 $n$개 미만인 경우 |

> 다음 글에서는 **고유값의 기하학적 의미**를 더 깊이 탐구하고, 대칭행렬의 특별한 성질과 스펙트럴 분해를 살펴본다.
