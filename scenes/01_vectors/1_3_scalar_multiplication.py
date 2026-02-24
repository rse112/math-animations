"""1.3 Scalar Multiplication — Manim Animation

Rendering examples:
    manim -pqm scenes/01_vectors/1_3_scalar_multiplication.py ScalarMultiplication
    manim -pqm scenes/01_vectors/1_3_scalar_multiplication.py NegativeScalar
"""

from manim import *


class ScalarMultiplication(Scene):
    """Scaling a vector by positive scalars"""

    def construct(self):
        # ── Title ──
        title = Text("Scalar Multiplication", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 7, 1], y_range=[-1, 4, 1],
            x_length=8, y_length=4.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.4)
        self.play(Create(plane), run_time=1.5)

        # ── v = (2, 1) ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_end(), UR, buff=0.15)
        self.play(GrowArrow(v_arrow), Write(v_label))
        self.wait(0.5)

        # ── 2v ──
        v2_arrow = Arrow(plane.c2p(0, 0), plane.c2p(4, 2), buff=0, color=BLUE, stroke_width=5)
        v2_label = MathTex(r"2\vec{v}", font_size=32, color=BLUE)
        v2_label.next_to(v2_arrow.get_end(), UR, buff=0.15)
        self.play(GrowArrow(v2_arrow), Write(v2_label))
        self.wait(0.4)

        # ── 3v ──
        v3_arrow = Arrow(plane.c2p(0, 0), plane.c2p(6, 3), buff=0, color=PURPLE, stroke_width=5)
        v3_label = MathTex(r"3\vec{v}", font_size=32, color=PURPLE)
        v3_label.next_to(v3_arrow.get_end(), UR, buff=0.15)
        self.play(GrowArrow(v3_arrow), Write(v3_label))
        self.wait(0.4)

        # ── 0.5v ──
        vhalf_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 0.5), buff=0, color=GREEN, stroke_width=5)
        vhalf_label = MathTex(r"0.5\vec{v}", font_size=32, color=GREEN)
        vhalf_label.next_to(vhalf_arrow.get_end(), DR, buff=0.15)
        self.play(GrowArrow(vhalf_arrow), Write(vhalf_label))

        # ── Formula ──
        formula = MathTex(r"c\vec{v} = (cv_1,\ cv_2)", font_size=36)
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)


class NegativeScalar(Scene):
    """Negative scalar reverses direction"""

    def construct(self):
        # ── Title ──
        title = Text("Negative Scalar", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.3)
        self.play(Create(plane), run_time=1.5)

        # ── v ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_center(), UL, buff=0.15)
        self.play(GrowArrow(v_arrow), Write(v_label))
        self.wait(0.5)

        # ── -v ──
        neg_v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(-2, -1), buff=0, color=RED, stroke_width=5)
        neg_v_label = MathTex(r"-\vec{v}", font_size=32, color=RED)
        neg_v_label.next_to(neg_v_arrow.get_center(), DR, buff=0.15)
        self.play(GrowArrow(neg_v_arrow), Write(neg_v_label))
        self.wait(0.4)

        # ── -2v ──
        neg2v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(-4, -2), buff=0, color=PURPLE, stroke_width=5)
        neg2v_label = MathTex(r"-2\vec{v}", font_size=32, color=PURPLE)
        neg2v_label.next_to(neg2v_arrow.get_center(), DR, buff=0.15)
        self.play(GrowArrow(neg2v_arrow), Write(neg2v_label))
        self.wait(2)
