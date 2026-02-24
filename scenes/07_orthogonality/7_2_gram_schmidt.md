# 7.2 그람-슈미트 과정

## 도입

지저분하게 뒤엉킨 선반들을 정리하여 깔끔하게 직각으로 정렬한다고 상상해 보자. 기존 선반들의 위치를 최대한 살리면서 서로 완벽하게 수직인 배치로 재구성하는 과정이다. **그람-슈미트 과정(Gram-Schmidt process)**이 정확히 이 일을 한다. 선형독립이지만 서로 직교하지 않는 벡터들로부터, 같은 공간을 span하는 정규직교기저를 체계적으로 만들어낸다.

이 과정은 1800년대 수학자 요르겐 그람(Jørgen Gram)과 에르하르트 슈미트(Erhard Schmidt)가 개발했으며, 오늘날 수치해석, 신호 처리, 기계 학습의 핵심 알고리즘인 **QR 분해**의 토대가 된다. 정규직교기저를 사용하면 좌표 계산이 단순 내적으로 줄어들고, 수치적으로도 훨씬 안정적이다.

---

## 핵심 아이디어: 정사영 빼기

### 정사영 복습

벡터 $\vec{a}$를 단위벡터 $\vec{e}$ 방향으로 정사영(project)한 벡터는:

$$\text{proj}_{\vec{e}}\vec{a} = (\vec{a} \cdot \vec{e})\vec{e}$$

그람-슈미트의 아이디어: 새 벡터에서 이미 처리된 방향들의 성분을 모두 빼면 남은 부분이 그 방향들과 직교가 된다.

---

## 알고리즘

### 입력: 선형독립 벡터 $\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_k$

### 출력: 정규직교 벡터 $\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_k$

**1단계: 첫 번째 벡터 정규화**

$$\vec{e}_1 = \frac{\vec{a}_1}{\|\vec{a}_1\|}$$

**2단계: 두 번째 벡터에서 첫 번째 방향 제거 후 정규화**

$$\vec{u}_2 = \vec{a}_2 - (\vec{a}_2 \cdot \vec{e}_1)\vec{e}_1$$

$$\vec{e}_2 = \frac{\vec{u}_2}{\|\vec{u}_2\|}$$

**3단계: 세 번째 벡터에서 앞의 두 방향 제거 후 정규화**

$$\vec{u}_3 = \vec{a}_3 - (\vec{a}_3 \cdot \vec{e}_1)\vec{e}_1 - (\vec{a}_3 \cdot \vec{e}_2)\vec{e}_2$$

$$\vec{e}_3 = \frac{\vec{u}_3}{\|\vec{u}_3\|}$$

**일반 $k$단계:**

$$\vec{u}_k = \vec{a}_k - \sum_{j=1}^{k-1} (\vec{a}_k \cdot \vec{e}_j)\vec{e}_j$$

$$\vec{e}_k = \frac{\vec{u}_k}{\|\vec{u}_k\|}$$

---

## 구체적 예시

### 예시: 3차원 벡터 3개

$$\vec{a}_1 = \begin{pmatrix}1\\1\\0\end{pmatrix}, \quad \vec{a}_2 = \begin{pmatrix}1\\0\\1\end{pmatrix}, \quad \vec{a}_3 = \begin{pmatrix}0\\1\\1\end{pmatrix}$$

**1단계:**

$$\|\vec{a}_1\| = \sqrt{1+1+0} = \sqrt{2}$$

$$\vec{e}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}$$

**2단계:**

$$\vec{a}_2 \cdot \vec{e}_1 = \frac{1}{\sqrt{2}}(1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0) = \frac{1}{\sqrt{2}}$$

$$\vec{u}_2 = \begin{pmatrix}1\\0\\1\end{pmatrix} - \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}1\\0\\1\end{pmatrix} - \frac{1}{2}\begin{pmatrix}1\\1\\0\end{pmatrix} = \begin{pmatrix}1/2\\-1/2\\1\end{pmatrix}$$

$$\|\vec{u}_2\| = \sqrt{1/4 + 1/4 + 1} = \sqrt{3/2} = \frac{\sqrt{6}}{2}$$

