# Linear Algebra Animations with Manim

ManimCE를 활용한 선형대수 시각화 프로젝트

## 목차

### 1. 벡터 (Vectors)
- 1.1 벡터란 무엇인가
- 1.2 벡터의 덧셈과 뺄셈
- 1.3 스칼라 곱
- 1.4 벡터의 크기와 단위벡터

### 2. 내적과 외적 (Dot & Cross Product)
- 2.1 내적의 정의와 기하학적 의미
- 2.2 정사영 (Projection)
- 2.3 외적의 정의와 기하학적 의미

### 3. 행렬 (Matrices)
- 3.1 행렬이란 무엇인가
- 3.2 행렬의 연산 (덧셈, 곱셈)
- 3.3 역행렬과 행렬식 (Inverse & Determinant)

### 4. 선형 변환 (Linear Transformations)
- 4.1 선형 변환의 개념
- 4.2 2D 변환 — 회전, 반사, 전단, 스케일링
- 4.3 3D 변환
- 4.4 변환의 합성

### 5. 벡터 공간 (Vector Spaces)
- 5.1 부분공간과 생성 (Span)
- 5.2 선형 독립과 기저 (Basis)
- 5.3 차원 (Dimension)
- 5.4 영공간과 열공간 (Null Space & Column Space)

### 6. 고유값과 고유벡터 (Eigenvalues & Eigenvectors)
- 6.1 고유값과 고유벡터의 정의
- 6.2 특성 방정식
- 6.3 대각화 (Diagonalization)
- 6.4 고유값 분해의 기하학적 의미

### 7. 직교성 (Orthogonality)
- 7.1 직교 벡터와 직교 행렬
- 7.2 그람-슈미트 과정 (Gram-Schmidt Process)
- 7.3 최소제곱법 (Least Squares)

### 8. 특이값 분해 (SVD)
- 8.1 SVD의 정의
- 8.2 SVD의 기하학적 의미
- 8.3 SVD의 응용 (차원 축소, 이미지 압축)

## 실행 방법

```bash
# 가상환경 활성화
source venv/bin/activate

# 특정 씬 렌더링
manim -pql scenes/vectors.py VectorAddition
```

## 환경 설정

- Python 3.10+
- ManimCE 0.19.1
- macOS (Apple Silicon)
