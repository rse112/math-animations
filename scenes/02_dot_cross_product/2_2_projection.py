"""2.2 Projection — Manim Animation

Rendering examples:
    manim -pqm scenes/02_dot_cross_product/2_2_projection.py VectorProjection
"""

from manim import *


class VectorProjection(Scene):
    """Projection of vector v onto vector w"""

    def construct(self):
        # ── Title ──
        title = Text("Vector Projection", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 6, 1], y_range=[-1, 4, 1],
            x_length=7, y_length=4.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.5)
        self.play(Create(plane), run_time=1.0)

        # ── w along x-axis for clarity ──
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(5, 0), buff=0, color=GREEN, stroke_width=5)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_end(), RIGHT, buff=0.1)
        self.play(GrowArrow(w_arrow), Write(w_label))

        # ── v = (3, 3) ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 3), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_end(), UL, buff=0.1)
        self.play(GrowArrow(v_arrow), Write(v_label))
        self.wait(0.5)

        # ── Perpendicular drop ──
        perp_line = DashedLine(plane.c2p(3, 3), plane.c2p(3, 0), color=WHITE, stroke_width=3)
        self.play(Create(perp_line))

        # ── Right angle mark ──
        corner = plane.c2p(3, 0)
        sq = Square(side_length=0.18, color=WHITE, stroke_width=2)
        sq.move_to(corner + LEFT * 0.09 + UP * 0.09)
        self.play(Create(sq))

        # ── Projection arrow ──
        proj_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 0), buff=0, color=RED, stroke_width=5)
        proj_label = MathTex(r"\vec{p}", font_size=28, color=RED)
        proj_label.next_to(proj_arrow.get_center(), DOWN, buff=0.25)
        self.play(GrowArrow(proj_arrow), Write(proj_label))
        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"\vec{p} = {\vec{v} \cdot \vec{w} \over |\vec{w}|^2}\,\vec{w}",
            font_size=34,
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)
