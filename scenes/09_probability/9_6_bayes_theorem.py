"""9.6 Bayes' Theorem — Manim Animation

베이즈 정리: 두 방향의 조건부확률을 연결해 P(A|B)를 뒤집는다.

Rendering examples:
    manim -pqm scenes/09_probability/9_6_bayes_theorem.py BayesTheorem
"""

from manim import *


class BayesTheorem(Scene):
    """베이즈 정리 유도 — 확률을 거꾸로 뒤집기"""

    def construct(self):
        title = Text("베이즈 정리 — 확률을 거꾸로 뒤집기", font_size=32).to_edge(UP)
        self.play(Write(title))

        # 같은 교집합을 두 방향으로
        eq1 = MathTex(r"P(A \cap B) = P(B)\,P(A|B)", font_size=32)
        eq2 = MathTex(r"P(A \cap B) = P(A)\,P(B|A)", font_size=32)
        grp = VGroup(eq1, eq2).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.7)
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(0.5)

        connect = Text("같은 교집합 확률 → 두 식을 연결", font_size=22, color=YELLOW)
        connect.next_to(grp, DOWN, buff=0.45)
        self.play(Write(connect))
        self.wait(0.6)

        # 베이즈 공식
        bayes = MathTex(
            r"P(A|B) = \frac{P(B|A)\,P(A)}{P(B)}",
            font_size=44,
            color=GREEN,
        ).next_to(connect, DOWN, buff=0.55)
        box = SurroundingRectangle(bayes, color=GREEN, buff=0.2)
        self.play(Write(bayes), Create(box))
        self.wait(2)
