"""6.2 Characteristic Equation — Manim Animation

Rendering examples:
    manim -pqm scenes/06_eigenvalues_eigenvectors/6_2_characteristic_equation.py CharacteristicEquation
"""

from manim import *


class CharacteristicEquation(Scene):
    """Deriving eigenvalues from det(A - λI) = 0"""

    def construct(self):
        # ── Title ──
        title = Text("Characteristic Equation", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Derivation steps ──
        step1 = MathTex(r"A\vec{v} = \lambda\vec{v}", font_size=36)
        step2 = MathTex(r"A\vec{v} - \lambda I\vec{v} = \vec{0}", font_size=36)
        step3 = MathTex(r"(A - \lambda I)\vec{v} = \vec{0}", font_size=36)
        step4 = MathTex(r"\det(A - \lambda I) = 0", font_size=40, color=YELLOW)

        steps = VGroup(step1, step2, step3, step4).arrange(DOWN, buff=0.5)
        steps.move_to(UP * 0.3)

        for step in steps:
            self.play(Write(step))
            self.wait(0.4)

        self.wait(0.5)

        # ── Example: 2x2 matrix ──
        example = MathTex(
            r"A = \begin{pmatrix}4&1\\2&3\end{pmatrix}"
            r"\;\Rightarrow\; \det\begin{pmatrix}4-\lambda&1\\2&3-\lambda\end{pmatrix} = 0",
            font_size=28,
        )
        example.to_edge(DOWN, buff=0.7)
        self.play(Write(example))
        self.wait(0.5)

        result = MathTex(
            r"(4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0"
            r"\;\Rightarrow\; \lambda = 5,\; \lambda = 2",
            font_size=26, color=GREEN,
        )
        result.next_to(example, UP, buff=0.3)
        self.play(Write(result))
        self.wait(2)
