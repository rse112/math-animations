# 4.4 변환의 합성

## 도입

"먼저 오른쪽으로 90° 회전한 다음, x 방향으로 2배 늘린다."
"먼저 x 방향으로 2배 늘린 다음, 오른쪽으로 90° 회전한다."

이 두 가지 순서의 결과가 같을까? — **다르다.**

행렬의 곱셈은 일반적으로 순서를 바꾸면 결과가 달라진다.
이것은 버그가 아니라 수학의 본질이다.
로봇 팔의 관절을 제어하거나, 3D 애니메이션의 키프레임을 설계할 때 변환 순서를 잘못 잡으면 완전히 다른 움직임이 나온다.
**변환의 합성(Composition)**을 이해하는 것은 선형대수의 핵심 역량이다.

---

## 합성의 정의

변환 $T_1 : \mathbb{R}^n \to \mathbb{R}^m$과 $T_2 : \mathbb{R}^m \to \mathbb{R}^k$가 있을 때,
두 변환을 연달아 적용하는 **합성 변환**은

$$T_2 \circ T_1 : \mathbb{R}^n \to \mathbb{R}^k, \quad (T_2 \circ T_1)(\vec{x}) = T_2(T_1(\vec{x}))$$

$T_1$을 **먼저** 적용하고, $T_2$를 **나중에** 적용한다.

---

## 행렬로 표현하기

$T_1(\vec{x}) = A\vec{x}$, $T_2(\vec{x}) = B\vec{x}$이면

$$(T_2 \circ T_1)(\vec{x}) = B(A\vec{x}) = (BA)\vec{x}$$

합성 변환의 행렬은 $BA$다 — **나중에 적용하는 변환의 행렬을 앞에** 쓴다.

이 표기 방식은 처음에는 헷갈리지만, 행렬-벡터 곱의 방향을 따라가면 자연스럽다.

---

## 순서의 중요성: $AB \neq BA$

**예시:** 45° 회전 행렬 $R$과 x축 반사 행렬 $M$을 정의하자.

$$R = R_{45°} = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \end{pmatrix}, \quad M = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**경우 1 — 먼저 회전, 나중에 반사:** 합성 행렬은 $MR$

$$MR = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \end{pmatrix} = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ -\tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \end{pmatrix}$$

**경우 2 — 먼저 반사, 나중에 회전:** 합성 행렬은 $RM$

$$RM = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{2}}{2} \\ \tfrac{\sqrt{2}}{2} & -\tfrac{\sqrt{2}}{2} \end{pmatrix}$$

$MR \neq RM$ — 순서가 다르면 결과가 다르다.

---

## 역변환 (Inverse Transformation)

선형변환 $T(\vec{x}) = A\vec{x}$의 **역변환** $T^{-1}$은

$$T^{-1}(\vec{y}) = A^{-1}\vec{y}$$

즉, 역변환의 행렬은 원래 행렬의 역행렬이다.

역변환이 존재하려면 $A$가 **정칙행렬(가역행렬)**이어야 한다: $\det(A) \neq 0$.

**합성의 역변환:**

$$(T_2 \circ T_1)^{-1} = T_1^{-1} \circ T_2^{-1}$$

행렬로는

$$(BA)^{-1} = A^{-1}B^{-1}$$

순서가 뒤집힌다 — 신발과 양말의 비유: 신을 때는 양말 먼저, 벗을 때는 신발 먼저.

---

## 예시: 45° 회전 후 x축 반사

벡터 $\vec{x} = (1, 0)^\top$에 45° 회전 후 x축 반사를 적용해보자.

**단계 1:** 45° 회전

$$R_{45°}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}\tfrac{\sqrt{2}}{2}\\\tfrac{\sqrt{2}}{2}\end{pmatrix}$$

**단계 2:** x축 반사

$$M_x\begin{pmatrix}\tfrac{\sqrt{2}}{2}\\\tfrac{\sqrt{2}}{2}\end{pmatrix} = \begin{pmatrix}\tfrac{\sqrt{2}}{2}\\-\tfrac{\sqrt{2}}{2}\end{pmatrix}$$

합성 행렬 $M_x R_{45°}$로 한 번에 계산해도 동일한 결과를 얻는다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 합성 변환 | $(T_2 \circ T_1)(\vec{x}) = T_2(T_1(\vec{x}))$ |
| 합성 행렬 | $T_1 \to A$, $T_2 \to B$이면 합성 행렬은 $BA$ |
| 순서 규칙 | 나중에 적용하는 변환의 행렬을 앞에 쓴다 |
| 비가환성 | 일반적으로 $AB \neq BA$ |
| 역변환 | $T^{-1}$의 행렬은 $A^{-1}$ (역행렬) |
| 합성의 역변환 | $(BA)^{-1} = A^{-1}B^{-1}$ (순서 역전) |
| 역변환 존재 조건 | $\det(A) \neq 0$ |

> 다음 글에서는 **벡터 공간 — 부분공간과 생성(Span)**을 알아본다.
