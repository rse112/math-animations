"""6.3 Diagonalization — Manim Animation

Rendering examples:
    manim -pqm scenes/06_eigenvalues_eigenvectors/6_3_diagonalization.py DiagonalizationFormula
    manim -pqm scenes/06_eigenvalues_eigenvectors/6_3_diagonalization.py DiagonalizationExample
"""

from manim import *


class DiagonalizationFormula(Scene):
    """A = P D P^{-1} decomposition"""

    def construct(self):
        # ── Title ──
        title = Text("Diagonalization", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Core formula ──
        formula = MathTex(r"A = P D P^{-1}", font_size=56)
        formula.move_to(UP * 1.2)
        self.play(Write(formula))
        self.wait(0.5)

        # ── Component labels ──
        P_desc = MathTex(r"P : \text{ columns are eigenvectors}", font_size=30, color=YELLOW)
        D_desc = MathTex(r"D : \text{ diagonal matrix of eigenvalues}", font_size=30, color=GREEN)
        P_inv = MathTex(r"P^{-1} : \text{ inverse of } P", font_size=30, color=BLUE_B)

        desc_group = VGroup(P_desc, D_desc, P_inv).arrange(DOWN, buff=0.35)
        desc_group.move_to(DOWN * 0.5)
        self.play(Write(desc_group))
        self.wait(0.5)

        # ── Condition ──
        cond = MathTex(
            r"A \text{ is diagonalizable} \;\Leftrightarrow\; A \text{ has } n \text{ linearly independent eigenvectors}",
            font_size=24, color=GREY_B,
        )
        cond.to_edge(DOWN, buff=0.6)
        self.play(Write(cond))
        self.wait(2)


class DiagonalizationExample(Scene):
    """Concrete 2×2 diagonalization example"""

    def construct(self):
        # ── Title ──
        title = Text("Diagonalization — Example", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── A ──
        A = MathTex(
            r"A = \begin{pmatrix}4&1\\2&3\end{pmatrix},\quad \lambda_1 = 5,\; \lambda_2 = 2",
            font_size=30,
        )
        A.move_to(UP * 1.6)
        self.play(Write(A))
        self.wait(0.4)

        # ── P and D ──
        P = MathTex(
            r"P = \begin{pmatrix}1&1\\1&-2\end{pmatrix},\quad D = \begin{pmatrix}5&0\\0&2\end{pmatrix}",
            font_size=30,
        )
        P.move_to(UP * 0.3)
        self.play(Write(P))
        self.wait(0.4)

        # ── Power of A ──
        power = MathTex(
            r"A^k = P D^k P^{-1} = P \begin{pmatrix}5^k&0\\0&2^k\end{pmatrix} P^{-1}",
            font_size=28, color=YELLOW,
        )
        power.to_edge(DOWN, buff=0.8)
        self.play(Write(power))
        self.wait(2)
