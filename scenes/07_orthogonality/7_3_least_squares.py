"""7.3 Least Squares — Manim Animation

Rendering examples:
    manim -pqm scenes/07_orthogonality/7_3_least_squares.py LeastSquaresViz
    manim -pqm scenes/07_orthogonality/7_3_least_squares.py LeastSquaresFormula
"""

from manim import *


class LeastSquaresViz(Scene):
    """Least squares: minimize ||Ax - b||"""

    def construct(self):
        # ── Title ──
        title = Text("Least Squares", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 6, 1], y_range=[-1, 5, 1],
            x_length=7, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.4)
        self.play(Create(plane), run_time=1.0)

        # ── Data points ──
        data = [(1, 1), (2, 2.5), (3, 2.8), (4, 4.2), (5, 4.5)]
        dots = VGroup(*[Dot(plane.c2p(x, y), color=WHITE, radius=0.08) for x, y in data])
        self.play(FadeIn(dots))
        self.wait(0.3)

        # ── Best fit line: y ≈ 0.87x + 0.15 ──
        fit_line = Line(plane.c2p(0, 0.15), plane.c2p(5.5, 4.93), color=YELLOW, stroke_width=3)
        fit_label = MathTex(r"\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x", font_size=26, color=YELLOW)
        fit_label.next_to(fit_line.get_end(), UR, buff=0.1)
        self.play(Create(fit_line), Write(fit_label))
        self.wait(0.3)

        # ── Residual lines ──
        for x, y in data:
            y_hat = 0.87 * x + 0.15
            residual = DashedLine(plane.c2p(x, y), plane.c2p(x, y_hat), color=RED, stroke_width=2)
            self.play(Create(residual), run_time=0.3)

        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"\hat{x} = (A^T A)^{-1} A^T \vec{b}",
            font_size=36,
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)


class LeastSquaresFormula(Scene):
    """Normal equation derivation"""

    def construct(self):
        # ── Title ──
        title = Text("Normal Equation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Problem ──
        prob = MathTex(r"\min_{\mathbf{x}} \|A\mathbf{x} - \vec{b}\|^2", font_size=40)
        prob.move_to(UP * 1.5)
        self.play(Write(prob))
        self.wait(0.5)

        # ── Gradient = 0 ──
        grad = MathTex(r"A^T(A\vec{x} - \vec{b}) = \vec{0}", font_size=36)
        grad.move_to(UP * 0.2)
        self.play(Write(grad))
        self.wait(0.4)

        # ── Normal equation ──
        normal = MathTex(r"A^T A \vec{x} = A^T \vec{b}", font_size=36, color=YELLOW)
        normal.move_to(DOWN * 0.9)
        self.play(Write(normal))
        self.wait(0.4)

        # ── Solution ──
        solution = MathTex(
            r"\hat{x} = (A^T A)^{-1} A^T \vec{b}",
            font_size=36, color=GREEN,
        )
        solution.to_edge(DOWN, buff=0.8)
        self.play(Write(solution))
        self.wait(2)
