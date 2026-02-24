"""4.4 Composition of Transformations — Manim Animation

Rendering examples:
    manim -pqm scenes/04_linear_transformations/4_4_composition.py TransformComposition
    manim -pqm scenes/04_linear_transformations/4_4_composition.py CompositionOrder
"""

from manim import *
import numpy as np


class TransformComposition(Scene):
    """Composing two linear transformations: BA = apply A then B"""

    def construct(self):
        # ── Title ──
        title = Text("Composition of Transformations", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Labels ──
        A_label = MathTex(
            r"A = \begin{pmatrix}2&0\\0&1\end{pmatrix} \text{ (scale x)}",
            font_size=28, color=YELLOW,
        )
        B_label = MathTex(
            r"B = \begin{pmatrix}1&1\\0&1\end{pmatrix} \text{ (shear)}",
            font_size=28, color=GREEN,
        )
        BA_label = MathTex(
            r"BA = \begin{pmatrix}2&2\\0&1\end{pmatrix}",
            font_size=28, color=RED,
        )

        A_label.to_corner(UL, buff=0.7).shift(DOWN * 0.9)
        B_label.next_to(A_label, DOWN, buff=0.3)
        BA_label.next_to(B_label, DOWN, buff=0.3)

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
        self.play(Create(grid), run_time=1.0)
        self.play(Write(A_label))
        self.wait(0.3)

        # ── Apply A first ──
        self.play(grid.animate.apply_matrix([[2, 0], [0, 1]]), run_time=1.5)
        self.wait(0.3)
        self.play(Write(B_label))

        # ── Then apply B ──
        self.play(grid.animate.apply_matrix([[1, 1], [0, 1]]), run_time=1.5)
        self.play(Write(BA_label))
        self.wait(2)


class CompositionOrder(Scene):
    """Order matters: AB ≠ BA in general"""

    def construct(self):
        # ── Title ──
        title = Text("Order Matters: AB ≠ BA", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── AB ──
        AB = MathTex(
            r"AB = \begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix}"
            r"= \begin{pmatrix}2&1\\0&1\end{pmatrix}",
            font_size=30,
        )
        AB.move_to(UP * 0.8)
        self.play(Write(AB))
        self.wait(0.5)

        # ── BA ──
        BA = MathTex(
            r"BA = \begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}"
            r"= \begin{pmatrix}2&2\\0&1\end{pmatrix}",
            font_size=30,
        )
        BA.move_to(DOWN * 0.3)
        self.play(Write(BA))
        self.wait(0.5)

        # ── Not equal ──
        neq = MathTex(r"AB \neq BA", font_size=44, color=RED)
        neq.to_edge(DOWN, buff=0.8)
        self.play(Write(neq))
        self.wait(2)
