# 5.2 선형 독립과 기저

## 도입

등산 지도를 펼쳤을 때 "동쪽"과 "북쪽"이라는 두 방향이 있다.
이 두 방향은 서로 "진짜 다른" 방향이다 — 동쪽으로만 아무리 걸어도 북쪽으로는 이동하지 않는다.

이제 "동쪽"과 "동북쪽"을 생각해보자.
동북쪽은 동쪽 $\frac{1}{\sqrt{2}}$배 + 북쪽 $\frac{1}{\sqrt{2}}$배이므로 "새로운 방향"이 아니다.
이미 알고 있는 두 방향의 조합일 뿐이다.

이처럼 벡터들이 서로 "진짜로 다른" 방향을 가리키는지 판단하는 개념이 **선형 독립**이다.
그리고 선형 독립이면서 공간 전체를 생성하는 벡터 집합이 바로 **기저(Basis)**다.

---

## 선형 독립의 정의

벡터들 $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$이 **선형 독립(Linearly Independent)**이란

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0}$$

의 유일한 해가 $c_1 = c_2 = \cdots = c_k = 0$인 경우다.

즉, 영벡터를 만드는 유일한 방법은 "모든 계수를 0으로 두는 것"뿐이다.

**판별법:** 벡터들을 열로 세운 행렬 $A = [\vec{v}_1 \mid \vec{v}_2 \mid \cdots \mid \vec{v}_k]$에서
$A\vec{c} = \vec{0}$의 유일 해가 $\vec{c} = \vec{0}$이면 선형 독립이다.

---

## 선형 종속의 정의

벡터들이 **선형 종속(Linearly Dependent)**이란 선형 독립이 아닌 경우다.
즉, 모두 0이 아닌 계수 $c_1, \ldots, c_k$가 존재해서

$$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{0}$$

이 성립한다.

이는 등가적으로: 적어도 하나의 벡터가 나머지들의 **선형결합**으로 표현된다는 뜻이다.

예를 들어 $c_1 \neq 0$이면

$$\vec{v}_1 = -\frac{c_2}{c_1}\vec{v}_2 - \cdots - \frac{c_k}{c_1}\vec{v}_k$$

$\vec{v}_1$이 나머지 벡터들로 표현되므로 "새로운 방향"을 제공하지 못한다.

---

## 예시로 확인하기

**선형 독립 예시:**

$$\vec{v}_1 = \begin{pmatrix}1\\0\end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix}0\\1\end{pmatrix}$$

$c_1\begin{pmatrix}1\\0\end{pmatrix} + c_2\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}$이려면 반드시 $c_1 = 0$, $c_2 = 0$. 선형 독립.

**선형 종속 예시:**

$$\vec{v}_1 = \begin{pmatrix}1\\2\end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix}2\\4\end{pmatrix}$$

$\vec{v}_2 = 2\vec{v}_1$이므로 $2\vec{v}_1 - \vec{v}_2 = \vec{0}$. 계수 $(2, -1)$이 모두 0이 아니므로 선형 종속.

---

## 기저 (Basis)

벡터 공간 $V$의 **기저(Basis)**는 다음 두 조건을 동시에 만족하는 벡터 집합이다.

1. **선형 독립:** 서로 "중복"되는 방향이 없다.
2. **$V$를 생성:** 이 벡터들의 선형결합으로 $V$의 모든 벡터를 나타낼 수 있다.

기저는 공간을 기술하기 위한 "최소한의 정보"다.

---

## 표준 기저 (Standard Basis)

$\mathbb{R}^n$의 **표준 기저**는 각 축 방향의 단위벡터들이다:

$$\hat{e}_1 = \begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},\quad \hat{e}_2 = \begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},\quad \ldots,\quad \hat{e}_n = \begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}$$

임의의 벡터 $\vec{x} = (x_1, x_2, \ldots, x_n)^\top$는

$$\vec{x} = x_1\hat{e}_1 + x_2\hat{e}_2 + \cdots + x_n\hat{e}_n$$

으로 **유일하게** 표현된다.

---

## 기저와 좌표의 유일성

기저 $\mathcal{B} = \{\vec{b}_1, \ldots, \vec{b}_n\}$가 주어지면,
$V$의 임의의 벡터 $\vec{v}$는

$$\vec{v} = c_1\vec{b}_1 + c_2\vec{b}_2 + \cdots + c_n\vec{b}_n$$

으로 **유일하게** 표현된다. 계수 $(c_1, c_2, \ldots, c_n)$을 $\mathcal{B}$에 대한 $\vec{v}$의 **좌표**라 한다.

유일성이 보장되기 때문에 기저는 "좌표계"의 역할을 한다.
GPS 좌표처럼, 기저를 정하면 공간 안의 모든 점을 유일한 숫자 묶음으로 표현할 수 있다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 선형 독립 | $c_1\vec{v}_1+\cdots+c_k\vec{v}_k=\vec{0} \Rightarrow$ 모든 $c_i=0$ |
| 선형 종속 | 영이 아닌 $c_i$가 존재하여 선형결합이 $\vec{0}$ |
| 종속의 의미 | 하나의 벡터가 나머지들의 선형결합으로 표현됨 |
| 기저 조건 | 선형 독립 + 공간 생성 (두 조건 동시 만족) |
| 표준 기저 | $\{\hat{e}_1, \ldots, \hat{e}_n\}$, $i$번째 성분만 1인 단위벡터 |
| 좌표의 유일성 | 기저가 주어지면 모든 벡터의 표현이 유일 |

> 다음 글에서는 **차원 — 기저의 원소 개수가 왜 항상 같은지**를 알아본다.
