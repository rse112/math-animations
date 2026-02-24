"""3.1 What is a Matrix? — Manim Animation

Rendering examples:
    manim -pqm scenes/03_matrices/3_1_what_is_matrix.py MatrixIntro
    manim -pqm scenes/03_matrices/3_1_what_is_matrix.py MatrixDimension
"""

from manim import *


class MatrixIntro(Scene):
    """Matrix as a rectangular array of numbers"""

    def construct(self):
        # ── Title ──
        title = Text("What is a Matrix?", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Matrix display ──
        matrix = MathTex(
            r"A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}",
            font_size=52,
        )
        matrix.move_to(UP * 0.5)
        self.play(Write(matrix))
        self.wait(0.5)

        # ── Row/column labels ──
        row_label = MathTex(r"2 \text{ rows}", font_size=32, color=YELLOW)
        col_label = MathTex(r"3 \text{ columns}", font_size=32, color=GREEN)
        row_label.next_to(matrix, LEFT, buff=0.6)
        col_label.next_to(matrix, DOWN, buff=0.5)
        self.play(Write(row_label), Write(col_label))
        self.wait(0.5)

        # ── Dimension notation ──
        dim = MathTex(r"A \in \mathbb{R}^{2 \times 3}", font_size=40)
        dim.to_edge(DOWN, buff=0.7)
        self.play(Write(dim))
        self.wait(2)


class MatrixDimension(Scene):
    """Matrix entry notation a_ij"""

    def construct(self):
        # ── Title ──
        title = Text("Matrix Entry Notation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── General matrix ──
        general = MathTex(
            r"A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}",
            font_size=36,
        )
        general.move_to(UP * 0.3)
        self.play(Write(general))
        self.wait(0.5)

        # ── Entry notation ──
        entry = MathTex(
            r"a_{ij} \;=\; \text{entry at row } i,\; \text{column } j",
            font_size=32, color=YELLOW,
        )
        entry.to_edge(DOWN, buff=0.8)
        self.play(Write(entry))

        # ── m×n ──
        dim = MathTex(r"A \in \mathbb{R}^{m \times n}", font_size=36)
        dim.next_to(entry, UP, buff=0.4)
        self.play(Write(dim))
        self.wait(2)
