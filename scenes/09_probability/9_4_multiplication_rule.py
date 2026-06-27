"""9.4 Multiplication Rule — Manim Animation

확률의 곱셈정리: P(A∩B) = P(B)·P(A|B). 확률 트리로 경로 곱 직관.

Rendering examples:
    manim -pqm scenes/09_probability/9_4_multiplication_rule.py MultiplicationRule
"""

from manim import *


class MultiplicationRule(Scene):
    """확률 트리로 보는 곱셈정리"""

    def construct(self):
        title = Text("확률의 곱셈정리", font_size=36).to_edge(UP)
        self.play(Write(title))

        formula = MathTex(
            r"P(A \cap B) = P(B)\,P(A|B)", font_size=36, color=YELLOW
        ).to_edge(DOWN, buff=0.5)

        # 트리 노드
        root = Dot(LEFT * 4.5, radius=0.06)
        b = Dot(LEFT * 1.5 + UP * 1.3, radius=0.06)
        bc = Dot(LEFT * 1.5 + DOWN * 1.3, radius=0.06)
        a = Dot(RIGHT * 2.2 + UP * 2.0, radius=0.06)
        ac = Dot(RIGHT * 2.2 + UP * 0.6, radius=0.06)

        l1 = Line(root.get_center(), b.get_center())
        l2 = Line(root.get_center(), bc.get_center())
        l3 = Line(b.get_center(), a.get_center())
        l4 = Line(b.get_center(), ac.get_center())

        pb = MathTex(r"P(B)", font_size=26).next_to(l1, UP, buff=0.1)
        pbc = MathTex(r"P(B^c)", font_size=26).next_to(l2, DOWN, buff=0.1)
        pab = MathTex(r"P(A|B)", font_size=26, color=GREEN).next_to(l3, UP, buff=0.1)
        b_lbl = MathTex("B", font_size=28, color=RED).next_to(b, LEFT, buff=0.15)
        a_lbl = MathTex("A", font_size=28, color=BLUE).next_to(a, RIGHT, buff=0.15)

        self.play(
            Create(l1), Create(l2), Write(pb), Write(pbc),
            FadeIn(b), FadeIn(bc), Write(b_lbl),
        )
        self.play(
            Create(l3), Create(l4), Write(pab),
            FadeIn(a), FadeIn(ac), Write(a_lbl),
        )
        self.wait(0.5)

        # 경로 강조 (root → B → A)
        path = VGroup(
            l1.copy().set_color(YELLOW).set_stroke(width=7),
            l3.copy().set_color(YELLOW).set_stroke(width=7),
        )
        cap = Text("경로의 확률 = 가지 확률의 곱", font_size=22, color=YELLOW).to_edge(DOWN, buff=1.5)
        self.play(Create(path), Write(cap))
        self.wait(1)
        self.play(FadeOut(cap), Write(formula))
        self.wait(2)
