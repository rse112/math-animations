"""3.3 Inverse Matrix and Determinant — Manim Animation

Rendering examples:
    manim -pqm scenes/03_matrices/3_3_inverse_determinant.py Determinant2x2
    manim -pqm scenes/03_matrices/3_3_inverse_determinant.py InverseMatrix2x2
"""

from manim import *


class Determinant2x2(Scene):
    """Determinant of a 2×2 matrix"""

    def construct(self):
        # ── Title ──
        title = Text("Determinant", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Definition ──
        defn = MathTex(
            r"\det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc",
            font_size=44,
        )
        defn.move_to(UP * 1.0)
        self.play(Write(defn))
        self.wait(0.5)

        # ── Example ──
        example = MathTex(
            r"\det\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix} = 3 \times 4 - 2 \times 1 = 12 - 2 = 10",
            font_size=34,
        )
        example.move_to(DOWN * 0.2)
        self.play(Write(example))
        self.wait(0.5)

        # ── Geometric meaning ──
        geo = MathTex(
            r"|\det(A)| = \text{area of parallelogram spanned by columns}",
            font_size=28, color=YELLOW,
        )
        geo.to_edge(DOWN, buff=0.7)
        self.play(Write(geo))
        self.wait(2)


class InverseMatrix2x2(Scene):
    """Inverse of a 2×2 matrix"""

    def construct(self):
        # ── Title ──
        title = Text("Inverse Matrix", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Definition ──
        defn = MathTex(r"A A^{-1} = A^{-1} A = I", font_size=40)
        defn.move_to(UP * 1.5)
        self.play(Write(defn))
        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}"
            r"\quad \text{for } A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            font_size=32,
        )
        formula.move_to(UP * 0.1)
        self.play(Write(formula))
        self.wait(0.5)

        # ── Example ──
        example = MathTex(
            r"\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}^{-1}"
            r"= \frac{1}{10}\begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix}",
            font_size=34,
        )
        example.to_edge(DOWN, buff=0.9)
        self.play(Write(example))
        self.wait(0.5)

        # ── Existence condition ──
        cond = MathTex(r"A^{-1} \text{ exists} \;\Leftrightarrow\; \det(A) \neq 0", font_size=30, color=YELLOW)
        cond.next_to(example, UP, buff=0.4)
        self.play(Write(cond))
        self.wait(2)
