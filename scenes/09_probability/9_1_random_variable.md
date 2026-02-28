# 9.1 확률변수 (Random Variable)

## 씬 목록

| 클래스명 | 설명 |
|---------|------|
| `RandomExperiment` | 주사위 던지기를 통한 확률실험 개념 시각화 |
| `SampleSpace` | 주사위 2번 던지기의 표본공간 (6x6 격자) |

## 핵심 개념

- **확률변수**: 확률 실험에서 얻은 결과를 수학적으로 표현한 변수
- **확률실험**: 동일한 조건에서 반복 가능하나 결과를 예측할 수 없는 실험
- **표본공간**: 가능한 모든 실현값의 집합

## 렌더링

```bash
manim -pqm scenes/09_probability/9_1_random_variable.py RandomExperiment
manim -pqm scenes/09_probability/9_1_random_variable.py SampleSpace
```
