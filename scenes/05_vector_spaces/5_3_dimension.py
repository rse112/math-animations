"""5.3 Dimension — Manim Animation

Rendering examples:
    manim -pqm scenes/05_vector_spaces/5_3_dimension.py DimensionExamples
"""

from manim import *


class DimensionExamples(Scene):
    """Dimension of different vector spaces"""

    def construct(self):
        # ── Title ──
        title = Text("Dimension", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Definition ──
        defn = MathTex(
            r"\dim(V) = \text{number of vectors in any basis of } V",
            font_size=30, color=GREY_B,
        )
        defn.move_to(UP * 2)
        self.play(Write(defn))
        self.wait(0.5)

        # ── Examples table ──
        examples = VGroup(
            MathTex(r"\{0\}", font_size=32, color=WHITE),
            MathTex(r"\dim = 0", font_size=32, color=YELLOW),
            MathTex(r"\text{line through origin}", font_size=28, color=WHITE),
            MathTex(r"\dim = 1", font_size=32, color=YELLOW),
            MathTex(r"\mathbb{R}^2 \text{ plane}", font_size=28, color=WHITE),
            MathTex(r"\dim = 2", font_size=32, color=YELLOW),
            MathTex(r"\mathbb{R}^3", font_size=32, color=WHITE),
            MathTex(r"\dim = 3", font_size=32, color=YELLOW),
        )

        rows = VGroup()
        for i in range(0, 8, 2):
            row = VGroup(examples[i], examples[i + 1]).arrange(RIGHT, buff=1.5)
            rows.add(row)

        rows.arrange(DOWN, buff=0.45)
        rows.move_to(DOWN * 0.3)
        self.play(Write(rows))
        self.wait(2)
