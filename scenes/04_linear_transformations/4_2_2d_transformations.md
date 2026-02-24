# 4.2 2D 선형변환

## 도입

스마트폰 사진 앱에서 이미지를 회전시키거나, 게임에서 캐릭터가 달리는 방향으로 스프라이트를 뒤집는 장면을 생각해보자.
영화의 특수효과, CAD 소프트웨어의 도면 편집, 지도 앱의 화면 회전 — 이 모든 것의 뒤에는 **2D 선형변환**이 있다.

2D 선형변환은 $2 \times 2$ 행렬 하나로 표현된다.
행렬의 네 숫자만 바꾸면 평면 위의 모든 점이 새로운 위치로 이동한다.
이번 글에서는 가장 자주 쓰이는 네 가지 변환을 살펴본다.

---

## 회전 변환 (Rotation)

각도 $\theta$만큼 **반시계 방향**으로 회전하는 변환의 행렬은

$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**유도:** 기저벡터 $\hat{e}_1 = (1, 0)^\top$을 $\theta$만큼 회전하면 $(\cos\theta, \sin\theta)^\top$,
$\hat{e}_2 = (0, 1)^\top$을 회전하면 $(-\sin\theta, \cos\theta)^\top$이 된다.
이 두 벡터를 열로 세우면 $R_\theta$가 나온다.

**예시:** $\theta = 90°$이면

$$R_{90°} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$

벡터 $(1, 0)^\top$은 $(0, 1)^\top$으로 이동한다. 정확히 90° 회전이다.

**회전 행렬의 성질:**
- $\det(R_\theta) = \cos^2\theta + \sin^2\theta = 1$ (넓이 보존)
- $R_\theta^{-1} = R_{-\theta} = R_\theta^\top$ (역변환은 반대 방향 회전)

---

## 반사 변환 (Reflection)

**x축에 대한 반사** — y 좌표의 부호를 뒤집는다:

$$M_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**y축에 대한 반사** — x 좌표의 부호를 뒤집는다:

$$M_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$$

**직선 $y = x$에 대한 반사** — x와 y 좌표를 서로 바꾼다:

$$M_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

반사 행렬의 특징: $\det(M) = -1$ (넓이는 보존하지만 방향이 뒤집힌다).

---

## 전단 변환 (Shear)

**수평 전단(Horizontal Shear)** — x 방향으로 y에 비례해 밀리는 변환:

$$S_H = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$

점 $(x, y)^\top$은 $(x + ky,\; y)^\top$으로 이동한다.
정사각형이 마름모처럼 기울어지는 변환이다.

**수직 전단(Vertical Shear)**:

$$S_V = \begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}$$

전단 변환의 특징: $\det(S) = 1$ (넓이는 변하지 않는다).

---

## 크기 조정 변환 (Scaling)

x 방향으로 $s_x$배, y 방향으로 $s_y$배 늘리거나 줄이는 변환:

$$S = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$$

**특수한 경우들:**

| 조건 | 의미 |
|------|------|
| $s_x = s_y = s$ | 균등 확대/축소 (isotropic scaling) |
| $s_x = -1, s_y = 1$ | y축 반사 (크기 조정의 특수 케이스) |
| $s_x = 1, s_y = -1$ | x축 반사 |
| $0 < s < 1$ | 축소 |
| $s > 1$ | 확대 |

$\det(S) = s_x \cdot s_y$ — 넓이가 $|s_x \cdot s_y|$배 변한다.

---

## 변환 요약 비교

| 변환 | 행렬 | 행렬식 | 넓이 변화 |
|------|------|--------|-----------|
| 회전 $\theta$ | $\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ | $1$ | 보존 |
| x축 반사 | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $-1$ | 보존 (방향 반전) |
| y축 반사 | $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ | $-1$ | 보존 (방향 반전) |
| 수평 전단 $k$ | $\begin{pmatrix}1&k\\0&1\end{pmatrix}$ | $1$ | 보존 |
| 크기 조정 | $\begin{pmatrix}s_x&0\\0&s_y\end{pmatrix}$ | $s_xs_y$ | $\|s_xs_y\|$배 |

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 회전 행렬 | $R_\theta = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$ |
| 회전의 역변환 | $R_\theta^{-1} = R_{-\theta} = R_\theta^\top$ |
| x축 반사 | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$, $\det = -1$ |
| y축 반사 | $\begin{pmatrix}-1&0\\0&1\end{pmatrix}$, $\det = -1$ |
| 수평 전단 | $\begin{pmatrix}1&k\\0&1\end{pmatrix}$, $\det = 1$ |
| 크기 조정 | $\begin{pmatrix}s_x&0\\0&s_y\end{pmatrix}$, $\det = s_xs_y$ |
| 행렬식과 넓이 | $|\det(A)|$는 넓이 변화 비율, 부호는 방향 |

> 다음 글에서는 **3D 선형변환 — x, y, z 축 회전과 동차좌표계**를 알아본다.
