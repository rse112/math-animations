# 9.2 확률이론 (Probability Theory)

## 씬 목록

| 클래스명 | 설명 |
|---------|------|
| `UnionIntersection` | 벤 다이어그램을 통한 합집합/교집합 시각화 |
| `ProbabilityAxioms` | 확률의 3가지 공리 |

## 핵심 개념

- **합집합** $A \cup B$: 두 집합의 모든 원소
- **교집합** $A \cap B$: 두 집합의 공통 원소
- **확률 공리**:
  1. $P(\Omega) = 1$
  2. $0 \leq P(A_n) \leq 1$
  3. $P(\bigcup_{n=1}^{\infty} A_n) = \sum_{n=1}^{\infty} P(A_n)$ (배반 사건)

## 렌더링

```bash
manim -pqm scenes/09_probability/9_2_probability_theory.py UnionIntersection
manim -pqm scenes/09_probability/9_2_probability_theory.py ProbabilityAxioms
```
