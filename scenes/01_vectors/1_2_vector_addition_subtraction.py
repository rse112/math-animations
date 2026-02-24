"""1.2 Vector Addition and Subtraction — Manim Animation

Rendering examples:
    manim -pqm scenes/01_vectors/1_2_vector_addition_subtraction.py VectorAddition
    manim -pqm scenes/01_vectors/1_2_vector_addition_subtraction.py VectorSubtraction
    manim -pqm scenes/01_vectors/1_2_vector_addition_subtraction.py ParallelogramRule
"""

from manim import *


class VectorAddition(Scene):
    """Tip-to-tail vector addition: v + w"""

    def construct(self):
        # ── Title ──
        title = Text("Vector Addition", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 7, 1], y_range=[-1, 5, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.3)
        self.play(Create(plane), run_time=1.5)

        # ── v = (3, 2) ──
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 2), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v} = (3,\ 2)", font_size=28, color=YELLOW)
        v_label.next_to(v_arrow.get_center(), UL, buff=0.15)

        # ── w = (2, 1) ──
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=GREEN, stroke_width=5)
        w_label = MathTex(r"\vec{w} = (2,\ 1)", font_size=28, color=GREEN)
        w_label.next_to(w_arrow.get_center(), DR, buff=0.15)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.5)

        # ── Tip-to-tail: translate w to tip of v ──
        w_shifted = Arrow(plane.c2p(3, 2), plane.c2p(5, 3), buff=0, color=GREEN, stroke_width=4)
        self.play(TransformFromCopy(w_arrow, w_shifted))
        self.wait(0.3)

        # ── Resultant vector ──
        sum_arrow = Arrow(plane.c2p(0, 0), plane.c2p(5, 3), buff=0, color=RED, stroke_width=5)
        sum_label = MathTex(r"\vec{v} + \vec{w} = (5,\ 3)", font_size=28, color=RED)
        sum_label.next_to(sum_arrow.get_center(), UR, buff=0.2)
        self.play(GrowArrow(sum_arrow), Write(sum_label))
        self.wait(2)


class VectorSubtraction(Scene):
    """Vector subtraction: v - w = v + (-w)"""

    def construct(self):
        # ── Title ──
        title = Text("Vector Subtraction", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-3, 5, 1], y_range=[-2, 4, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.3)
        self.play(Create(plane), run_time=1.5)

        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(3, 2), buff=0, color=YELLOW, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_center(), UL, buff=0.15)

        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=GREEN, stroke_width=5)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_center(), DR, buff=0.15)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.5)

        # ── -w ──
        neg_w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(-2, -1), buff=0, color=ORANGE, stroke_width=5)
        neg_w_label = MathTex(r"-\vec{w}", font_size=32, color=ORANGE)
        neg_w_label.next_to(neg_w_arrow.get_center(), UL, buff=0.15)
        self.play(GrowArrow(neg_w_arrow), Write(neg_w_label))
        self.wait(0.3)

        # ── -w shifted to tip of v ──
        neg_w_shifted = Arrow(plane.c2p(3, 2), plane.c2p(1, 1), buff=0, color=ORANGE, stroke_width=4)
        self.play(TransformFromCopy(neg_w_arrow, neg_w_shifted))

        diff_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 1), buff=0, color=RED, stroke_width=5)
        diff_label = MathTex(r"\vec{v} - \vec{w} = (1,\ 1)", font_size=28, color=RED)
        diff_label.next_to(diff_arrow.get_center(), UR, buff=0.2)
        self.play(GrowArrow(diff_arrow), Write(diff_label))
        self.wait(2)


class ParallelogramRule(Scene):
    """Parallelogram rule for vector addition"""

    def construct(self):
        # ── Title ──
        title = Text("Parallelogram Rule", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        plane = NumberPlane(
            x_range=[-1, 7, 1], y_range=[-1, 5, 1],
            x_length=8, y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1, "stroke_opacity": 0.4},
        )
        plane.move_to(DOWN * 0.3)
        self.play(Create(plane), run_time=1.5)

        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(4, 1), buff=0, color=YELLOW, stroke_width=5)
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 3), buff=0, color=GREEN, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_center(), DOWN, buff=0.15)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_center(), LEFT, buff=0.15)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.3)

        # ── Parallelogram sides ──
        v_shifted = DashedLine(plane.c2p(1, 3), plane.c2p(5, 4), color=YELLOW_D, stroke_width=3)
        w_shifted = DashedLine(plane.c2p(4, 1), plane.c2p(5, 4), color=GREEN_D, stroke_width=3)
        self.play(Create(v_shifted), Create(w_shifted))
        self.wait(0.3)

        # ── Diagonal = v + w ──
        sum_arrow = Arrow(plane.c2p(0, 0), plane.c2p(5, 4), buff=0, color=RED, stroke_width=5)
        sum_label = MathTex(r"\vec{v} + \vec{w}", font_size=32, color=RED)
        sum_label.next_to(sum_arrow.get_center(), UR, buff=0.2)
        self.play(GrowArrow(sum_arrow), Write(sum_label))
        self.wait(2)
