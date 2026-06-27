"""9.5 Independence — Manim Animation

사건의 독립과 종속: 독립이면 P(A|B)=P(A), 즉 P(A∩B)=P(A)P(B).

Rendering examples:
    manim -pqm scenes/09_probability/9_5_independence.py Independence
"""

from manim import *


class Independence(Scene):
    """독립과 종속의 정의 비교"""

    def construct(self):
        title = Text("사건의 독립과 종속", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 독립의 정의
        indep = MathTex(r"P(A|B) = P(A)", font_size=38, color=GREEN)
        indep.next_to(title, DOWN, buff=0.6)
        indep_txt = Text("B가 일어나도 A의 확률이 그대로 → 독립", font_size=22)
        indep_txt.next_to(indep, DOWN, buff=0.3)
        self.play(Write(indep))
        self.play(Write(indep_txt))
        self.wait(0.8)

        # 동치 형태
        equiv = MathTex(
            r"\Longleftrightarrow \quad P(A \cap B) = P(A)\,P(B)",
            font_size=34,
            color=YELLOW,
        ).next_to(indep_txt, DOWN, buff=0.5)
        self.play(Write(equiv))
        self.wait(1)

        # 종속 대비
        dep = MathTex(r"P(A|B) \neq P(A)", font_size=32, color=RED)
        dep.next_to(equiv, DOWN, buff=0.7)
        dep_txt = Text("값이 달라지면 → 종속 (서로 영향을 줌)", font_size=22, color=RED)
        dep_txt.next_to(dep, DOWN, buff=0.25)
        self.play(Write(dep), Write(dep_txt))
        self.wait(2)
