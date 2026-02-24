# 4.3 3D 선형변환

## 도입

3D 게임에서 캐릭터가 머리를 돌리거나, 애니메이션 영화에서 로봇 팔이 관절을 꺾는 장면을 생각해보자.
드론이 공중에서 기울어지고, 우주선이 세 방향으로 자세를 바꾸는 것 — 이 모든 동작은 **3D 선형변환**으로 표현된다.

3D 공간에서는 회전축이 세 개(x, y, z)이기 때문에 변환이 훨씬 풍부해진다.
그리고 이동(Translation)을 선형변환으로 처리하려면 **동차좌표계**라는 도구가 필요하다.
이번 글에서 3D 변환의 세계를 탐험해보자.

---

## x축 회전

x축을 고정하고 yz 평면 위에서 $\theta$만큼 반시계 회전하는 변환:

$$R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}$$

x 좌표는 변하지 않고, y와 z 좌표가 2D 회전처럼 섞인다.
항공 용어로는 **롤(Roll)** — 비행기 날개를 기울이는 동작이다.

---

## y축 회전

y축을 고정하고 xz 평면 위에서 $\theta$만큼 회전하는 변환:

$$R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}$$

부호에 주의: $R_x$, $R_z$와 달리 $\sin\theta$의 위치가 다르다.
이는 오른손 좌표계에서 y축의 방향 때문이다.
항공 용어로는 **피치(Pitch)** — 비행기 기수를 올리거나 내리는 동작이다.

---

## z축 회전

z축을 고정하고 xy 평면 위에서 $\theta$만큼 반시계 회전하는 변환:

$$R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

xy 블록이 2D 회전 행렬과 동일하다. z 좌표는 변하지 않는다.
항공 용어로는 **요(Yaw)** — 비행기가 좌우로 방향을 바꾸는 동작이다.

---

## 3D 크기 조정 (Scaling)

세 축 방향으로 각각 $s_x$, $s_y$, $s_z$배 확대/축소:

$$S = \begin{pmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{pmatrix} = \text{diag}(s_x,\, s_y,\, s_z)$$

부피 변화율은 $|\det(S)| = |s_x \cdot s_y \cdot s_z|$이다.

---

## 세 회전 비교

| 회전축 | 행렬 크기 | 고정 좌표 | 항공 명칭 |
|--------|-----------|-----------|-----------|
| x축 $R_x(\theta)$ | $3\times3$ | x 불변 | Roll |
| y축 $R_y(\theta)$ | $3\times3$ | y 불변 | Pitch |
| z축 $R_z(\theta)$ | $3\times3$ | z 불변 | Yaw |

세 회전 행렬 모두 $\det = 1$이고 $R^{-1} = R^\top$이다 (직교 행렬).

---

## 동차좌표계 (Homogeneous Coordinates)

선형변환 $T(\vec{x}) = A\vec{x}$는 원점을 고정한다.
따라서 **이동(Translation)** $\vec{x} \mapsto \vec{x} + \vec{t}$는 선형변환이 아니다.

이 문제를 해결하기 위해 **동차좌표계**를 사용한다.
3D 점 $(x, y, z)$를 4D 벡터로 확장한다:

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} \longrightarrow \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix}$$

이동 변환을 $4 \times 4$ 행렬로 표현하면:

$$T_{\vec{t}} = \begin{pmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

이제 회전, 크기 조정, 이동을 모두 $4 \times 4$ 행렬의 곱으로 통일할 수 있다.
컴퓨터 그래픽스(OpenGL, DirectX)에서 표준으로 사용하는 방식이다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| x축 회전 | $R_x(\theta)$: yz 평면 회전, Roll |
| y축 회전 | $R_y(\theta)$: xz 평면 회전, Pitch (부호 주의) |
| z축 회전 | $R_z(\theta)$: xy 평면 회전, Yaw |
| 3D 크기 조정 | $\text{diag}(s_x, s_y, s_z)$, 부피 변화 $= \|s_xs_ys_z\|$ |
| 직교 행렬 | 회전 행렬은 $R^{-1} = R^\top$, $\det = 1$ |
| 동차좌표계 | 3D 점을 4D로 확장, 이동을 행렬 곱으로 표현 |
| 4×4 이동 행렬 | 마지막 열에 이동 벡터 $\vec{t}$를 배치 |

> 다음 글에서는 **변환의 합성 — 두 변환을 연달아 적용할 때 순서가 왜 중요한지**를 알아본다.
