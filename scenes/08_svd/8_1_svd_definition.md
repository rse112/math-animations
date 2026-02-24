# 8.1 특이값 분해 (SVD) 정의

## 도입

행렬 분해의 세계에서 SVD(Singular Value Decomposition, 특이값 분해)는 단연 가장 강력하고 범용적인 도구다. 고유값 분해는 정방행렬에만 적용되고, 대각화는 일부 행렬에만 가능하며, QR 분해는 특정 방정식 풀기에 특화되어 있다. 하지만 SVD는 **모든 행렬**에 적용된다. 직사각행렬이든 정방행렬이든, 가역이든 특이행렬이든 예외가 없다.

SVD의 본질적 아이디어는 아름답다. 어떤 복잡한 선형변환이든, 그것을 세 가지 단순한 동작으로 분해할 수 있다: **회전 → 축 방향 늘리기 → 다시 회전**. 이 분해를 통해 행렬의 숨겨진 구조(랭크, 조건수, 중요한 방향들)가 명확하게 드러난다. 현대 데이터 과학, 이미지 압축, 추천 시스템, 자연어 처리에서 SVD는 빠질 수 없는 핵심 도구다.

---

## SVD의 정의

### $A = U\Sigma V^T$

임의의 실수 행렬 $A \in \mathbb{R}^{m \times n}$에 대해, 다음과 같이 분해할 수 있다:

$$A = U\Sigma V^T$$

각 행렬의 역할:

| 행렬 | 크기 | 성질 | 의미 |
|------|------|------|------|
| $U$ | $m \times m$ | 직교행렬 ($U^TU = I$) | 좌특이벡터(left singular vectors) |
| $\Sigma$ | $m \times n$ | 대각 성분이 특이값 | 크기 정보 |
| $V$ | $n \times n$ | 직교행렬 ($V^TV = I$) | 우특이벡터(right singular vectors) |

$\Sigma$의 형태 ($r = \text{rank}(A)$):

$$\Sigma = \begin{pmatrix} \sigma_1 & & & & \\ & \sigma_2 & & & \\ & & \ddots & & \\ & & & \sigma_r & \\ & & & & 0 \end{pmatrix}$$

여기서 특이값들은 내림차순: $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$

---

## 특이값의 의미와 계산

### 특이값 $\sigma_i = \sqrt{\lambda_i(A^TA)}$

특이값 $\sigma_i$는 $A^TA$의 고유값의 양의 제곱근이다:

$$\sigma_i = \sqrt{\lambda_i(A^TA)}, \quad \lambda_1 \geq \lambda_2 \geq \cdots \geq 0$$

이것이 가능한 이유: $A^TA$는 항상 **양반정치(positive semidefinite)** 대칭행렬이므로, 모든 고유값이 $\geq 0$이다.

**증명 스케치:**

$A^TA$의 고유벡터를 $\vec{v}_i$라 하면 ($A^TA\vec{v}_i = \lambda_i \vec{v}_i$):

$$\sigma_i = \sqrt{\lambda_i}, \quad \vec{u}_i = \frac{1}{\sigma_i}A\vec{v}_i \quad (\sigma_i \neq 0 \text{인 경우})$$

이렇게 구성하면 $A = U\Sigma V^T$가 성립함을 확인할 수 있다.

---

## SVD 예시: 2×3 행렬

### 예시

$$A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}$$

**1단계: $A^TA$ 계산**

$$A^TA = \begin{pmatrix}3&2\\2&3\\2&-2\end{pmatrix}\begin{pmatrix}3&2&2\\2&3&-2\end{pmatrix} = \begin{pmatrix}13&12&2\\12&13&-2\\2&-2&8\end{pmatrix}$$

**2단계: $A^TA$의 고유값 (특이값의 제곱)**

특성방정식을 풀면: $\lambda_1 = 25$, $\lambda_2 = 9$, $\lambda_3 = 0$

특이값: $\sigma_1 = 5$, $\sigma_2 = 3$

**3단계: $V$ 구성 ($A^TA$의 고유벡터)**

$$\vec{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}, \quad \vec{v}_2 = \frac{1}{\sqrt{18}}\begin{pmatrix}1\\-1\\4\end{pmatrix}, \quad \vec{v}_3 = \frac{1}{3}\begin{pmatrix}2\\-2\\-1\end{pmatrix}$$

**4단계: $U$ 구성**

$$\vec{u}_1 = \frac{1}{\sigma_1}A\vec{v}_1 = \frac{1}{5} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}5\\5\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$$

$$\vec{u}_2 = \frac{1}{\sigma_2}A\vec{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$$

$$\Sigma = \begin{pmatrix}5&0&0\\0&3&0\end{pmatrix}$$

---

## SVD와 랭크

### 랭크 = 영이 아닌 특이값의 수

$$\text{rank}(A) = r = \#\{\sigma_i : \sigma_i > 0\}$$

이는 SVD의 가장 중요한 성질 중 하나다. 특이값들이 행렬의 "실질적인 차원수"를 알려준다.

### 네 가지 부분공간과 SVD

SVD는 선형대수의 핵심 정리인 네 가지 부분공간을 명확히 드러낸다:

| 부분공간 | SVD에서의 기저 |
|----------|----------------|
| 열공간 $C(A)$ | $U$의 첫 $r$개 열 $\vec{u}_1, \ldots, \vec{u}_r$ |
| 영공간 $N(A)$ | $V$의 마지막 $n-r$개 열 $\vec{v}_{r+1}, \ldots, \vec{v}_n$ |
| 행공간 $C(A^T)$ | $V$의 첫 $r$개 열 $\vec{v}_1, \ldots, \vec{v}_r$ |
| 좌영공간 $N(A^T)$ | $U$의 마지막 $m-r$개 열 $\vec{u}_{r+1}, \ldots, \vec{u}_m$ |

---

## SVD의 존재성

모든 실수 행렬에 SVD가 존재한다는 것은 선형대수학의 중요한 정리다. 이는 $A^TA$가 항상 대칭 양반정치이므로 스펙트럴 정리에 의해 직교 대각화가 가능하다는 사실로부터 증명된다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| SVD 정의 | $A = U\Sigma V^T$ |
| $U$ | $m \times m$ 직교행렬, 좌특이벡터 |
| $\Sigma$ | $m \times n$ 대각행렬, 특이값 $\sigma_1 \geq \cdots \geq 0$ |
| $V$ | $n \times n$ 직교행렬, 우특이벡터 |
| 특이값 공식 | $\sigma_i = \sqrt{\lambda_i(A^TA)}$ |
| 랭크 | $r$ = 영이 아닌 특이값의 수 |
| 존재성 | 모든 실수(복소수) 행렬에 SVD 존재 |
| 열공간 기저 | $U$의 첫 $r$개 열 |
| 영공간 기저 | $V$의 마지막 $n-r$개 열 |

> 다음 글에서는 **SVD의 기하학적 의미**를 살펴보며, 임의의 선형변환이 "회전-늘리기-회전"으로 분해되는 과정을 직관적으로 이해해 본다.
