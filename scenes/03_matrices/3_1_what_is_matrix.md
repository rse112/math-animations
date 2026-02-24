# 3.1 행렬이란?

## 도입

세 가지 물건 A, B, C를 판매하는 가게가 있다고 하자. 각 물건의 가격과 재고를 관리하려면 어떻게 할까? 표를 그리는 것이 가장 자연스럽다. 행에는 물건 종류를, 열에는 속성(가격, 재고, 판매량)을 배치하면 한눈에 모든 정보를 파악할 수 있다. 수학에서 이렇게 숫자를 직사각형 형태로 배열한 것을 **행렬(Matrix)**이라고 한다.

행렬은 단순한 데이터 저장 구조를 넘어선다. 연립방정식을 행렬 형태로 쓰면 복잡한 계산을 체계적으로 처리할 수 있고, 선형 변환(회전, 확대, 반사)을 행렬 하나로 표현할 수 있다. 현대 수학, 물리학, 컴퓨터 과학, 머신러닝 전반에서 행렬은 없어서는 안 될 언어다.

---

## 행렬의 정의

### 기본 정의

**$m \times n$ 행렬**이란 $m$개의 행(row)과 $n$개의 열(column)로 이루어진 숫자의 직사각형 배열이다.

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$

성분 $a_{ij}$는 $i$번째 행, $j$번째 열에 위치한 원소를 의미한다. 행 번호가 먼저, 열 번호가 나중에 온다는 규칙을 기억하자.

### 연립방정식과의 관계

다음 연립방정식을 생각해 보자.

$$\begin{cases} 2x + 3y = 5 \\ x - y = 1 \end{cases}$$

계수만 모아 행렬로 쓰면:

$$A = \begin{pmatrix} 2 & 3 \\ 1 & -1 \end{pmatrix}, \quad \vec{x} = \begin{pmatrix} x \\ y \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$$

그러면 연립방정식은 단 하나의 행렬 방정식으로 표현된다.

$$A\vec{x} = \vec{b}$$

---

## 특수 행렬

### 영행렬 (Zero Matrix)

모든 성분이 0인 행렬이다. 덧셈의 항등원 역할을 한다.

$$O = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$

$A + O = A$가 항상 성립한다.

### 단위행렬 (Identity Matrix)

대각선 성분은 1이고 나머지는 모두 0인 **정방행렬**이다. 곱셈의 항등원이다.

$$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix}$$

$AI = IA = A$가 항상 성립한다.

### 정방행렬 (Square Matrix)

행과 열의 수가 같은 행렬, 즉 $n \times n$ 행렬이다. 역행렬, 행렬식 등 많은 개념이 정방행렬에서 정의된다.

### 대각행렬 (Diagonal Matrix)

대각선 원소 이외의 성분이 모두 0인 정방행렬이다.

$$D = \begin{pmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{pmatrix}$$

대각행렬끼리의 곱은 계산이 매우 쉽다. 대각 성분만 서로 곱하면 된다.

---

## 전치행렬

### 정의

행렬 $A$의 **전치행렬(Transpose)** $A^T$는 $A$의 행과 열을 서로 바꾼 행렬이다. 즉, $(A^T)_{ij} = A_{ji}$이다.

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \implies A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

$A$가 $m \times n$이면 $A^T$는 $n \times m$이다.

### 전치행렬의 성질

$$\left(A^T\right)^T = A$$
$$(A + B)^T = A^T + B^T$$
$$(cA)^T = cA^T$$
$$(AB)^T = B^T A^T \quad \text{(순서 역전에 주의!)}$$

---

## 대칭행렬

전치행렬이 자기 자신과 같은 정방행렬을 **대칭행렬(Symmetric Matrix)**이라 한다.

$$A^T = A \quad \Leftrightarrow \quad a_{ij} = a_{ji}$$

대칭행렬은 대각선을 기준으로 대칭인 모양을 가진다. 공분산 행렬, 그래프의 인접 행렬 등 실전에서 자주 등장한다.

$$S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 4 \\ 3 & 4 & 6 \end{pmatrix}$$

반대로 $A^T = -A$를 만족하는 행렬은 **반대칭행렬(Skew-Symmetric Matrix)**이라 한다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| $m \times n$ 행렬 | $m$행 $n$열의 수 배열, 성분 $a_{ij}$ |
| 영행렬 | 모든 성분이 0, $A + O = A$ |
| 단위행렬 | 대각이 1, 나머지 0, $AI = IA = A$ |
| 정방행렬 | 행 수 = 열 수 ($n \times n$) |
| 대각행렬 | 비대각 성분이 모두 0 |
| 전치행렬 | $(A^T)_{ij} = A_{ji}$, $(AB)^T = B^T A^T$ |
| 대칭행렬 | $A^T = A$, 즉 $a_{ij} = a_{ji}$ |

> 다음 글에서는 **행렬 연산**을 알아본다. 행렬의 덧셈, 뺄셈, 스칼라 곱, 그리고 행렬 곱셈의 규칙을 다룬다.
