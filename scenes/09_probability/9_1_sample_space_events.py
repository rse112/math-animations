"""9.1 Sample Space and Events — Manim Animation

표본공간과 사건. 주사위 예시로 P(A) = |A|/|Ω| 직관.

Rendering examples:
    manim -pqm scenes/09_probability/9_1_sample_space_events.py SampleSpaceEvents
"""

from manim import *


class SampleSpaceEvents(Scene):
    """표본공간 Ω와 사건 A (주사위 모델)"""

    def construct(self):
        title = Text("표본공간과 사건", font_size=36).to_edge(UP)
        self.play(Write(title))

        omega_label = MathTex(r"\Omega = \{1,2,3,4,5,6\}", font_size=34)
        omega_label.next_to(title, DOWN, buff=0.4)
        self.play(Write(omega_label))
        self.wait(0.3)

        # 6개 결과를 사각형으로
        squares = VGroup()
        for i in range(1, 7):
            sq = Square(side_length=1.0).set_stroke(WHITE, 2)
            num = MathTex(str(i), font_size=30).move_to(sq.get_center())
            squares.add(VGroup(sq, num))
        squares.arrange(RIGHT, buff=0.25).shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(s) for s in squares], lag_ratio=0.15))
        self.wait(0.5)

        # 사건 A = 짝수 {2,4,6}
        cap = Text("사건 A = '짝수가 나온다' = {2, 4, 6}", font_size=24, color=YELLOW)
        cap.to_edge(DOWN, buff=1.2)
        self.play(Write(cap))
        for idx in (1, 3, 5):  # 2, 4, 6 위치
            self.play(squares[idx][0].animate.set_fill(YELLOW, 0.5), run_time=0.3)
        self.wait(0.5)

        # P(A) = |A|/|Ω|
        formula = MathTex(
            r"P(A) = \frac{|A|}{|\Omega|} = \frac{3}{6} = \frac{1}{2}",
            font_size=34,
            color=GREEN,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(cap), Write(formula))
        self.wait(2)
