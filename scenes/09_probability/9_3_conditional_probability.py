"""9.3 Conditional Probability — Manim Animation

조건부확률에 대한 애니메이션

씬 구성:
    ConditionalProbability  — 정의와 공식
    ShrinkingSampleSpace    — ⭐ 핵심: 표본공간이 B로 쪼그라드는 직관
    ConditionalExample      — 공학 전공 예시 (면적 모델)

Rendering examples:
    manim -pqm scenes/09_probability/9_3_conditional_probability.py ConditionalProbability
    manim -pqm scenes/09_probability/9_3_conditional_probability.py ShrinkingSampleSpace
    manim -pqm scenes/09_probability/9_3_conditional_probability.py ConditionalExample
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
            line_spacing=1.0,
        )
        definition.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # 공식
        formula = MathTex(
            r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
            font_size=48,
        )
        formula.center()
        box = SurroundingRectangle(formula, color=BLUE, buff=0.25)
        self.play(Write(formula), Create(box))
        self.wait(1)

        # 기호 읽는 법 (검색어 "조건부확률 기호" 대응)
        read_sym = MathTex(r"P(A|B)", font_size=36)
        read_arrow = MathTex(r"\longrightarrow", font_size=30)
        read_txt = Text("\"B가 주어졌을 때 A\"", font_size=24, color=YELLOW)
        read = VGroup(read_sym, read_arrow, read_txt).arrange(RIGHT, buff=0.3)
        read.next_to(formula, DOWN, buff=0.8)
        self.play(Write(read))
        self.wait(2)


class ShrinkingSampleSpace(Scene):
    """⭐ 핵심 직관: 전체 표본공간이 B로 쪼그라들며 P(A|B)가 드러난다."""

    def construct(self):
        title = Text("B가 일어나면, 세계가 B로 좁혀진다", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # 1) 전체 표본공간 Ω
        omega = Square(side_length=4.6).set_stroke(WHITE, 2).set_fill(GREY, 0.08)
        omega.shift(DOWN * 0.3)
        omega_label = MathTex(r"\Omega", font_size=34).next_to(omega, UL, buff=0.1)
        omega_cap = Text("전체 표본공간", font_size=18, color=GREY_B)
        omega_cap.next_to(omega_label, RIGHT, buff=0.2)
        self.play(Create(omega), Write(omega_label), FadeIn(omega_cap))
        self.wait(0.4)

        # 2) 사건 A, B (겹치게 배치)
        cb = Circle(radius=1.5).set_stroke(RED, 3).set_fill(RED, 0.22)
        cb.move_to(omega.get_center() + RIGHT * 0.75)
        ca = Circle(radius=1.25).set_stroke(BLUE, 3).set_fill(BLUE, 0.22)
        ca.move_to(omega.get_center() + LEFT * 0.55 + DOWN * 0.15)

        lb = MathTex("B", color=RED, font_size=34).move_to(cb.get_center() + RIGHT * 1.0 + UP * 0.95)
        la = MathTex("A", color=BLUE, font_size=34).move_to(ca.get_center() + LEFT * 0.85 + DOWN * 0.55)

        self.play(Create(cb), Write(lb))
        self.play(Create(ca), Write(la))

        # 교집합 A∩B
        inter = Intersection(ca, cb).set_stroke(GREEN, 2).set_fill(GREEN, 0.75)
        self.play(FadeIn(inter))
        self.wait(0.5)

        # 3) "B가 일어났다" → B 밖의 세계가 사라짐
        given = Text("B가 일어났다", color=YELLOW, font_size=30).next_to(omega, DOWN, buff=0.35)
        self.play(Write(given))
        self.wait(0.4)
        self.play(
            FadeOut(omega), FadeOut(omega_label), FadeOut(omega_cap),
            ca.animate.set_opacity(0.0),        # A 원의 테두리/채움 제거 (A∩B만 남김)
            FadeOut(la), FadeOut(given),
        )
        self.wait(0.3)

        # 4) B가 새로운 전체 우주로 확대
        self.play(FadeOut(lb))
        shapes = VGroup(cb, inter)
        self.play(shapes.animate.scale(1.7).move_to(ORIGIN + DOWN * 0.2), run_time=1.6)

        new_cap = Text("이제 B가 새로운 '전체'", font_size=22, color=RED)
        new_cap.next_to(cb, UP, buff=0.3)
        ab_cap = MathTex(r"A\cap B", color=WHITE, font_size=28).move_to(inter.get_center())
        self.play(Write(new_cap), Write(ab_cap))
        self.wait(0.6)

        # 5) 비율 = 조건부확률 (수식은 순수 LaTeX, 한글은 Text로 분리)
        ratio = MathTex(
            r"P(A|B) = \frac{A \cap B}{B} = \frac{P(A \cap B)}{P(B)}",
            font_size=34,
            color=YELLOW,
        )
        ratio.to_edge(DOWN, buff=0.5)
        self.play(Write(ratio))
        self.wait(2)


class ConditionalExample(Scene):
    """조건부확률 예시: 대학교 공학 전공 (면적 모델)"""

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
        male_eng = Rectangle(width=4.8, height=0.9, color=BLUE, fill_opacity=0.6)
        male_eng.align_to(male_rect, LEFT + DOWN)

        female_eng = Rectangle(width=3.2, height=0.6, color=PINK, fill_opacity=0.6)
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

        # 계산: P(남성 | 공학)  — MathTex엔 기호(M,E)만, 한글은 Text 범례로
        legend = Text("M = 남성,  E = 공학", font_size=18, color=GREY_B)
        legend.to_edge(DOWN, buff=1.5)
        calc = MathTex(
            r"P(M|E) = \frac{0.6 \times 0.3}{0.6\times0.3 + 0.4\times0.2} \approx 0.69",
            font_size=28,
            color=YELLOW,
        )
        calc.next_to(legend, DOWN, buff=0.25)
        self.play(FadeIn(legend), Write(calc))
        self.wait(0.5)

        result = Text("약 69%", font_size=36, color=GREEN)
        result.next_to(calc, DOWN, buff=0.3)
        result_box = SurroundingRectangle(result, color=GREEN, buff=0.1)
        self.play(Write(result), Create(result_box))
        self.wait(2)
