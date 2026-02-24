# 7.3 최소제곱법 (Least Squares)

## 도입

기상청 연구원이 지난 10년간의 기온 데이터를 가지고 온난화 추세를 분석하려 한다. 데이터 점이 10개면 방정식도 10개이지만, 구하고 싶은 미지수(직선의 기울기와 절편)는 2개뿐이다. 이 10개의 방정식을 동시에 완벽하게 만족하는 직선은 없다. 그렇다면 "가장 잘 맞는" 직선은 무엇일까?

**최소제곱법(Least Squares)**은 이 질문에 대한 수학적으로 엄밀하고 우아한 답을 제공한다. 모든 데이터 점과의 오차의 제곱합을 최소화하는 해를 구하는 방법으로, 선형회귀(linear regression), 신호 복원, 로봇 위치 추정, 컴퓨터 비전 등 현대 공학과 데이터 과학의 거의 모든 분야에서 사용된다.

---

## 문제 설정

### 과결정 시스템 (Overdetermined System)

방정식의 수 $m$이 미지수의 수 $n$보다 클 때($m > n$), 보통 $A\vec{x} = \vec{b}$에는 정확한 해가 존재하지 않는다. 이때 우리는 **오차(residual)를 최소화**하는 $\hat{x}$를 찾는다:

$$\hat{x} = \arg\min_{\vec{x}} \|A\vec{x} - \vec{b}\|^2$$

$\|A\vec{x} - \vec{b}\|^2$은 각 방정식에서의 오차의 제곱합이다:

$$\|A\vec{x} - \vec{b}\|^2 = \sum_{i=1}^{m} ([\text{i번째 행}] \cdot \vec{x} - b_i)^2$$

---

## 정규방정식 (Normal Equations)

### 유도: 기하학적 관점

$A\hat{x}$는 $A$의 열공간 $C(A)$ 위의 벡터다. $\vec{b}$가 $C(A)$ 위에 있지 않을 때, $\|A\vec{x} - \vec{b}\|$를 최소화하는 것은 $\vec{b}$를 $C(A)$에 **정사영(orthogonal projection)**한 벡터 $A\hat{x}$를 찾는 것과 같다.

정사영의 핵심 조건: 잔차(residual) $\vec{r} = \vec{b} - A\hat{x}$가 $C(A)$와 직교해야 한다. 즉, $A$의 모든 열 $\vec{a}_j$에 대해:

$$\vec{a}_j \cdot (\vec{b} - A\hat{x}) = 0 \quad \text{for all } j$$

이를 행렬 형태로 쓰면:

$$A^T(\vec{b} - A\hat{x}) = \vec{0}$$

$$A^T A\hat{x} = A^T\vec{b}$$

이것이 **정규방정식(normal equations)**이다.

### 최소제곱 해

$A^TA$가 가역이면 (즉, $A$의 열들이 선형독립이면):

$$\hat{x} = (A^TA)^{-1}A^T\vec{b}$$

행렬 $(A^TA)^{-1}A^T$를 **의사역행렬(pseudoinverse)**의 특수한 경우라고도 하며, $A^+$로 표기하기도 한다.

---

## 직선 피팅 예시

### 문제: 3개의 데이터 점에 직선 피팅

데이터: $(1, 1)$, $(2, 2)$, $(3, 4)$

직선 $y = c_1 + c_2 x$를 피팅하면, 과결정 시스템:

$$\begin{pmatrix}1 & 1 \\ 1 & 2 \\ 1 & 3\end{pmatrix}\begin{pmatrix}c_1 \\ c_2\end{pmatrix} = \begin{pmatrix}1 \\ 2 \\ 4\end{pmatrix}$$

$$A = \begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix}, \quad \vec{b} = \begin{pmatrix}1\\2\\4\end{pmatrix}$$

**정규방정식 계산:**

$$A^TA = \begin{pmatrix}1&1&1\\1&2&3\end{pmatrix}\begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix} = \begin{pmatrix}3&6\\6&14\end{pmatrix}$$

