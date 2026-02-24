"""5.1 Subspace and Span — Manim Animation

Rendering examples:
    manim -pqm scenes/05_vector_spaces/5_1_subspace_span.py Span1D
    manim -pqm scenes/05_vector_spaces/5_1_subspace_span.py Span2D
"""

from manim import *


class Span1D(Scene):
    """Span of a single vector forms a line"""

    def construct(self):
        # ── Title ──
        title = Text("Span of One Vector", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=5.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.2)
        self.play(Create(plane), run_time=1.0)

        # ── Vector v ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_end(), UR, buff=0.1)
        self.play(GrowArrow(v_arrow), Write(v_label))
        self.wait(0.3)

        # ── Span = line through origin ──
        span_line = Line(plane.c2p(-4, -2), plane.c2p(4, 2), color=YELLOW, stroke_width=2, stroke_opacity=0.5)
        self.play(Create(span_line))
        self.wait(0.3)

        # ── Scalar multiples ──
        for scalar, color in [(-1.5, RED), (0.5, GREEN), (2.5, BLUE)]:
            arrow = Arrow(plane.c2p(0, 0), plane.c2p(2*scalar, scalar), buff=0, color=color, stroke_width=3)
            lbl = MathTex(f"{scalar}" + r"\vec{v}", font_size=22, color=color)
            lbl.next_to(arrow.get_end(), UR if scalar > 0 else DL, buff=0.1)
            self.play(GrowArrow(arrow), Write(lbl), run_time=0.6)

        # ── Formula ──
        formula = MathTex(r"\text{span}(\vec{v}) = \{c\vec{v} \mid c \in \mathbb{R}\}", font_size=32)
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)


class Span2D(Scene):
    """Span of two linearly independent vectors fills the plane"""

    def construct(self):
        # ── Title ──
        title = Text("Span of Two Vectors", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=8, y_length=5.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.2)
        self.play(Create(plane), run_time=1.0)

        # ── v and w ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, 0), buff=0, color=YELLOW, stroke_width=5)
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(0, 2), buff=0, color=GREEN, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_end(), DOWN, buff=0.1)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_end(), LEFT, buff=0.1)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.3)

        # ── Shaded plane (entire background) ──
        fill = Rectangle(
            width=8, height=5.5, color=PURPLE, fill_opacity=0.15, stroke_width=0,
        ).move_to(plane.get_center())
        self.play(FadeIn(fill))
        self.wait(0.3)

        # ── Formula ──
        formula = MathTex(
            r"\text{span}(\vec{v},\vec{w}) = \{c_1\vec{v} + c_2\vec{w} \mid c_1, c_2 \in \mathbb{R}\} = \mathbb{R}^2",
            font_size=28,
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)
