"""7.1 Orthogonal Vectors and Matrices — Manim Animation

Rendering examples:
    manim -pqm scenes/07_orthogonality/7_1_orthogonal_vectors_matrices.py OrthogonalVectors
    manim -pqm scenes/07_orthogonality/7_1_orthogonal_vectors_matrices.py OrthogonalMatrix
"""

from manim import *


class OrthogonalVectors(Scene):
    """Two vectors are orthogonal when v·w = 0"""

    def construct(self):
        # ── Title ──
        title = Text("Orthogonal Vectors", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 4, 1],
            x_length=7, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.4)
        self.play(Create(plane), run_time=1.0)

        # ── v and w orthogonal ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 0), buff=0, color=YELLOW, stroke_width=5)
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(0, 2), buff=0, color=GREEN, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_end(), DOWN, buff=0.15)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_end(), LEFT, buff=0.15)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.3)

        # ── Right angle mark ──
        corner = plane.c2p(0, 0)
        sq = Square(side_length=0.2, color=WHITE, stroke_width=2)
        sq.move_to(corner + RIGHT * 0.1 + UP * 0.1)
        self.play(Create(sq))
        self.wait(0.3)

        # ── Dot product = 0 ──
        formula = MathTex(
            r"\vec{v} \cdot \vec{w} = 0 \;\Leftrightarrow\; \vec{v} \perp \vec{w}",
            font_size=36,
        )
        formula.to_edge(DOWN, buff=0.6)
        self.play(Write(formula))
        self.wait(2)


class OrthogonalMatrix(Scene):
    """Orthogonal matrix: Q^T Q = I"""

    def construct(self):
        # ── Title ──
        title = Text("Orthogonal Matrix", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Definition ──
        defn = MathTex(r"Q^T Q = I \;\Leftrightarrow\; Q^{-1} = Q^T", font_size=40)
        defn.move_to(UP * 1.5)
        self.play(Write(defn))
        self.wait(0.5)

        # ── Properties ──
        props = VGroup(
            MathTex(r"\bullet\; \text{Columns of } Q \text{ are orthonormal}", font_size=30, color=YELLOW),
            MathTex(r"\bullet\; |\det(Q)| = 1", font_size=30, color=GREEN),
            MathTex(r"\bullet\; Q \text{ preserves lengths and angles}", font_size=30, color=BLUE_B),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        props.move_to(DOWN * 0.3)
        self.play(Write(props))
        self.wait(0.5)

        # ── Example ──
        example = MathTex(
            r"Q = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}"
            r"\;\text{(rotation matrix)}",
            font_size=28,
        )
        example.to_edge(DOWN, buff=0.7)
        self.play(Write(example))
        self.wait(2)
