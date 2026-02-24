"""8.1 SVD Definition — Manim Animation

Rendering examples:
    manim -pqm scenes/08_svd/8_1_svd_definition.py SVDFormula
    manim -pqm scenes/08_svd/8_1_svd_definition.py SVDComponents
"""

from manim import *


class SVDFormula(Scene):
    """Singular Value Decomposition: A = U Σ V^T"""

    def construct(self):
        # ── Title ──
        title = Text("Singular Value Decomposition", font_size=38)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Core formula ──
        formula = MathTex(r"A = U \Sigma V^T", font_size=64)
        formula.move_to(UP * 1.0)
        self.play(Write(formula))
        self.wait(0.5)

        # ── Component descriptions ──
        descs = VGroup(
            MathTex(r"U \in \mathbb{R}^{m\times m} : \text{ left singular vectors (orthonormal)}", font_size=26, color=RED_B),
            MathTex(r"\Sigma \in \mathbb{R}^{m\times n} : \text{ diagonal, singular values } \sigma_1 \geq \sigma_2 \geq \cdots \geq 0", font_size=26, color=GREEN),
            MathTex(r"V \in \mathbb{R}^{n\times n} : \text{ right singular vectors (orthonormal)}", font_size=26, color=BLUE_B),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        descs.move_to(DOWN * 0.8)
        self.play(Write(descs))
        self.wait(0.5)

        # ── Existence ──
        exist = MathTex(r"\text{Every matrix } A \in \mathbb{R}^{m\times n} \text{ has an SVD}", font_size=28, color=YELLOW)
        exist.to_edge(DOWN, buff=0.5)
        self.play(Write(exist))
        self.wait(2)


class SVDComponents(Scene):
    """SVD component shapes and singular values"""

    def construct(self):
        # ── Title ──
        title = Text("SVD Components", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Matrix shapes ──
        shapes = MathTex(
            r"\underbrace{A}_{m\times n}"
            r"= \underbrace{U}_{m\times m}"
            r"\underbrace{\Sigma}_{m\times n}"
            r"\underbrace{V^T}_{n\times n}",
            font_size=38,
        )
        shapes.move_to(UP * 1.0)
        self.play(Write(shapes))
        self.wait(0.5)

        # ── Singular values ──
        sigma = MathTex(
            r"\Sigma = \begin{pmatrix}\sigma_1 & & \\ & \sigma_2 & \\ & & \ddots\end{pmatrix},"
            r"\quad \sigma_i = \sqrt{\lambda_i(A^T A)}",
            font_size=30,
        )
        sigma.move_to(DOWN * 0.5)
        self.play(Write(sigma))
        self.wait(0.5)

        # ── Rank ──
        rank = MathTex(
            r"\text{rank}(A) = \text{number of nonzero singular values}",
            font_size=28, color=YELLOW,
        )
        rank.to_edge(DOWN, buff=0.7)
        self.play(Write(rank))
        self.wait(2)
