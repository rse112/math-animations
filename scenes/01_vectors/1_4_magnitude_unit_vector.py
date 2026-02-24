"""1.4 Vector Magnitude and Unit Vector — Manim Animation

Rendering examples:
    manim -pqm scenes/01_vectors/1_4_magnitude_unit_vector.py VectorMagnitude
    manim -pqm scenes/01_vectors/1_4_magnitude_unit_vector.py UnitVector
"""

from manim import *


class VectorMagnitude(Scene):
    """Vector magnitude via the Pythagorean theorem"""

    def construct(self):
        # ── Title ──
        title = Text("Vector Magnitude", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=7, y_length=5.5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.2)
        self.play(Create(plane), run_time=1.5)

        # ── Vector v = (3, 4) ──
        vec_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 4), buff=0, color=YELLOW, stroke_width=5)
        vec_label = MathTex(r"\vec{v} = (3,\ 4)", font_size=28, color=YELLOW)
        vec_label.next_to(vec_arrow.get_center(), LEFT, buff=0.2)
        self.play(GrowArrow(vec_arrow), Write(vec_label))
        self.wait(0.5)

        # ── Right triangle ──
        x_line = Line(plane.c2p(0, 0), plane.c2p(3, 0), color=RED, stroke_width=4)
        y_line = Line(plane.c2p(3, 0), plane.c2p(3, 4), color=GREEN, stroke_width=4)
        x_label = MathTex("3", font_size=28, color=RED)
        x_label.next_to(x_line, DOWN, buff=0.2)
        y_label = MathTex("4", font_size=28, color=GREEN)
        y_label.next_to(y_line, RIGHT, buff=0.2)

        self.play(Create(x_line), FadeIn(x_label))
        self.play(Create(y_line), FadeIn(y_label))

        # ── Right angle mark ──
        corner = plane.c2p(3, 0)
        sq = Square(side_length=0.2, color=WHITE, stroke_width=2)
        sq.move_to(corner + RIGHT * 0.1 + UP * 0.1)
        self.play(Create(sq))
        self.wait(0.3)

        # ── Formula ──
        formula = MathTex(
            r"|\vec{v}| = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5",
            font_size=32,
        )
        formula.to_edge(DOWN, buff=0.6)
        self.play(Write(formula))
        self.wait(2)


class UnitVector(Scene):
    """Unit vector: normalize v to length 1"""

    def construct(self):
        # ── Title ──
        title = Text("Unit Vector", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-2, 4, 1], y_range=[-2, 3, 1],
            x_length=7, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.2)
        self.play(Create(plane), run_time=1.5)

        # ── Unit circle ──
        one_unit = plane.c2p(1, 0)[0] - plane.c2p(0, 0)[0]
        unit_circle = Circle(radius=one_unit, color=GREY, stroke_width=2, stroke_opacity=0.6)
        unit_circle.move_to(plane.c2p(0, 0))
        self.play(Create(unit_circle))

        # ── Original vector v = (3, 2) ──
        vec_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 2), buff=0, color=YELLOW, stroke_width=5)
        vec_label = MathTex(r"\vec{v} = (3,\ 2)", font_size=28, color=YELLOW)
        vec_label.next_to(vec_arrow.get_end(), UR, buff=0.15)
        self.play(GrowArrow(vec_arrow), Write(vec_label))
        self.wait(0.5)

        # ── Unit vector hat_v ──
        mag = (3**2 + 2**2) ** 0.5
        ux, uy = 3 / mag, 2 / mag
        unit_arrow = Arrow(plane.c2p(0, 0), plane.c2p(ux, uy), buff=0, color=RED, stroke_width=5)
        unit_label = MathTex(r"\hat{v}", font_size=32, color=RED)
        unit_label.next_to(unit_arrow.get_end(), UR, buff=0.15)
        self.play(GrowArrow(unit_arrow), Write(unit_label))
        self.wait(0.5)

        # ── Formula ──
        formula = MathTex(
            r"\hat{v} = {\vec{v} \over |\vec{v}|} = {(3,\ 2) \over \sqrt{13}}",
            font_size=32,
        )
        formula.to_edge(DOWN, buff=0.6)
        self.play(Write(formula))
        self.wait(2)
