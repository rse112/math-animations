"""3.2 Matrix Operations — Manim Animation

Rendering examples:
    manim -pqm scenes/03_matrices/3_2_matrix_operations.py MatrixAddition
    manim -pqm scenes/03_matrices/3_2_matrix_operations.py MatrixMultiplication
"""

from manim import *


class MatrixAddition(Scene):
    """Matrix addition: element-wise"""

    def construct(self):
        # ── Title ──
        title = Text("Matrix Addition", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── A + B ──
        expr = MathTex(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}"
            r"+ \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}"
            r"= \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}",
            font_size=42,
        )
        expr.move_to(UP * 0.5)
        self.play(Write(expr))
        self.wait(0.5)

        # ── Rule ──
        rule = MathTex(r"(A + B)_{ij} = A_{ij} + B_{ij}", font_size=36, color=YELLOW)
        rule.to_edge(DOWN, buff=1.0)
        self.play(Write(rule))
        self.wait(0.5)

        # ── Requirement ──
        req = MathTex(r"A,\, B \in \mathbb{R}^{m \times n} \quad \text{(same dimensions)}", font_size=30, color=GREY_B)
        req.next_to(rule, UP, buff=0.4)
        self.play(Write(req))
        self.wait(2)


class MatrixMultiplication(Scene):
    """Matrix multiplication: dot product of rows and columns"""

    def construct(self):
        # ── Title ──
        title = Text("Matrix Multiplication", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── AB = C ──
        product = MathTex(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}"
            r"\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}"
            r"= \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}",
            font_size=38,
        )
        product.move_to(UP * 0.8)
        self.play(Write(product))
        self.wait(0.5)

        # ── One entry calculation ──
        entry = MathTex(
            r"C_{11} = 1\times5 + 2\times7 = 5 + 14 = 19",
            font_size=32, color=YELLOW,
        )
        entry.move_to(DOWN * 0.3)
        self.play(Write(entry))
        self.wait(0.5)

        # ── General rule ──
        rule = MathTex(
            r"C_{ij} = \sum_{k} A_{ik} B_{kj}",
            font_size=36,
        )
        rule.to_edge(DOWN, buff=0.7)
        self.play(Write(rule))
        self.wait(2)
