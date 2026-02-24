"""2.3 Cross Product — Manim Animation

Rendering examples:
    manim -pqm scenes/02_dot_cross_product/2_3_cross_product.py CrossProductFormula
    manim -pqm scenes/02_dot_cross_product/2_3_cross_product.py CrossProductArea
"""

from manim import *


class CrossProductFormula(Scene):
    """Cross product definition via determinant"""

    def construct(self):
        # ── Title ──
        title = Text("Cross Product", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Determinant form ──
        det_form = MathTex(
            r"\vec{v} \times \vec{w} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}",
            font_size=38,
        )
        det_form.move_to(UP * 1.2)
        self.play(Write(det_form))
        self.wait(0.5)

        # ── Result ──
        result = MathTex(
            r"= (v_2 w_3 - v_3 w_2)\,\vec{i} - (v_1 w_3 - v_3 w_1)\,\vec{j} + (v_1 w_2 - v_2 w_1)\,\vec{k}",
            font_size=26,
        )
        result.next_to(det_form, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(0.5)

        # ── Key property ──
        prop = MathTex(
            r"\vec{v} \times \vec{w} \;\perp\; \vec{v} \quad \text{and} \quad \vec{v} \times \vec{w} \;\perp\; \vec{w}",
            font_size=30, color=YELLOW,
        )
        prop.to_edge(DOWN, buff=0.7)
        self.play(Write(prop))
        self.wait(2)


class CrossProductArea(Scene):
    """Cross product magnitude = area of parallelogram"""

    def construct(self):
        # ── Title ──
        title = Text("Cross Product — Area", font_size=42)
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

        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(4, 1), buff=0, color=YELLOW, stroke_width=5)
        w_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 3), buff=0, color=GREEN, stroke_width=5)
        v_label = MathTex(r"\vec{v}", font_size=32, color=YELLOW)
        v_label.next_to(v_arrow.get_center(), DOWN, buff=0.15)
        w_label = MathTex(r"\vec{w}", font_size=32, color=GREEN)
        w_label.next_to(w_arrow.get_center(), LEFT, buff=0.15)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(w_arrow), Write(w_label))
        self.wait(0.3)

        # ── Parallelogram ──
        parallelogram = Polygon(
            plane.c2p(0, 0), plane.c2p(4, 1),
            plane.c2p(5, 4), plane.c2p(1, 3),
            color=PURPLE, fill_opacity=0.3, stroke_width=2,
        )
        self.play(FadeIn(parallelogram))
        self.wait(0.3)

        # ── Area formula ──
        formula = MathTex(
            r"|\vec{v} \times \vec{w}| = |\vec{v}||\vec{w}|\sin\theta = \text{Area of parallelogram}",
            font_size=28,
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)
