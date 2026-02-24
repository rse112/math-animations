"""1.1 What is a Vector? — Manim Animation

Rendering examples:
    manim -pqm scenes/01_vectors/1_1_what_is_vector.py ScalarVsVector
    manim -pqm scenes/01_vectors/1_1_what_is_vector.py VectorInCoordinate
    manim -pqm scenes/01_vectors/1_1_what_is_vector.py VectorPosition
"""

from manim import *


def add_axis_labels(ax, x_range, y_range, font_size=18):
    """Add MathTex-based number labels to axes."""
    labels = VGroup()
    for x in range(int(x_range[0]), int(x_range[1]) + 1):
        if x == 0:
            continue
        lbl = MathTex(str(x), font_size=font_size)
        lbl.next_to(ax.c2p(x, 0), DOWN, buff=0.15)
        labels.add(lbl)
    for y in range(int(y_range[0]), int(y_range[1]) + 1):
        if y == 0:
            continue
        lbl = MathTex(str(y), font_size=font_size)
        lbl.next_to(ax.c2p(0, y), LEFT, buff=0.15)
        labels.add(lbl)
    return labels


class ScalarVsVector(Scene):
    """Scalar (magnitude only) vs Vector (magnitude + direction)"""

    def construct(self):
        # ── Title ──
        title = Text("Scalar vs Vector", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Left: Scalar ──
        scalar_label = Text("Scalar", font_size=30, color=YELLOW)
        scalar_label.move_to(LEFT * 3.5 + UP * 2)

        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=5,
            include_numbers=False,
        )
        number_line.move_to(LEFT * 3.5 + DOWN * 0.5)

        # Manual number labels
        nl_labels = VGroup()
        for i in range(0, 11, 2):
            lbl = MathTex(str(i), font_size=16)
            lbl.next_to(number_line.n2p(i), DOWN, buff=0.15)
            nl_labels.add(lbl)

        dot = Dot(number_line.n2p(5), color=YELLOW, radius=0.12)
        dot_label = MathTex("5", font_size=36, color=YELLOW)
        dot_label.next_to(dot, UP, buff=0.3)


        # ── Right: Vector ──
        vector_label = Text("Vector", font_size=30, color=BLUE)
        vector_label.move_to(RIGHT * 3.5 + UP * 2)

        plane = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=3.5,
            axis_config={"include_numbers": False},
        )
        plane.move_to(RIGHT * 3.5 + DOWN * 0.3)

        plane_labels = add_axis_labels(
            plane, [-1, 5], [-1, 4], font_size=14
        )

        arrow = Arrow(
            plane.c2p(0, 0),
            plane.c2p(3, 2),
            buff=0,
            color=BLUE,
            stroke_width=5,
        )

        vec_label = MathTex(r"\vec{v}", font_size=36, color=BLUE)
        vec_label.next_to(arrow.get_center(), UL, buff=0.2)


        # ── Divider ──
        divider = DashedLine(UP * 3, DOWN * 3, color=GREY, dash_length=0.15)

        # ── Animation ──
        self.play(Create(divider))

        # Scalar side
        self.play(FadeIn(scalar_label))
        self.play(Create(number_line), FadeIn(nl_labels))
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(0.5)

        # Vector side
        self.play(FadeIn(vector_label))
        self.play(Create(plane), FadeIn(plane_labels))
        self.play(GrowArrow(arrow), Write(vec_label))

        self.wait(2)


class VectorInCoordinate(Scene):
    """Vector and component decomposition in 2D coordinate plane"""

    def construct(self):
        # ── Title ──
        title = Text("Vector in Coordinate Plane", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Coordinate plane ──
        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False},
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
        )
        plane.move_to(DOWN * 0.3)

        plane_labels = add_axis_labels(
            plane, [-1, 5], [-1, 4], font_size=18
        )

        self.play(Create(plane), FadeIn(plane_labels), run_time=1.5)

        # ── Vector (3, 2) ──
        vec_arrow = Arrow(
            plane.c2p(0, 0),
            plane.c2p(3, 2),
            buff=0,
            color=YELLOW,
            stroke_width=5,
        )
        vec_label = MathTex(r"\vec{v} = (3,\ 2)", font_size=32, color=YELLOW)
        vec_label.next_to(vec_arrow.get_end(), UR, buff=0.2)

        self.play(GrowArrow(vec_arrow), run_time=1.2)
        self.play(Write(vec_label))
        self.wait(0.5)

        # ── Component decomposition: x component (dashed, red) ──
        x_line = DashedLine(
            plane.c2p(0, 0),
            plane.c2p(3, 0),
            color=RED,
            dash_length=0.1,
            stroke_width=3,
        )
        x_label = MathTex("3", font_size=28, color=RED)
        x_label.next_to(x_line, DOWN, buff=0.25)

        # ── Component decomposition: y component (dashed, green) ──
        y_line = DashedLine(
            plane.c2p(3, 0),
            plane.c2p(3, 2),
            color=GREEN,
            dash_length=0.1,
            stroke_width=3,
        )
        y_label = MathTex("2", font_size=28, color=GREEN)
        y_label.next_to(y_line, RIGHT, buff=0.25)

        self.play(Create(x_line), FadeIn(x_label))
        self.play(Create(y_line), FadeIn(y_label))
        self.wait(0.5)

        # ── Component label text ──
        comp_parts = MathTex(
            r"\vec{v} = (", r"3", r",\;", r"2", r")",
            font_size=34,
        )
        comp_parts[1].set_color(RED)
        comp_parts[3].set_color(GREEN)
        comp_parts.to_edge(DOWN, buff=0.7)

        self.play(Write(comp_parts))

        self.wait(2)


class VectorPosition(Scene):
    """Free Vector: same vector regardless of starting position"""

    def construct(self):
        # ── Title ──
        title = Text("Free Vector", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Coordinate plane ──
        plane = NumberPlane(
            x_range=[-2, 6, 1],
            y_range=[-2, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": False},
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
        )
        plane.move_to(DOWN * 0.2)

        plane_labels = add_axis_labels(
            plane, [-2, 6], [-2, 5], font_size=16
        )

        self.play(Create(plane), FadeIn(plane_labels), run_time=1.5)

        # ── Draw vector (3, 2) at multiple positions ──
        start_points = [(0, 0), (-1, -1), (2, 1)]
        colors = [YELLOW, GREEN, RED]
        arrows = []

        for start, color in zip(start_points, colors):
            end = (start[0] + 3, start[1] + 2)
            arrow = Arrow(
                plane.c2p(*start),
                plane.c2p(*end),
                buff=0,
                color=color,
                stroke_width=4,
            )
            arrows.append(arrow)

        # First vector (origin)
        vec_label = MathTex(r"\vec{v} = (3,\ 2)", font_size=30, color=YELLOW)
        vec_label.next_to(arrows[0].get_end(), UR, buff=0.15)

        self.play(GrowArrow(arrows[0]), Write(vec_label))
        self.wait(0.5)

        # Second and third vectors (translated)
        self.play(GrowArrow(arrows[1]), run_time=0.8)
        self.play(GrowArrow(arrows[2]), run_time=0.8)
        self.wait(0.5)

        self.wait(2)
