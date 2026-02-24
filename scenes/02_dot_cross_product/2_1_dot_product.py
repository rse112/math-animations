"""2.1 Dot Product — Manim Animation

Rendering examples:
    manim -pqm scenes/02_dot_cross_product/2_1_dot_product.py DotProductAlgebraic
    manim -pqm scenes/02_dot_cross_product/2_1_dot_product.py DotProductGeometric
"""

from manim import *


class DotProductAlgebraic(Scene):
    """Algebraic definition and example of dot product"""

    def construct(self):
        # ── Title ──
        title = Text("Dot Product", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"\vec{v} \cdot \vec{w} = v_1 w_1 + v_2 w_2",
            font_size=42,
        )
        formula.move_to(UP * 1.5)
        self.play(Write(formula))
        self.wait(0.5)

        # ── Example vectors ──
        example_v = MathTex(r"\vec{v} = (3,\ 2)", font_size=34, color=YELLOW)
        example_w = MathTex(r"\vec{w} = (1,\ 4)", font_size=34, color=GREEN)
        example_v.move_to(LEFT * 2.8 + DOWN * 0.2)
        example_w.move_to(RIGHT * 2.8 + DOWN * 0.2)
        self.play(Write(example_v), Write(example_w))
        self.wait(0.5)

        # ── Calculation ──
        calc = MathTex(
            r"\vec{v} \cdot \vec{w} = 3 \times 1 + 2 \times 4 = 3 + 8 = 11",
            font_size=34,
        )
        calc.move_to(DOWN * 1.5)
        self.play(Write(calc))
        self.wait(2)


class DotProductGeometric(Scene):
    """Geometric interpretation: v·w = |v||w|cos θ"""

    def construct(self):
        # ── Title ──
        title = Text("Dot Product — Geometric", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 4, 1],
            x_length=7, y_length=4.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.5)
        self.play(Create(plane), run_time=1.0)

        # ── Vectors ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(4, 1), buff=0, color=YELLOW, stroke_width=5)
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 3), buff=0, color=GREEN, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_end(), RIGHT, buff=0.1)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_end(), UP, buff=0.1)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.3)

        # ── Angle arc ──
        line_v = Line(plane.c2p(0, 0), plane.c2p(4, 1))
        line_w = Line(plane.c2p(0, 0), plane.c2p(1, 3))
        angle = Angle(line_v, line_w, radius=0.7, color=WHITE)
        theta = MathTex(r"\theta", font_size=28)
        theta.next_to(plane.c2p(0, 0), UR, buff=0.5)
        self.play(Create(angle), Write(theta))
        self.wait(0.3)

        # ── Formula ──
        formula = MathTex(
            r"\vec{v} \cdot \vec{w} = |\vec{v}||\vec{w}|\cos\theta",
            font_size=36,
        )
        formula.to_edge(DOWN, buff=0.7)
        self.play(Write(formula))
        self.wait(0.5)

        # ── Perpendicular special case ──
        note = MathTex(
            r"\vec{v} \perp \vec{w} \;\Rightarrow\; \vec{v} \cdot \vec{w} = 0",
            font_size=30, color=BLUE_B,
        )
        note.next_to(formula, UP, buff=0.4)
        self.play(Write(note))
        self.wait(2)
