"""8.3 SVD Applications — Manim Animation

Rendering examples:
    manim -pqm scenes/08_svd/8_3_svd_applications.py LowRankApproximation
    manim -pqm scenes/08_svd/8_3_svd_applications.py SVDApplications
"""

from manim import *


class LowRankApproximation(Scene):
    """Low-rank approximation via truncated SVD"""

    def construct(self):
        # ── Title ──
        title = Text("Low-Rank Approximation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Full SVD ──
        full = MathTex(
            r"A = \sum_{i=1}^{r} \sigma_i \vec{u}_i \vec{v}_i^T",
            font_size=40,
        )
        full.move_to(UP * 1.5)
        self.play(Write(full))
        self.wait(0.5)

        # ── Rank-k approximation ──
        rank_k = MathTex(
            r"A_k = \sum_{i=1}^{k} \sigma_i \vec{u}_i \vec{v}_i^T \quad (k < r)",
            font_size=36, color=YELLOW,
        )
        rank_k.move_to(UP * 0.2)
        self.play(Write(rank_k))
        self.wait(0.5)

        # ── Eckart-Young theorem ──
        theorem = MathTex(
            r"\|A - A_k\|_F = \min_{\text{rank-}k\; B} \|A - B\|_F = \sqrt{\sigma_{k+1}^2 + \cdots + \sigma_r^2}",
            font_size=24, color=GREEN,
        )
        theorem.move_to(DOWN * 0.8)
        self.play(Write(theorem))
        self.wait(0.5)

        # ── Applications ──
        apps = VGroup(
            MathTex(r"\bullet\; \text{Image compression}", font_size=28, color=BLUE_B),
            MathTex(r"\bullet\; \text{Dimensionality reduction (PCA)}", font_size=28, color=BLUE_B),
            MathTex(r"\bullet\; \text{Recommender systems}", font_size=28, color=BLUE_B),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        apps.to_edge(DOWN, buff=0.6)
        self.play(Write(apps))
        self.wait(2)


class SVDApplications(Scene):
    """Summary of SVD applications"""

    def construct(self):
        # ── Title ──
        title = Text("SVD Applications", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── PCA connection ──
        pca = MathTex(
            r"\text{PCA}: \quad \text{principal components} = \text{right singular vectors of } X",
            font_size=28, color=YELLOW,
        )
        pca.move_to(UP * 1.5)
        self.play(Write(pca))
        self.wait(0.4)

        # ── Pseudoinverse ──
        pinv = MathTex(
            r"A^+ = V \Sigma^+ U^T \quad (\text{Moore-Penrose pseudoinverse})",
            font_size=28, color=GREEN,
        )
        pinv.move_to(UP * 0.4)
        self.play(Write(pinv))
        self.wait(0.4)

        # ── Condition number ──
        cond = MathTex(
            r"\kappa(A) = {\sigma_{\max} \over \sigma_{\min}} \quad (\text{condition number})",
            font_size=28, color=BLUE_B,
        )
        cond.move_to(DOWN * 0.6)
        self.play(Write(cond))
        self.wait(0.4)

        # ── Least squares ──
        ls = MathTex(
            r"\hat{x} = A^+ \vec{b} = V\Sigma^+ U^T \vec{b} \quad (\text{least squares via SVD})",
            font_size=26, color=RED_B,
        )
        ls.to_edge(DOWN, buff=0.8)
        self.play(Write(ls))
        self.wait(2)
