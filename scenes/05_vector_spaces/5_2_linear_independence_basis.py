"""5.2 Linear Independence and Basis — Manim Animation

Rendering examples:
    manim -pqm scenes/05_vector_spaces/5_2_linear_independence_basis.py LinearDependence
    manim -pqm scenes/05_vector_spaces/5_2_linear_independence_basis.py StandardBasis
"""

from manim import *


class LinearDependence(Scene):
    """Linearly dependent vs independent vectors"""

    def construct(self):
        # ── Title ──
        title = Text("Linear Independence", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Left: dependent ──
        left_label = Text("Dependent", font_size=28, color=RED)
        left_label.move_to(LEFT * 3.5 + UP * 2.2)

        plane_l = NumberPlane(
            x_range=[-1, 4, 1], y_range=[-1, 3, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
        )
        plane_l.move_to(LEFT * 3.5 + DOWN * 0.5)

        v1 = Arrow(plane_l.c2p(0, 0), plane_l.c2p(2, 1), buff=0, color=YELLOW, stroke_width=4)
        v2 = Arrow(plane_l.c2p(0, 0), plane_l.c2p(3, 1.5), buff=0, color=ORANGE, stroke_width=4)
        v1_l = MathTex(r"\vec{v}_1", font_size=24, color=YELLOW).next_to(v1.get_end(), UL, buff=0.1)
        v2_l = MathTex(r"\vec{v}_2 = 1.5\vec{v}_1", font_size=20, color=ORANGE).next_to(v2.get_end(), UR, buff=0.1)

        # ── Right: independent ──
        right_label = Text("Independent", font_size=28, color=GREEN)
        right_label.move_to(RIGHT * 3.5 + UP * 2.2)

        plane_r = NumberPlane(
            x_range=[-1, 4, 1], y_range=[-1, 3, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
        )
        plane_r.move_to(RIGHT * 3.5 + DOWN * 0.5)

        w1 = Arrow(plane_r.c2p(0, 0), plane_r.c2p(2, 0), buff=0, color=YELLOW, stroke_width=4)
        w2 = Arrow(plane_r.c2p(0, 0), plane_r.c2p(0, 2), buff=0, color=GREEN, stroke_width=4)
        w1_l = MathTex(r"\vec{w}_1", font_size=24, color=YELLOW).next_to(w1.get_end(), DOWN, buff=0.1)
        w2_l = MathTex(r"\vec{w}_2", font_size=24, color=GREEN).next_to(w2.get_end(), LEFT, buff=0.1)

        divider = DashedLine(UP * 3, DOWN * 3, color=GREY, dash_length=0.15)

        self.play(Create(divider))
        self.play(FadeIn(left_label), FadeIn(right_label))
        self.play(Create(plane_l), Create(plane_r), run_time=1.0)
        self.play(GrowArrow(v1), Write(v1_l), GrowArrow(w1), Write(w1_l))
        self.play(GrowArrow(v2), Write(v2_l), GrowArrow(w2), Write(w2_l))
        self.wait(2)


class StandardBasis(Scene):
    """Standard basis vectors in R^2 and R^3"""

    def construct(self):
        # ── Title ──
        title = Text("Standard Basis", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── R^2 basis ──
        r2_label = MathTex(r"\mathbb{R}^2", font_size=36, color=YELLOW)
        r2_label.move_to(LEFT * 3.5 + UP * 2)

        plane = NumberPlane(
            x_range=[-1, 3, 1], y_range=[-1, 3, 1],
            x_length=4, y_length=4,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
        )
        plane.move_to(LEFT * 3.5 + DOWN * 0.3)

        e1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=RED, stroke_width=5)
        e2 = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=GREEN, stroke_width=5)
        e1_l = MathTex(r"\vec{e}_1 = (1,0)", font_size=20, color=RED).next_to(e1.get_end(), DR, buff=0.1)
        e2_l = MathTex(r"\vec{e}_2 = (0,1)", font_size=20, color=GREEN).next_to(e2.get_end(), UR, buff=0.1)

        # ── R^3 basis (formula) ──
        r3_label = MathTex(r"\mathbb{R}^3", font_size=36, color=YELLOW)
        r3_label.move_to(RIGHT * 3 + UP * 2)

        r3_basis = MathTex(
            r"\vec{e}_1 = \begin{pmatrix}1\\0\\0\end{pmatrix},\;"
            r"\vec{e}_2 = \begin{pmatrix}0\\1\\0\end{pmatrix},\;"
            r"\vec{e}_3 = \begin{pmatrix}0\\0\\1\end{pmatrix}",
            font_size=26,
        )
        r3_basis.move_to(RIGHT * 3 + DOWN * 0.3)

        divider = DashedLine(UP * 3, DOWN * 3, color=GREY, dash_length=0.15)

        self.play(Create(divider))
        self.play(Write(r2_label), Write(r3_label))
        self.play(Create(plane))
        self.play(GrowArrow(e1), Write(e1_l))
        self.play(GrowArrow(e2), Write(e2_l))
        self.play(Write(r3_basis))
        self.wait(2)
