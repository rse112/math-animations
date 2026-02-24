# 5.4 영공간과 열공간

## 도입

연립방정식 $A\vec{x} = \vec{b}$를 풀 때 가장 먼저 드는 질문은 이것이다:
**"이 방정식의 해가 존재하는가? 그리고 존재한다면 몇 개인가?"**

해가 없는 경우, 해가 하나인 경우, 해가 무한히 많은 경우 — 이 세 가지 상황을 결정하는 것이 바로 행렬 $A$의 두 가지 핵심 부분공간이다.

- **열공간(Column Space):** $\vec{b}$가 "도달 가능한" 벡터인지 결정한다.
- **영공간(Null Space):** 해가 얼마나 많은지 결정한다.

이 두 공간과 그 차원의 관계를 정확히 이해하면 $A\vec{x} = \vec{b}$의 구조 전체가 투명하게 보인다.

---

## 영공간 (Null Space)

행렬 $A$의 **영공간(Null Space)**은

$$N(A) = \{\vec{x} \in \mathbb{R}^n \mid A\vec{x} = \vec{0}\}$$

즉, $A$에 곱했을 때 영벡터가 되는 모든 벡터의 집합이다.

**영공간은 부분공간이다.** 확인:
- $A\vec{0} = \vec{0}$이므로 $\vec{0} \in N(A)$.
- $A\vec{u} = \vec{0}$이고 $A\vec{v} = \vec{0}$이면 $A(\vec{u}+\vec{v}) = \vec{0}$. (덧셈 닫힘)
- $A\vec{u} = \vec{0}$이면 $A(c\vec{u}) = c\vec{0} = \vec{0}$. (스칼라 곱 닫힘)

영공간의 차원을 **영공간 차원(Nullity)**이라 부른다:

$$\text{nullity}(A) = \dim(N(A))$$

---

## 영공간 예시

$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$$

$A\vec{x} = \vec{0}$을 풀면:

$$x_1 + 2x_2 = 0 \implies x_1 = -2x_2$$

자유변수 $x_2 = t$로 두면:

$$\vec{x} = t\begin{pmatrix}-2\\1\end{pmatrix}, \quad t \in \mathbb{R}$$

$$N(A) = \text{span}\left\{\begin{pmatrix}-2\\1\end{pmatrix}\right\}, \quad \text{nullity}(A) = 1$$

영공간은 원점을 지나는 직선이다.

---

## 열공간 (Column Space)

행렬 $A$의 **열공간(Column Space)**은 $A$의 열벡터들의 Span이다.

$A$의 열벡터를 $\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_n$이라 하면

$$C(A) = \text{span}\{\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_n\}$$

열공간은 $A\vec{x}$로 **도달할 수 있는 모든 벡터**의 집합이다:

$$C(A) = \{A\vec{x} \mid \vec{x} \in \mathbb{R}^n\} = \text{(A의 치역, Range of A)}$$

**열공간은 부분공간이다** — Span은 항상 부분공간이기 때문이다.

열공간의 차원을 **랭크(Rank)**라 부른다:

$$\text{rank}(A) = \dim(C(A))$$

---

## 해의 존재성

**핵심 정리:** $A\vec{x} = \vec{b}$의 해가 존재한다 $\iff$ $\vec{b} \in C(A)$.

왜냐하면

$$A\vec{x} = x_1\vec{a}_1 + x_2\vec{a}_2 + \cdots + x_n\vec{a}_n$$

이므로 $A\vec{x}$는 열벡터들의 선형결합이다. 따라서 $\vec{b}$가 열공간에 속할 때만 해가 존재한다.

---

## 랭크-영공간 정리 (Rank-Nullity Theorem)

$A$가 $m \times n$ 행렬일 때

$$\text{rank}(A) + \text{nullity}(A) = n$$

이를 **랭크-영공간 정리** 또는 **차원 정리**라 부른다.

**직관적 의미:**
- $n$은 입력 공간 $\mathbb{R}^n$의 차원이다.
- $\text{rank}(A)$는 변환 후 "실제로 늘어나는" 차원의 수다.
- $\text{nullity}(A)$는 변환에서 "사라지는" 차원의 수다.
- 이 둘의 합은 항상 입력 차원 $n$이다.

---

## 예시로 정리 확인

$$A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

**열공간:** 1열 $(1,0,0)^\top$과 2열 $(0,1,0)^\top$은 선형 독립, 3열 = 1열 + 2열.

$$C(A) = \text{span}\left\{\begin{pmatrix}1\\0\\0\end{pmatrix}, \begin{pmatrix}0\\1\\0\end{pmatrix}\right\}, \quad \text{rank}(A) = 2$$

**영공간:** $A\vec{x} = \vec{0}$의 해 — $x_3 = t$ (자유변수), $x_1 = -t$, $x_2 = -t$.

$$N(A) = \text{span}\left\{\begin{pmatrix}-1\\-1\\1\end{pmatrix}\right\}, \quad \text{nullity}(A) = 1$$

**확인:** $\text{rank}(A) + \text{nullity}(A) = 2 + 1 = 3 = n$. 정리가 성립!

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 영공간 | $N(A) = \{\vec{x} : A\vec{x} = \vec{0}\}$, 부분공간 |
| 영공간 차원 | $\text{nullity}(A) = \dim(N(A))$ |
| 열공간 | $C(A) = \text{span}\{\text{열벡터들}\} = \{A\vec{x}\}$, 부분공간 |
| 랭크 | $\text{rank}(A) = \dim(C(A))$ |
| 해의 존재 조건 | $A\vec{x}=\vec{b}$ 해 존재 $\iff$ $\vec{b} \in C(A)$ |
| 랭크-영공간 정리 | $\text{rank}(A) + \text{nullity}(A) = n$ |
| 유일 해 조건 | $\text{nullity}(A) = 0$ (영공간 = $\{\vec{0}\}$) |

> 다음 글에서는 **고유값과 고유벡터 — 선형변환이 "방향을 바꾸지 않는" 특별한 벡터들**을 알아본다.
