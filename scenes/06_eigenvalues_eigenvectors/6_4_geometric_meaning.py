"""6.4 Geometric Meaning of Eigendecomposition — Manim Animation

Rendering examples:
    manim -pqm scenes/06_eigenvalues_eigenvectors/6_4_geometric_meaning.py EigendecompGeometric
"""

from manim import *
import numpy as np


class EigendecompGeometric(Scene):
    """Eigendecomposition as stretch along eigenvector axes"""

    def construct(self):
        # ── Title ──
        title = Text("Eigendecomposition — Geometric View", font_size=38)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"A = P D P^{-1}",
            font_size=44,
        )
        formula.move_to(UP * 1.8)
        self.play(Write(formula))
        self.wait(0.3)

        # ── Step-by-step interpretation ──
        steps = VGroup(
            MathTex(r"1.\; P^{-1} : \text{rotate to eigenvector basis}", font_size=28, color=BLUE_B),
            MathTex(r"2.\; D : \text{scale along each eigenvector axis } (\times\lambda_i)", font_size=28, color=GREEN),
            MathTex(r"3.\; P : \text{rotate back to standard basis}", font_size=28, color=RED_B),
        ).arrange(DOWN, buff=0.45)
        steps.move_to(DOWN * 0.2)
        for s in steps:
            self.play(Write(s))
            self.wait(0.3)

        # ── Grid transform ──
        bg = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.2},
            axis_config={"stroke_opacity": 0.3},
        )
        grid = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GREEN_C, "stroke_width": 1.2, "stroke_opacity": 0.5},
            axis_config={"stroke_color": GREEN_B, "stroke_width": 1.5},
        )

        # ── Show actual transformation A = [[4,1],[2,3]] ──
        mat_label = MathTex(
            r"A = \begin{pmatrix}4&1\\2&3\end{pmatrix}",
            font_size=26, color=YELLOW,
        )
        mat_label.to_corner(DL, buff=0.5)

        self.add(bg)
        self.play(Create(grid), Write(mat_label))
        self.play(grid.animate.apply_matrix([[4, 1], [2, 3]]), run_time=2)
        self.wait(2)
