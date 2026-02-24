# 3.2 행렬 연산

## 도입

지도 앱을 사용할 때, 화면을 먼저 30° 회전한 뒤 2배로 확대한다고 하자. 두 변환을 따로따로 적용해도 되지만, 미리 두 변환을 합쳐 "회전 후 확대"를 한 번에 수행하는 단일 변환으로 만들 수도 있다. 행렬 연산, 특히 **행렬 곱셈**이 바로 이 역할을 한다. 두 변환을 연속으로 합성한 결과를 하나의 행렬로 표현할 수 있는 것이다.

행렬 연산에는 덧셈, 스칼라 곱, 행렬 곱셈이 있다. 이 중 행렬 곱셈은 일반 수의 곱셈과 다른 규칙을 가지며, 이 차이를 정확히 이해하는 것이 선형대수 전체의 기초가 된다.

---

## 행렬의 덧셈과 뺄셈

### 정의

두 행렬의 **크기가 같을 때(동형 행렬)**에만 덧셈과 뺄셈이 정의된다. 같은 위치의 성분끼리 더하거나 뺀다.

$$(A + B)_{ij} = a_{ij} + b_{ij}$$
$$(A - B)_{ij} = a_{ij} - b_{ij}$$

### 예시

$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$

### 성질

$$A + B = B + A \quad \text{(교환법칙)}$$
$$(A + B) + C = A + (B + C) \quad \text{(결합법칙)}$$
$$A + O = A \quad \text{(항등원)}$$
$$A + (-A) = O \quad \text{(역원)}$$

---

## 스칼라 곱 (Scalar Multiplication)

### 정의

스칼라(실수) $c$와 행렬 $A$의 곱은 $A$의 모든 성분에 $c$를 곱한 것이다.

$$(cA)_{ij} = c \cdot a_{ij}$$

### 예시

$$3 \begin{pmatrix} 1 & -2 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 3 & -6 \\ 0 & 12 \end{pmatrix}$$

### 성질

$$c(A + B) = cA + cB$$
$$(c + d)A = cA + dA$$
$$(cd)A = c(dA)$$
$$1 \cdot A = A$$

---

## 행렬 곱셈

### 크기 조건

$A$가 $m \times n$ 행렬이고 $B$가 $n \times p$ 행렬일 때, **$A$의 열 수와 $B$의 행 수가 같아야** 행렬 곱 $AB$가 정의된다. 결과는 $m \times p$ 행렬이다.

$$\underbrace{A}_{m \times n} \cdot \underbrace{B}_{n \times p} = \underbrace{AB}_{m \times p}$$

### 정의

$(AB)_{ij}$는 $A$의 $i$번째 행과 $B$의 $j$번째 열의 **내적**이다.

$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{in}b_{nj}$$

### 예시

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

$$AB = \begin{pmatrix} 1\cdot5+2\cdot7 & 1\cdot6+2\cdot8 \\ 3\cdot5+4\cdot7 & 3\cdot6+4\cdot8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

---

## 행렬 곱셈의 성질

### 결합법칙 (성립)

$$(AB)C = A(BC)$$

세 변환을 순서대로 합성하는 방식이 어느 쪽을 먼저 묶어도 결과가 같음을 의미한다.

### 분배법칙 (성립)

$$A(B + C) = AB + AC$$
$$(A + B)C = AC + BC$$

### 단위행렬과의 곱

$$AI = IA = A$$

### 교환법칙 (일반적으로 불성립)

$$AB \neq BA \quad \text{(일반적으로)}$$

이것은 행렬 곱셈의 가장 중요한 특징이다. 일반 수에서는 $ab = ba$이지만, 행렬에서는 성립하지 않는다.

**반례:**

$$A = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 1 \\ 0 & 2 \end{pmatrix}$$

$$AB = \begin{pmatrix} 0 & 5 \\ 0 & 0 \end{pmatrix}, \quad BA = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$

$AB \neq BA$임을 확인할 수 있다.

### 영인자 존재

일반 수에서 $ab = 0$이면 $a = 0$ 또는 $b = 0$이지만, 행렬에서는 $AB = O$이더라도 $A \neq O$이고 $B \neq O$일 수 있다.

위 반례에서 $BA = O$이지만 $A \neq O$이고 $B \neq O$이다.

---

## 행렬 곱셈의 기하학적 의미

$\vec{x}$에 $B$를 곱해 변환하고, 그 결과에 $A$를 곱해 또 다른 변환을 적용하는 것은:

$$(AB)\vec{x} = A(B\vec{x})$$

즉, $AB$는 "먼저 $B$로 변환, 그 다음 $A$로 변환"하는 합성 변환을 나타내는 행렬이다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 행렬 덧셈 | 같은 크기일 때만 가능, 성분별 덧셈 |
| 스칼라 곱 | 모든 성분에 스칼라를 곱함 |
| 행렬 곱 크기 조건 | $m \times n$ 곱하기 $n \times p$ = $m \times p$ |
| 행렬 곱 성분 | $(AB)_{ij} = \sum_k a_{ik} b_{kj}$ |
| 결합법칙 | $(AB)C = A(BC)$ 성립 |
| 교환법칙 | $AB \neq BA$ (일반적으로 불성립) |
| 분배법칙 | $A(B+C) = AB + AC$ 성립 |
| 기하학적 의미 | 행렬 곱 = 선형 변환의 합성 |

> 다음 글에서는 **역행렬과 행렬식**을 알아본다. 행렬 방정식 $A\vec{x}=\vec{b}$를 풀기 위한 핵심 도구를 다룬다.
