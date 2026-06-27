# 9.3 조건부확률 (Conditional Probability)

## 씬 목록

| 클래스명 | 설명 |
|---------|------|
| `ConditionalProbability` | 조건부확률 정의·공식·기호 읽는 법 |
| `ShrinkingSampleSpace` | ⭐ **핵심**: 전체 표본공간 Ω가 B로 쪼그라들며 $P(A\|B)$가 드러나는 직관 |
| `ConditionalExample` | 공학 전공 예시 (면적 모델로 조건부확률 계산) |

## 핵심 개념

- **조건부확률**: $P(A|B) = \dfrac{P(A \cap B)}{P(B)}$
- B가 일어났을 때 A가 일어날 확률
- **직관**: B가 주어지면 전체 세계가 B로 "좁혀지고", 그 안에서 A가 차지하는 비율이 $P(A|B)$

## 렌더링

```bash
manim -pqm scenes/09_probability/9_3_conditional_probability.py ConditionalProbability
manim -pqm scenes/09_probability/9_3_conditional_probability.py ShrinkingSampleSpace
manim -pqm scenes/09_probability/9_3_conditional_probability.py ConditionalExample
```

> 고화질(블로그용 GIF)은 `-pqh`로 렌더 후 GIF 추출.
