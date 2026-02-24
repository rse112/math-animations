"""4.1 Linear Transformation — Manim Animation

Rendering examples:
    manim -pqm scenes/04_linear_transformations/4_1_linear_transformation.py LinearTransformGrid
    manim -pqm scenes/04_linear_transformations/4_1_linear_transformation.py LinearTransformBasis
"""

from manim import *


class LinearTransformGrid(Scene):
    """Linear transformation as grid deformation"""

    def construct(self):
        # ── Title ──
        title = Text("Linear Transformation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Matrix label ──
        mat_label = MathTex(
            r"A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}",
            font_size=34,
        )
        mat_label.to_corner(UL, buff=0.8)
        mat_label.shift(DOWN * 0.8)

        # ── Background grid (fixed) ──
        bg = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0.5},
        )

        # ── Moving grid ──
        grid = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GREEN_C, "stroke_width": 1.5, "stroke_opacity": 0.7},
            axis_config={"stroke_color": GREEN_B, "stroke_width": 2},
        )

        self.add(bg)
        self.play(Create(grid), run_time=1.0)
        self.play(Write(mat_label))
        self.wait(0.5)

        # ── Apply matrix ──
        matrix = [[2, 1], [0, 2]]
        self.play(grid.animate.apply_matrix(matrix), run_time=2)
        self.wait(2)


class LinearTransformBasis(Scene):
    """How transformation acts on basis vectors"""

    def construct(self):
        # ── Title ──
        title = Text("Basis Vector Transformation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-2, 5, 1], y_range=[-2, 4, 1],
            x_length=7, y_length=5.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.2)
        self.play(Create(plane), run_time=1.0)

        # ── Original basis vectors ──
        e1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=RED, stroke_width=5)
        e2 = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=GREEN, stroke_width=5)
        e1_label = MathTex(r"\vec{e}_1", font_size=28, color=RED)
        e1_label.next_to(e1.get_end(), DOWN, buff=0.15)
        e2_label = MathTex(r"\vec{e}_2", font_size=28, color=GREEN)
        e2_label.next_to(e2.get_end(), LEFT, buff=0.15)

        self.play(GrowArrow(e1), Write(e1_label))
        self.play(GrowArrow(e2), Write(e2_label))
        self.wait(0.5)

        # ── Matrix: A = [[2,1],[0,2]] ──
        mat_label = MathTex(
            r"A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}",
            font_size=32,
        )
        mat_label.to_corner(UR, buff=0.8)
        self.play(Write(mat_label))
        self.wait(0.3)

        # ── Transformed basis vectors ──
        Ae1 = Arrow(plane.c2p(0, 0), plane.c2p(2, 0), buff=0, color=RED_B, stroke_width=5)
        Ae2 = Arrow(plane.c2p(0, 0), plane.c2p(1, 2), buff=0, color=GREEN_B, stroke_width=5)
        Ae1_label = MathTex(r"A\vec{e}_1 = \begin{pmatrix}2\\0\end{pmatrix}", font_size=24, color=RED_B)
        Ae1_label.next_to(Ae1.get_end(), DOWN, buff=0.15)
        Ae2_label = MathTex(r"A\vec{e}_2 = \begin{pmatrix}1\\2\end{pmatrix}", font_size=24, color=GREEN_B)
        Ae2_label.next_to(Ae2.get_end(), UR, buff=0.1)

        self.play(Transform(e1.copy(), Ae1), Write(Ae1_label))
        self.play(GrowArrow(Ae1))
        self.play(Transform(e2.copy(), Ae2), Write(Ae2_label))
        self.play(GrowArrow(Ae2))
        self.wait(2)
