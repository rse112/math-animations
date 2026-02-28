"""9.3 Conditional Probability — Manim Animation

조건부확률에 대한 애니메이션

Rendering examples:
    manim -pqm scenes/09_probability/9_3_conditional_probability.py ConditionalProbability
    manim -pqm scenes/09_probability/9_3_conditional_probability.py BayesExample
"""

from manim import *


class ConditionalProbability(Scene):
    """조건부확률 정의와 공식"""

    def construct(self):
        title = Text("조건부 확률 (Conditional Probability)", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 정의
        definition = Text(
            "사건 B가 일어난 조건에서\n사건 A가 일어날 확률",
            font_size=24,
            color=YELLOW,
        )
        definition.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # 공식
        formula = MathTex(
            r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
            font_size=40,
        )
        formula.center()
        box = SurroundingRectangle(formula, color=BLUE, buff=0.2)
        self.play(Write(formula), Create(box))
        self.wait(1)

        # 벤 다이어그램으로 시각화
        self.play(
            FadeOut(definition),
            formula.animate.scale(0.7).to_edge(LEFT).shift(UP * 1.5),
            FadeOut(box),
        )

        circle_b = Circle(radius=1.5, color=RED, fill_opacity=0.2)
        circle_b.shift(RIGHT * 1.5)
        label_b = MathTex("B", font_size=30, color=RED)
        label_b.next_to(circle_b, UP + RIGHT, buff=0.1)

        circle_a = Circle(radius=1.2, color=BLUE, fill_opacity=0.2)
        circle_a.shift(RIGHT * 0.5)
        label_a = MathTex("A", font_size=30, color=BLUE)
        label_a.next_to(circle_a, UP + LEFT, buff=0.1)

        self.play(Create(circle_b), Write(label_b))
        self.play(Create(circle_a), Write(label_a))

        # B가 일어났을 때 (B 전체 강조)
        b_highlight = circle_b.copy().set_fill(RED, opacity=0.4)
        b_text = MathTex(r"P(B)", font_size=24, color=RED)
        b_text.next_to(circle_b, DOWN, buff=0.3)
        self.play(FadeIn(b_highlight), Write(b_text))
        self.wait(0.5)

        # A∩B 강조
        inter = Intersection(
            circle_a, circle_b, fill_opacity=0.6, fill_color=GREEN, stroke_color=GREEN
        )
        ab_text = MathTex(r"P(A \cap B)", font_size=24, color=GREEN)
        ab_text.next_to(inter, DOWN, buff=0.5)
        self.play(FadeOut(b_highlight), FadeIn(inter), Write(ab_text))
        self.wait(0.5)

        # 비율 설명
        ratio_text = MathTex(
            r"P(A|B) = \frac{\text{초록 영역}}{\text{빨간 원 전체}}",
            font_size=24,
            color=YELLOW,
        )
        ratio_text.to_edge(DOWN, buff=0.5)
        self.play(Write(ratio_text))
        self.wait(2)


class BayesExample(Scene):
    """조건부확률 예시: 대학교 공학 전공"""

    def construct(self):
        title = Text("예시: 공학 전공 학생", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # 문제 설정 시각화
        total = Rectangle(width=8, height=3, color=WHITE)
        total.center().shift(UP * 0.3)

        # 남성 60%, 여성 40%
        male_rect = Rectangle(width=4.8, height=3, color=BLUE, fill_opacity=0.3)
        male_rect.align_to(total, LEFT)
        male_rect.align_to(total, UP)

        female_rect = Rectangle(width=3.2, height=3, color=PINK, fill_opacity=0.3)
        female_rect.align_to(total, RIGHT)
        female_rect.align_to(total, UP)

        male_label = Text("남성 60%", font_size=20, color=BLUE)
        male_label.move_to(male_rect.get_top()).shift(DOWN * 0.3)

        female_label = Text("여성 40%", font_size=20, color=PINK)
        female_label.move_to(female_rect.get_top()).shift(DOWN * 0.3)

        self.play(
            Create(total),
            FadeIn(male_rect),
            FadeIn(female_rect),
            Write(male_label),
            Write(female_label),
        )
        self.wait(0.5)

        # 공학 전공 부분 강조
        male_eng = Rectangle(
            width=4.8, height=0.9, color=BLUE, fill_opacity=0.6
        )
        male_eng.align_to(male_rect, LEFT + DOWN)

        female_eng = Rectangle(
            width=3.2, height=0.6, color=PINK, fill_opacity=0.6
        )
        female_eng.align_to(female_rect, RIGHT + DOWN)

        male_eng_label = Text("공학 30%", font_size=16)
        male_eng_label.move_to(male_eng)

        female_eng_label = Text("공학 20%", font_size=16)
        female_eng_label.move_to(female_eng)

        self.play(
            FadeIn(male_eng),
            FadeIn(female_eng),
            Write(male_eng_label),
            Write(female_eng_label),
        )
        self.wait(1)

        # 계산
        calc = MathTex(
            r"P(\text{남성}|\text{공학}) = \frac{0.6 \times 0.3}{0.26} \approx 0.69",
            font_size=28,
            color=YELLOW,
        )
        calc.to_edge(DOWN, buff=0.8)
        self.play(Write(calc))
        self.wait(0.5)

        result = Text("약 69%", font_size=36, color=GREEN)
        result.next_to(calc, DOWN, buff=0.3)
        result_box = SurroundingRectangle(result, color=GREEN, buff=0.1)
        self.play(Write(result), Create(result_box))
        self.wait(2)
