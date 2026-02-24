"""7.2 Gram-Schmidt Process — Manim Animation

Rendering examples:
    manim -pqm scenes/07_orthogonality/7_2_gram_schmidt.py GramSchmidtProcess
"""

from manim import *


class GramSchmidtProcess(Scene):
    """Gram-Schmidt orthogonalization step by step"""

    def construct(self):
        # ── Title ──
        title = Text("Gram-Schmidt Process", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=6, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(RIGHT * 1.5 + DOWN * 0.3)
        self.play(Create(plane), run_time=1.0)

        # ── Original vectors a1, a2 ──
        a1 = Arrow(plane.c2p(0, 0), plane.c2p(3, 1), buff=0, color=GREY_B, stroke_width=4)
        a2 = Arrow(plane.c2p(0, 0), plane.c2p(1, 4), buff=0, color=GREY_B, stroke_width=4)
        a1_l = MathTex(r"\vec{a}_1", font_size=26, color=GREY_B).next_to(a1.get_end(), DR, buff=0.1)
        a2_l = MathTex(r"\vec{a}_2", font_size=26, color=GREY_B).next_to(a2.get_end(), UR, buff=0.1)
        self.play(GrowArrow(a1), Write(a1_l), GrowArrow(a2), Write(a2_l))
        self.wait(0.3)

        # ── Step 1: e1 = a1 / |a1| ──
        e1_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 1), buff=0, color=YELLOW, stroke_width=5)
        e1_label = MathTex(r"\vec{e}_1 = \frac{\vec{a}_1}{|\vec{a}_1|}", font_size=22, color=YELLOW)
        e1_label.to_corner(UL, buff=0.6).shift(DOWN * 0.8)
        self.play(GrowArrow(e1_arrow), Write(e1_label))
        self.wait(0.3)

        # ── Step 2: u2 = a2 - proj_e1(a2) ──
        proj_pt = plane.c2p(1.2, 0.4)  # projection of a2 onto e1 direction
        proj_arrow = Arrow(plane.c2p(0, 0), proj_pt, buff=0, color=RED, stroke_width=4)
        perp_line = DashedLine(plane.c2p(1, 4), proj_pt, color=WHITE, stroke_width=2)
        u2_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 4) - (proj_pt - plane.c2p(0, 0)), buff=0, color=GREEN, stroke_width=5)

        e2_label = MathTex(
            r"\vec{e}_2 = \frac{\vec{a}_2 - (\vec{a}_2\cdot\vec{e}_1)\vec{e}_1}{|\cdots|}",
            font_size=20, color=GREEN,
        )
        e2_label.next_to(e1_label, DOWN, buff=0.3)

        self.play(GrowArrow(proj_arrow), Create(perp_line))
        self.play(GrowArrow(u2_arrow), Write(e2_label))
        self.wait(0.5)

        # ── Right angle mark ──
        sq = Square(side_length=0.15, color=WHITE, stroke_width=2)
        sq.move_to(proj_pt + LEFT * 0.075 + UP * 0.075)
        self.play(Create(sq))

        # ── Result formula ──
        result = MathTex(
            r"\vec{e}_1 \cdot \vec{e}_2 = 0 \;\Rightarrow\; \text{orthonormal basis}",
            font_size=28, color=YELLOW,
        )
        result.to_edge(DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(2)
