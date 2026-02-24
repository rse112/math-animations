# 3.3 역행렬과 행렬식

## 도입

스칼라 방정식 $ax = b$를 풀 때, $a \neq 0$이면 양변에 $a^{-1} = \frac{1}{a}$를 곱해 $x = a^{-1}b$를 얻는다. 행렬 방정식 $A\vec{x} = \vec{b}$도 같은 아이디어로 풀 수 있다면 어떨까? 만약 행렬 $A$에 대해 "행렬 버전의 역수"가 존재한다면, 양변에 그것을 곱해 $\vec{x}$를 구할 수 있다. 이것이 **역행렬(Inverse Matrix)**의 핵심 아이디어다.

그러나 모든 $a$가 역수를 갖지는 않는다 — $a = 0$이면 $\frac{1}{0}$은 존재하지 않는다. 행렬에도 마찬가지로 역행렬이 존재하지 않는 경우가 있다. 역행렬의 존재 여부를 판단하는 도구가 **행렬식(Determinant)**이다.

---

## 역행렬의 정의

### 정의

$n \times n$ 정방행렬 $A$에 대해, 다음을 만족하는 행렬 $A^{-1}$을 $A$의 **역행렬**이라 한다.

$$A A^{-1} = A^{-1} A = I$$

역행렬이 존재하는 행렬을 **가역행렬(Invertible Matrix)** 또는 **비특이행렬(Non-singular Matrix)**이라 하고, 역행렬이 존재하지 않으면 **특이행렬(Singular Matrix)**이라 한다.

### 역행렬의 유일성

역행렬이 존재하면 그것은 유일하다. 만약 $B$와 $C$ 둘 다 $A$의 역행렬이라면:

$$B = BI = B(AC) = (BA)C = IC = C$$

### 역행렬의 성질

$$(A^{-1})^{-1} = A$$
$$(AB)^{-1} = B^{-1}A^{-1} \quad \text{(순서 역전!)}$$
$$(A^T)^{-1} = (A^{-1})^T$$
$$(cA)^{-1} = \frac{1}{c}A^{-1} \quad (c \neq 0)$$

---

## 2×2 역행렬 공식

### 공식

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

단, $ad - bc \neq 0$이어야 한다.

### 기억법

대각선 원소를 맞바꾸고($a \leftrightarrow d$), 비대각 원소의 부호를 바꾼 뒤($b \to -b$, $c \to -c$), $\frac{1}{ad-bc}$를 곱한다.

### 예시

$$A = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$$

$$\det A = 3 \cdot 2 - 1 \cdot 5 = 6 - 5 = 1$$

$$A^{-1} = \frac{1}{1}\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$$

검증: $AA^{-1} = \begin{pmatrix}3&1\\5&2\end{pmatrix}\begin{pmatrix}2&-1\\-5&3\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$ $\checkmark$

---

## 행렬식 (Determinant)

### 2×2 행렬식

$$\det A = \det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

또는 $|A|$로도 표기한다.

### 기하학적 의미 — 넓이 배율

2차원에서 행렬 $A$의 열벡터들이 이루는 **평행사변형의 넓이**가 $|\det A|$이다. 더 일반적으로, $A$는 공간의 모든 도형의 넓이를 $|\det A|$배로 바꾼다.

- $|\det A| > 1$: 넓이가 확대된다.
- $|\det A| = 1$: 넓이가 보존된다 (등적 변환).
- $|\det A| = 0$: 넓이가 0이 된다 — 평면이 선으로 찌부러진다.
- $\det A < 0$: 방향(오리엔테이션)이 뒤집힌다.

### 3×3 행렬식

$$\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = a_{11}(a_{22}a_{33}-a_{23}a_{32}) - a_{12}(a_{21}a_{33}-a_{23}a_{31}) + a_{13}(a_{21}a_{32}-a_{22}a_{31})$$

이 전개를 **라플라스 전개(Laplace Expansion)**라 하며, 첫 번째 행에 대해 전개한 것이다.

---

## 행렬식의 성질

### 곱의 행렬식

$$\det(AB) = \det(A) \cdot \det(B)$$

이 성질은 매우 강력하다. 행렬 곱의 행렬식을 각각 따로 계산해 곱한 것과 같다.

### 전치행렬의 행렬식

$$\det(A^T) = \det(A)$$

### 역행렬의 행렬식

$$\det(A^{-1}) = \frac{1}{\det(A)}$$

$\det(AA^{-1}) = \det(I) = 1$이고, $\det(A)\det(A^{-1}) = 1$이므로 성립한다.

### 스칼라 곱의 행렬식

$$\det(cA) = c^n \det(A) \quad (n \times n \text{ 행렬})$$

---

## 역행렬 존재 조건

$$\boxed{A^{-1} \text{ 존재} \quad \Leftrightarrow \quad \det A \neq 0}$$

이것이 핵심 판정 기준이다. $\det A = 0$이면 $A$는 특이행렬로, 역행렬이 존재하지 않는다.

기하학적으로 $\det A = 0$은 변환 후 공간이 더 낮은 차원으로 "찌부러진다"는 것을 의미한다. 정보가 손실되므로 역변환(원래 상태로 돌아가기)이 불가능하다.

$$A\vec{x} = \vec{b} \text{ 의 유일해} \quad \Leftrightarrow \quad \det A \neq 0 \quad \Leftrightarrow \quad \vec{x} = A^{-1}\vec{b}$$

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 역행렬 정의 | $AA^{-1} = A^{-1}A = I$ |
| 2×2 역행렬 | $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| $(AB)^{-1}$ | $B^{-1}A^{-1}$ (순서 역전) |
| 2×2 행렬식 | $\det A = ad - bc$ |
| 기하학적 의미 | 넓이(부피) 배율 $= |\det A|$ |
| 곱의 행렬식 | $\det(AB) = \det A \cdot \det B$ |
| 역행렬 존재 조건 | $\det A \neq 0$ |
| 연립방정식 해 | $\det A \neq 0$이면 $\vec{x} = A^{-1}\vec{b}$ |

> 다음 글에서는 **선형변환(Linear Transformation)**을 알아본다. 행렬이 벡터 공간을 어떻게 변환하는지, 그 기하학적 의미를 깊이 탐구한다.
