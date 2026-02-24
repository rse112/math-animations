"""4.2 2D Transformations — Manim Animation

Rendering examples:
    manim -pqm scenes/04_linear_transformations/4_2_2d_transformations.py Rotation2D
    manim -pqm scenes/04_linear_transformations/4_2_2d_transformations.py Reflection2D
    manim -pqm scenes/04_linear_transformations/4_2_2d_transformations.py Shear2D
"""

from manim import *
import numpy as np


class Rotation2D(Scene):
    """2D rotation by angle θ"""

    def construct(self):
        # ── Title ──
        title = Text("2D Rotation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Rotation matrix ──
        mat_label = MathTex(
            r"R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}",
            font_size=34,
        )
        mat_label.to_corner(UL, buff=0.8).shift(DOWN * 0.8)

        bg = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0.5},
        )
        grid = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GREEN_C, "stroke_width": 1.5, "stroke_opacity": 0.7},
            axis_config={"stroke_color": GREEN_B, "stroke_width": 2},
        )

        self.add(bg)
        self.play(Create(grid), Write(mat_label), run_time=1.0)
        self.wait(0.5)

        # ── Rotate 45° ──
        theta = np.pi / 4
        rot_matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]

        angle_label = MathTex(r"\theta = 45°", font_size=30, color=YELLOW)
        angle_label.to_corner(UR, buff=0.8)
        self.play(Write(angle_label))

        self.play(grid.animate.apply_matrix(rot_matrix), run_time=2)
        self.wait(2)


class Reflection2D(Scene):
    """Reflection about the x-axis"""

    def construct(self):
        # ── Title ──
        title = Text("Reflection", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        mat_label = MathTex(
            r"R_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}",
            font_size=36,
        )
        mat_label.to_corner(UL, buff=0.8).shift(DOWN * 0.8)

        bg = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0.5},
        )
        grid = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GREEN_C, "stroke_width": 1.5, "stroke_opacity": 0.7},
            axis_config={"stroke_color": GREEN_B, "stroke_width": 2},
        )

        self.add(bg)
        self.play(Create(grid), Write(mat_label), run_time=1.0)
        self.wait(0.5)

        # ── Reflect over x-axis ──
        self.play(grid.animate.apply_matrix([[1, 0], [0, -1]]), run_time=2)
        self.wait(2)


class Shear2D(Scene):
    """Horizontal shear transformation"""

    def construct(self):
        # ── Title ──
        title = Text("Shear Transformation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        mat_label = MathTex(
            r"S = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}",
            font_size=36,
        )
        mat_label.to_corner(UL, buff=0.8).shift(DOWN * 0.8)

        bg = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0.5},
        )
        grid = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GREEN_C, "stroke_width": 1.5, "stroke_opacity": 0.7},
            axis_config={"stroke_color": GREEN_B, "stroke_width": 2},
        )

        self.add(bg)
        self.play(Create(grid), Write(mat_label), run_time=1.0)
        self.wait(0.5)

        # k = 1.5
        k_label = MathTex(r"k = 1.5", font_size=30, color=YELLOW)
        k_label.to_corner(UR, buff=0.8)
        self.play(Write(k_label))

        self.play(grid.animate.apply_matrix([[1, 1.5], [0, 1]]), run_time=2)
        self.wait(2)
