# 4.1 선형변환이란?

## 도입

지도를 손으로 잡아당겨 늘리거나, 종이를 회전시켜 다른 방향으로 펼치는 상상을 해보자.
지도 위의 모든 점이 **동시에**, 그리고 **규칙적으로** 움직인다면 — 이것이 바로 **선형변환**의 직관이다.

선형변환은 벡터 공간을 "구부리지 않고" 변환하는 함수다.
직선은 직선으로, 원점은 원점으로, 평행한 선은 여전히 평행하게 유지된다.
컴퓨터 그래픽스, 물리 시뮬레이션, 머신러닝의 신경망까지 — 선형변환은 수학의 핵심 도구다.

---

## 선형변환의 정의

**선형변환(Linear Transformation)**이란 두 벡터 공간 사이의 함수

$$T : \mathbb{R}^n \to \mathbb{R}^m$$

로서, 다음 두 가지 조건을 만족하는 것이다.

**조건 1 — 덧셈 보존 (Additivity):**

$$T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$$

**조건 2 — 스칼라 곱 보존 (Homogeneity):**

$$T(c\vec{u}) = c\,T(\vec{u})$$

두 조건을 하나로 합치면:

$$T(c_1\vec{u} + c_2\vec{v}) = c_1\,T(\vec{u}) + c_2\,T(\vec{v})$$

이를 **선형성(linearity)**이라 부른다.

### 선형변환이 아닌 예시

함수 $f(x) = x + 3$은 선형변환이 아니다.
$f(0) = 3 \neq 0$ 이므로 원점이 원점으로 가지 않는다.

선형변환은 반드시 $T(\vec{0}) = \vec{0}$을 만족해야 한다.

---

## 행렬 표현

모든 선형변환 $T : \mathbb{R}^n \to \mathbb{R}^m$은 **행렬**로 완전히 표현할 수 있다.

$$T(\vec{x}) = A\vec{x}$$

여기서 $A$는 $m \times n$ 행렬이다.

이 사실은 매우 강력하다.
선형변환의 모든 정보가 행렬 하나에 압축되어 있기 때문이다.

---

## 기저벡터의 상(Image)

$\mathbb{R}^2$의 표준 기저벡터를 떠올려 보자.

$$\hat{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \hat{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

선형변환 $T$를 기저벡터에 적용했을 때의 결과를 각각

$$T(\hat{e}_1) = \begin{pmatrix} a \\ c \end{pmatrix}, \quad T(\hat{e}_2) = \begin{pmatrix} b \\ d \end{pmatrix}$$

라 하면, 대응하는 행렬은

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

즉, **기저벡터의 상이 행렬의 열(column)**이 된다.

임의의 벡터 $\vec{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$에 대해

$$T(\vec{x}) = x_1\,T(\hat{e}_1) + x_2\,T(\hat{e}_2) = x_1 \begin{pmatrix} a \\ c \end{pmatrix} + x_2 \begin{pmatrix} b \\ d \end{pmatrix} = A\vec{x}$$

---

## 예시: 단위 정사각형의 변환

단위 정사각형의 꼭짓점은

$$\begin{pmatrix}0\\0\end{pmatrix},\quad \begin{pmatrix}1\\0\end{pmatrix},\quad \begin{pmatrix}1\\1\end{pmatrix},\quad \begin{pmatrix}0\\1\end{pmatrix}$$

행렬 $A = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$으로 변환하면

$$\begin{pmatrix}0\\0\end{pmatrix} \to \begin{pmatrix}0\\0\end{pmatrix},\quad \begin{pmatrix}1\\0\end{pmatrix} \to \begin{pmatrix}2\\0\end{pmatrix},\quad \begin{pmatrix}1\\1\end{pmatrix} \to \begin{pmatrix}3\\1\end{pmatrix},\quad \begin{pmatrix}0\\1\end{pmatrix} \to \begin{pmatrix}1\\1\end{pmatrix}$$

정사각형이 **평행사변형**으로 변환되었다.
직선은 직선으로, 평행선은 평행선으로 유지된다 — 이것이 선형성의 기하학적 의미다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 선형변환 정의 | $T : \mathbb{R}^n \to \mathbb{R}^m$, 덧셈·스칼라 곱 보존 |
| 덧셈 보존 | $T(\vec{u}+\vec{v}) = T(\vec{u})+T(\vec{v})$ |
| 스칼라 곱 보존 | $T(c\vec{u}) = c\,T(\vec{u})$ |
| 원점 조건 | $T(\vec{0}) = \vec{0}$ (선형변환의 필요 조건) |
| 행렬 표현 | $T(\vec{x}) = A\vec{x}$ (모든 선형변환은 행렬로 표현됨) |
| 열 = 기저의 상 | $A$의 각 열은 $T(\hat{e}_i)$ |
| 기하학적 의미 | 직선 → 직선, 평행선 → 평행선, 정사각형 → 평행사변형 |

> 다음 글에서는 **2D 선형변환의 구체적인 종류들 — 회전, 반사, 전단, 크기 조정**을 알아본다.