$$\vec{e}_2 = \frac{2}{\sqrt{6}}\begin{pmatrix}1/2\\-1/2\\1\end{pmatrix} = \frac{1}{\sqrt{6}}\begin{pmatrix}1\\-1\\2\end{pmatrix}$$

**3단계:**

$$\vec{a}_3 \cdot \vec{e}_1 = \frac{1}{\sqrt{2}}(0+1+0) = \frac{1}{\sqrt{2}}, \quad \vec{a}_3 \cdot \vec{e}_2 = \frac{1}{\sqrt{6}}(0-1+2) = \frac{1}{\sqrt{6}}$$

$$\vec{u}_3 = \begin{pmatrix}0\\1\\1\end{pmatrix} - \frac{1}{2}\begin{pmatrix}1\\1\\0\end{pmatrix} - \frac{1}{6}\begin{pmatrix}1\\-1\\2\end{pmatrix} = \begin{pmatrix}-2/3\\2/3\\2/3\end{pmatrix}$$

$$\vec{e}_3 = \frac{1}{\sqrt{4/3}} \begin{pmatrix}-2/3\\2/3\\2/3\end{pmatrix} = \frac{1}{\sqrt{3}}\begin{pmatrix}-1\\1\\1\end{pmatrix}$$

---

## QR 분해

### $A = QR$

그람-슈미트 과정을 행렬 형태로 정리하면 **QR 분해**가 된다. 행렬 $A = [\vec{a}_1 \; \vec{a}_2 \; \cdots \; \vec{a}_n]$에 대해:

$$A = QR$$

- $Q = [\vec{e}_1 \; \vec{e}_2 \; \cdots \; \vec{e}_n]$: 정규직교 열벡터를 갖는 행렬
- $R$: 상삼각(upper triangular) 행렬, 성분은 $R_{ij} = \vec{a}_j \cdot \vec{e}_i$ ($i \leq j$)

$$R = \begin{pmatrix} \vec{a}_1\cdot\vec{e}_1 & \vec{a}_2\cdot\vec{e}_1 & \vec{a}_3\cdot\vec{e}_1 \\ 0 & \vec{a}_2\cdot\vec{e}_2 & \vec{a}_3\cdot\vec{e}_2 \\ 0 & 0 & \vec{a}_3\cdot\vec{e}_3 \end{pmatrix}$$

QR 분해는 선형 시스템 풀기, 최소제곱법, 고유값 계산 알고리즘(QR 알고리즘)에 광범위하게 사용된다.

---

## 수치 안정성

### 변형 그람-슈미트 (Modified Gram-Schmidt)

이론적으로 그람-슈미트 과정은 완벽하지만, 실제 컴퓨터에서는 부동소수점 오차가 누적되어 직교성이 깨질 수 있다. **변형 그람-슈미트(Modified Gram-Schmidt)**는 이 문제를 줄이기 위해, 각 단계마다 이미 정규화된 벡터들과 즉시 직교화하는 방식으로 수치 오차를 억제한다. 실제 수치 계산 라이브러리에서는 변형 그람-슈미트 또는 하우스홀더(Householder) 반사를 사용해 더욱 안정적인 QR 분해를 수행한다.

---

## 핵심 포인트 정리

| 개념 | 설명/공식 |
|------|-----------|
| 목적 | 선형독립 벡터 $\to$ 정규직교기저 |
| 정사영 | $\text{proj}_{\vec{e}}\vec{a} = (\vec{a}\cdot\vec{e})\vec{e}$ |
| 직교화 | $\vec{u}_k = \vec{a}_k - \sum_{j<k}(\vec{a}_k\cdot\vec{e}_j)\vec{e}_j$ |
| 정규화 | $\vec{e}_k = \vec{u}_k / \|\vec{u}_k\|$ |
| QR 분해 | $A = QR$ ($Q$: 정규직교, $R$: 상삼각) |
| $R$의 성분 | $R_{ij} = \vec{a}_j \cdot \vec{e}_i$ ($i \leq j$) |
| 수치 안정성 | 변형 그람-슈미트 또는 하우스홀더 반사 사용 |

> 다음 글에서는 **최소제곱법(Least Squares)**을 통해 해가 존재하지 않는 선형 시스템에서 최선의 근사해를 구하는 방법을 알아본다.
