"""6.1 Eigenvalues and Eigenvectors — Manim Animation

Rendering examples:
    manim -pqm scenes/06_eigenvalues_eigenvectors/6_1_definition.py EigenvalueEquation
    manim -pqm scenes/06_eigenvalues_eigenvectors/6_1_definition.py EigenvectorVisualization
"""

from manim import *


class EigenvalueEquation(Scene):
    """Eigenvalue equation: Av = λv"""

    def construct(self):
        # ── Title ──
        title = Text("Eigenvalues & Eigenvectors", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Core equation ──
        eq = MathTex(r"A\vec{v} = \lambda\vec{v}", font_size=60)
        eq.move_to(UP * 1.0)
        self.play(Write(eq))
        self.wait(0.5)

        # ── Labels ──
        labels = VGroup(
            MathTex(r"\vec{v} \neq \vec{0} : \text{ eigenvector}", font_size=32, color=YELLOW),
            MathTex(r"\lambda \in \mathbb{R} : \text{ eigenvalue}", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.4)
        labels.move_to(DOWN * 0.6)
        self.play(Write(labels))
        self.wait(0.5)

        # ── Example ──
        example = MathTex(
            r"\begin{pmatrix}3&1\\0&2\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}"
            r"= 3\begin{pmatrix}1\\0\end{pmatrix}",
            font_size=32,
        )
        example.to_edge(DOWN, buff=0.7)
        self.play(Write(example))
        self.wait(2)


class EigenvectorVisualization(Scene):
    """Eigenvectors only scale, never rotate"""

    def construct(self):
        # ── Title ──
        title = Text("Eigenvector Direction", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-3, 5, 1], y_range=[-3, 4, 1],
            x_length=8, y_length=5.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.2)
        self.play(Create(plane), run_time=1.0)

        # ── Eigenvector v (direction preserved) ──
        v = Arrow(plane.c2p(0, 0), plane.c2p(2, 0), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=30, color=YELLOW)
        v_label.next_to(v.get_end(), DOWN, buff=0.15)
        self.play(GrowArrow(v), Write(v_label))
        self.wait(0.3)

        # ── Av = 3v (scaled, same direction) ──
        Av = Arrow(plane.c2p(0, 0), plane.c2p(4, 0), buff=0, color=RED, stroke_width=5)
        Av_label = MathTex(r"A\vec{v} = 3\vec{v}", font_size=28, color=RED)
        Av_label.next_to(Av.get_end(), DOWN, buff=0.15)
        self.play(TransformFromCopy(v, Av), Write(Av_label))
        self.wait(0.3)

        # ── Non-eigenvector w (direction changes) ──
        w = Arrow(plane.c2p(0, 0), plane.c2p(1, 2), buff=0, color=GREEN, stroke_width=5)
        w_label = MathTex(r"\vec{w}", font_size=30, color=GREEN)
        w_label.next_to(w.get_end(), UL, buff=0.1)
        self.play(GrowArrow(w), Write(w_label))
        self.wait(0.3)

        # ── Aw rotates (direction changes) ──
        Aw = Arrow(plane.c2p(0, 0), plane.c2p(3, 2), buff=0, color=ORANGE, stroke_width=5)
        Aw_label = MathTex(r"A\vec{w} \text{ (rotated)}", font_size=24, color=ORANGE)
        Aw_label.next_to(Aw.get_end(), UR, buff=0.1)
        self.play(GrowArrow(Aw), Write(Aw_label))
        self.wait(2)
