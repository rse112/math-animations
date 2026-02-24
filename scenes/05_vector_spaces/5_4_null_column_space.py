"""5.4 Null Space and Column Space — Manim Animation

Rendering examples:
    manim -pqm scenes/05_vector_spaces/5_4_null_column_space.py NullSpaceViz
    manim -pqm scenes/05_vector_spaces/5_4_null_column_space.py ColumnSpaceViz
"""

from manim import *


class NullSpaceViz(Scene):
    """Null space: all x such that Ax = 0"""

    def construct(self):
        # ── Title ──
        title = Text("Null Space", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Definition ──
        defn = MathTex(
            r"\text{Null}(A) = \{\vec{x} \mid A\vec{x} = \vec{0}\}",
            font_size=40,
        )
        defn.move_to(UP * 1.5)
        self.play(Write(defn))
        self.wait(0.5)

        # ── Example ──
        mat = MathTex(
            r"A = \begin{pmatrix}1 & 2 \\ 2 & 4\end{pmatrix}",
            font_size=34,
        )
        mat.move_to(LEFT * 2 + DOWN * 0.2)
        self.play(Write(mat))
        self.wait(0.3)

        null_eq = MathTex(
            r"A\vec{x} = \vec{0} \;\Rightarrow\; x_1 + 2x_2 = 0",
            font_size=30, color=YELLOW,
        )
        null_eq.move_to(RIGHT * 2.5 + DOWN * 0.2)
        self.play(Write(null_eq))
        self.wait(0.3)

        null_result = MathTex(
            r"\text{Null}(A) = \text{span}\!\left(\begin{pmatrix}-2\\1\end{pmatrix}\right)",
            font_size=32,
        )
        null_result.to_edge(DOWN, buff=0.8)
        self.play(Write(null_result))

        # ── Rank-nullity ──
        rn = MathTex(
            r"\text{rank}(A) + \text{nullity}(A) = n",
            font_size=30, color=BLUE_B,
        )
        rn.next_to(null_result, UP, buff=0.4)
        self.play(Write(rn))
        self.wait(2)


class ColumnSpaceViz(Scene):
    """Column space: all possible outputs Ax"""

    def construct(self):
        # ── Title ──
        title = Text("Column Space", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Definition ──
        defn = MathTex(
            r"\text{Col}(A) = \{A\vec{x} \mid \vec{x} \in \mathbb{R}^n\} = \text{span of columns of } A",
            font_size=28,
        )
        defn.move_to(UP * 1.8)
        self.play(Write(defn))
        self.wait(0.5)

        # ── Example ──
        mat = MathTex(
            r"A = \begin{pmatrix}1 & 3 \\ 2 & 6\end{pmatrix}"
            r"= \begin{bmatrix}\vec{a}_1 & \vec{a}_2\end{bmatrix}",
            font_size=34,
        )
        mat.move_to(UP * 0.2)
        self.play(Write(mat))
        self.wait(0.3)

        # ── Column 2 = 3 * Column 1 ──
        dep = MathTex(
            r"\vec{a}_2 = 3\vec{a}_1 \;\Rightarrow\; \text{Col}(A) = \text{span}(\vec{a}_1)",
            font_size=30, color=YELLOW,
        )
        dep.move_to(DOWN * 0.8)
        self.play(Write(dep))
        self.wait(0.3)

        result = MathTex(
            r"\text{Col}(A) = \text{line in } \mathbb{R}^2,\quad \dim = 1",
            font_size=30,
        )
        result.to_edge(DOWN, buff=0.7)
        self.play(Write(result))
        self.wait(2)