$$A^T\vec{b} = \begin{pmatrix}1&1&1\\1&2&3\end{pmatrix}\begin{pmatrix}1\\2\\4\end{pmatrix} = \begin{pmatrix}7\\17\end{pmatrix}$$

**정규방정식 풀기:**

$$\begin{pmatrix}3&6\\6&14\end{pmatrix}\begin{pmatrix}c_1\\c_2\end{pmatrix} = \begin{pmatrix}7\\17\end{pmatrix}$$

$\det(A^TA) = 3 \cdot 14 - 6 \cdot 6 = 42 - 36 = 6$

$$(A^TA)^{-1} = \frac{1}{6}\begin{pmatrix}14&-6\\-6&3\end{pmatrix}$$

$$\hat{x} = \frac{1}{6}\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}7\\17\end{pmatrix} = \frac{1}{6}\begin{pmatrix}98-102\\-42+51\end{pmatrix} = \frac{1}{6}\begin{pmatrix}-4\\9\end{pmatrix} = \begin{pmatrix}-2/3\\3/2\end{pmatrix}$$

최적 직선: $y = -\dfrac{2}{3} + \dfrac{3}{2}x$

---

## 기하학적 의미와 잔차

### 잔차는 열공간에 직교한다

최소제곱 해 $\hat{x}$에서의 잔차:

$$\vec{r} = \vec{b} - A\hat{x}$$

이 잔차는 $A$의 열공간 $C(A)$에 직교한다:

$$A^T\vec{r} = A^T(\vec{b} - A\hat{x}) = A^T\vec{b} - A^TA\hat{x} = \vec{0}$$

위 예시에서:

$$A\hat{x} = \begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix}\begin{pmatrix}-2/3\\3/2\end{pmatrix} = \begin{pmatrix}5/6\\7/3\\19/6\end{pmatrix}$$

$$\vec{r} = \begin{pmatrix}1\\2\\4\end{pmatrix} - \begin{pmatrix}5/6\\7/3\\19/6\end{pmatrix} = \begin{pmatrix}1/6\\-1/3\\5/6\end{pmatrix}$$

잔차 제곱합: $\|\vec{r}\|^2 = \frac{1}{36} + \frac{1}{9} + \frac{25}{36} = \frac{1+4+25}{36} = \frac{30}{36} = \frac{5}{6}$

---

## QR 분해를 이용한 최소제곱법

$A = QR$로 분해하면 정규방정식이 단순해진다:

$$A^TA\hat{x} = A^T\vec{b}$$

$$(QR)^T(QR)\hat{x} = (QR)^T\vec{b}$$

$$R^T Q^T Q R\hat{x} = R^TQ^T\vec{b}$$

$$R^TR\hat{x} = R^TQ^T\vec{b}$$

$$R\hat{x} = Q^T\vec{b}$$

$R$이 상삼각행렬이므로 역대입(back substitution)으로 쉽게 풀 수 있으며, $(A^TA)^{-1}$을 직접 계산하는 것보다 **수치적으로 안정적**이다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 목적 | $\|A\vec{x}-\vec{b}\|^2$ 최소화 |
| 정규방정식 | $A^TA\hat{x} = A^T\vec{b}$ |
| 최소제곱 해 | $\hat{x} = (A^TA)^{-1}A^T\vec{b}$ |
| 기하학적 의미 | $A\hat{x}$는 $\vec{b}$의 $C(A)$로의 정사영 |
| 잔차 | $\vec{r} = \vec{b} - A\hat{x}$ |
| 잔차의 성질 | $\vec{r} \perp C(A)$, 즉 $A^T\vec{r} = \vec{0}$ |
| QR 분해 활용 | $R\hat{x} = Q^T\vec{b}$ (수치 안정적) |
| 응용 | 선형회귀, 데이터 피팅, 신호 복원 |

> 다음 글에서는 **특이값 분해(SVD)**를 살펴보며, 모든 행렬을 세 가지 단순한 변환의 합성으로 분해하는 가장 강력한 행렬 분해법을 소개한다.
