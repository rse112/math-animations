"""8.2 SVD Geometric Meaning — Manim Animation

Rendering examples:
    manim -pqm scenes/08_svd/8_2_svd_geometric.py SVDGeometric
"""

from manim import *
import numpy as np


class SVDGeometric(Scene):
    """SVD as three sequential transformations: rotate → stretch → rotate"""

    def construct(self):
        # ── Title ──
        title = Text("SVD — Geometric View", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"A = U\Sigma V^T",
            font_size=40,
        )
        formula.to_corner(UR, buff=0.8).shift(DOWN * 0.8)
        self.play(Write(formula))
        self.wait(0.3)

        # ── Three steps ──
        steps = VGroup(
            MathTex(r"1.\; V^T : \text{ rotate input space}", font_size=28, color=BLUE_B),
            MathTex(r"2.\; \Sigma : \text{ stretch along axes } (\sigma_1, \sigma_2)", font_size=28, color=GREEN),
            MathTex(r"3.\; U : \text{ rotate output space}", font_size=28, color=RED_B),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        steps.to_corner(UL, buff=0.8).shift(DOWN * 0.8)
        for s in steps:
            self.play(Write(s))
            self.wait(0.3)

        # ── Unit circle → ellipse ──
        bg = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.2},
            axis_config={"stroke_opacity": 0.4},
        )
        self.add(bg)

        # Initial unit circle
        circle = Circle(radius=1.2, color=YELLOW, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.3)

        # After SVD (ellipse stretched by σ1, σ2)
        ellipse = Ellipse(width=3.6, height=1.6, color=RED, stroke_width=3)
        ellipse.move_to(ORIGIN).rotate(np.pi / 6)
        self.play(Transform(circle, ellipse), run_time=2)
        self.wait(0.5)

        # ── Caption ──
        cap = MathTex(
            r"\text{Unit circle} \xrightarrow{A} \text{Ellipse with semi-axes } \sigma_1, \sigma_2",
            font_size=26, color=YELLOW,
        )
        cap.to_edge(DOWN, buff=0.5)
        self.play(Write(cap))
        self.wait(2)
