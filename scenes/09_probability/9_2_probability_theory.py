"""9.2 Probability Theory — Manim Animation

합집합, 교집합, 확률의 공리, 덧셈정리에 대한 애니메이션

Rendering examples:
    manim -pqm scenes/09_probability/9_2_probability_theory.py UnionIntersection
    manim -pqm scenes/09_probability/9_2_probability_theory.py ProbabilityAxioms
    manim -pqm scenes/09_probability/9_2_probability_theory.py AdditionRule
"""

from manim import *


class UnionIntersection(Scene):
    """합집합과 교집합 시각화 (벤 다이어그램)"""

    def construct(self):
        title = Text("합집합과 교집합", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # 벤 다이어그램
        circle_a = Circle(radius=1.5, color=BLUE, fill_opacity=0.3)
        circle_a.shift(LEFT * 0.8)
        label_a = MathTex("A", font_size=36, color=BLUE)
        label_a.next_to(circle_a, UP + LEFT, buff=0.1)

        circle_b = Circle(radius=1.5, color=RED, fill_opacity=0.3)
        circle_b.shift(RIGHT * 0.8)
        label_b = MathTex("B", font_size=36, color=RED)
        label_b.next_to(circle_b, UP + RIGHT, buff=0.1)

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(0.5)

        # 합집합 강조
        union_label = MathTex(r"A \cup B", font_size=32, color=YELLOW)
        union_label.to_edge(DOWN, buff=1.5)
        union_desc = Text("합집합: 두 집합의 모든 원소", font_size=20)
        union_desc.next_to(union_label, DOWN, buff=0.2)

        union_highlight_a = circle_a.copy().set_fill(YELLOW, opacity=0.5).set_stroke(YELLOW)
        union_highlight_b = circle_b.copy().set_fill(YELLOW, opacity=0.5).set_stroke(YELLOW)

        self.play(
            FadeIn(union_highlight_a),
            FadeIn(union_highlight_b),
            Write(union_label),
            Write(union_desc),
        )
        self.wait(1.5)
        self.play(
            FadeOut(union_highlight_a),
            FadeOut(union_highlight_b),
            FadeOut(union_label),
            FadeOut(union_desc),
        )

        # 교집합 강조
        inter_label = MathTex(r"A \cap B", font_size=32, color=GREEN)
        inter_label.to_edge(DOWN, buff=1.5)
        inter_desc = Text("교집합: 공통 원소", font_size=20)
        inter_desc.next_to(inter_label, DOWN, buff=0.2)

        # 교집합 영역 (겹치는 부분)
        inter_region = Intersection(circle_a, circle_b, fill_opacity=0.6, fill_color=GREEN, stroke_color=GREEN)

        self.play(FadeIn(inter_region), Write(inter_label), Write(inter_desc))
        self.wait(2)


class ProbabilityAxioms(Scene):
    """확률의 3가지 공리"""

    def construct(self):
        title = Text("확률이 되기 위한 조건", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        axioms = VGroup()

        # 공리 1
        ax1_num = Text("1.", font_size=24, color=YELLOW)
        ax1_text = MathTex(r"P(\Omega) = 1", font_size=32)
        ax1_desc = Text("모든 사건의 확률 합 = 1", font_size=20, color=GRAY)
        ax1 = VGroup(ax1_num, ax1_text, ax1_desc).arrange(RIGHT, buff=0.3)
        axioms.add(ax1)

        # 공리 2
        ax2_num = Text("2.", font_size=24, color=YELLOW)
        ax2_text = MathTex(r"0 \leq P(A_n) \leq 1", font_size=32)
        ax2_desc = Text("모든 확률은 0 이상", font_size=20, color=GRAY)
        ax2 = VGroup(ax2_num, ax2_text, ax2_desc).arrange(RIGHT, buff=0.3)
        axioms.add(ax2)

        # 공리 3
        ax3_num = Text("3.", font_size=24, color=YELLOW)
        ax3_text = MathTex(
            r"P\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n)",
            font_size=28,
        )
        axioms.add(VGroup(ax3_num, ax3_text).arrange(RIGHT, buff=0.3))

        ax3_desc = Text("서로 배반인 사건들의 합", font_size=20, color=GRAY)

        axioms.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        axioms.center()

        for i, axiom in enumerate(axioms):
            self.play(FadeIn(axiom, shift=RIGHT), run_time=0.8)
            self.wait(0.8)

        ax3_desc.next_to(axioms[2], DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(ax3_desc))

        # 결론 박스
        conclusion = Text(
            "이 3가지가 정의되어야 확률변수라 할 수 있다",
            font_size=22,
            color=GREEN,
        )
        conclusion.to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(conclusion, color=GREEN, buff=0.15)
        self.play(Write(conclusion), Create(box))
        self.wait(2)


class AdditionRule(Scene):
    """확률의 덧셈정리: P(A∪B) = P(A) + P(B) - P(A∩B) (포함-배제)"""

    def construct(self):
        title = Text("확률의 덧셈정리", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 벤 다이어그램
        ca = Circle(radius=1.5, color=BLUE, fill_opacity=0.3).shift(LEFT * 0.8 + DOWN * 0.3)
        cb = Circle(radius=1.5, color=RED, fill_opacity=0.3).shift(RIGHT * 0.8 + DOWN * 0.3)
        la = MathTex("A", color=BLUE, font_size=34).next_to(ca, UL, buff=0.1)
        lb = MathTex("B", color=RED, font_size=34).next_to(cb, UR, buff=0.1)
        self.play(Create(ca), Create(cb), Write(la), Write(lb))
        self.wait(0.4)

        # ① P(A) 더하기
        step = Text("① P(A) 를 더한다", font_size=24, color=BLUE).to_edge(DOWN, buff=1.4)
        ha = ca.copy().set_fill(BLUE, opacity=0.55)
        self.play(FadeIn(ha), Write(step))
        self.wait(0.8)

        # ② P(B) 더하기 → 겹친 부분이 두 번 칠해짐
        step2 = Text("② P(B) 를 더한다 → 겹친 곳이 두 번!", font_size=24, color=RED).to_edge(DOWN, buff=1.4)
        hb = cb.copy().set_fill(RED, opacity=0.55)
        inter = Intersection(ca, cb, fill_opacity=0.9, fill_color=PURPLE, stroke_color=PURPLE)
        self.play(FadeOut(step), FadeIn(hb), Write(step2))
        self.play(FadeIn(inter))
        self.wait(1)

        # ③ 겹친 P(A∩B) 한 번 빼기
        step3 = Text("③ 겹친 P(A∩B) 를 한 번 뺀다", font_size=24, color=GREEN).to_edge(DOWN, buff=1.4)
        self.play(FadeOut(step2), Write(step3))
        self.play(inter.animate.set_fill(GREEN, opacity=0.5), FadeOut(ha), FadeOut(hb))
        self.wait(0.8)

        # 공식
        formula = MathTex(
            r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
            font_size=34,
            color=YELLOW,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(step3), Write(formula))
        self.wait(2)
