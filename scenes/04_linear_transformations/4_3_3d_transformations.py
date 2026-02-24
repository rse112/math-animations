"""4.3 3D Transformations — Manim Animation

Rendering examples:
    manim -pqm scenes/04_linear_transformations/4_3_3d_transformations.py RotationMatrices3D
    manim -pqm scenes/04_linear_transformations/4_3_3d_transformations.py ScalingMatrix3D
"""

from manim import *


class RotationMatrices3D(Scene):
    """3D rotation matrices about each axis"""

    def construct(self):
        # ── Title ──
        title = Text("3D Rotation Matrices", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Rx ──
        Rx = MathTex(
            r"R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}",
            font_size=28, color=RED_B,
        )
        Rx.move_to(LEFT * 3 + UP * 0.5)

        # ── Ry ──
        Ry = MathTex(
            r"R_y(\theta) = \begin{pmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{pmatrix}",
            font_size=28, color=GREEN_B,
        )
        Ry.move_to(RIGHT * 3 + UP * 0.5)

        # ── Rz ──
        Rz = MathTex(
            r"R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}",
            font_size=28, color=BLUE_B,
        )
        Rz.to_edge(DOWN, buff=0.5)

        self.play(Write(Rx))
        self.wait(0.3)
        self.play(Write(Ry))
        self.wait(0.3)
        self.play(Write(Rz))
        self.wait(2)


class ScalingMatrix3D(Scene):
    """3D scaling transformation"""

    def construct(self):
        # ── Title ──
        title = Text("3D Scaling", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── Scaling matrix ──
        scale = MathTex(
            r"S = \begin{pmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{pmatrix}",
            font_size=44,
        )
        scale.move_to(UP * 0.8)
        self.play(Write(scale))
        self.wait(0.5)

        # ── Example ──
        example = MathTex(
            r"S\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}s_x x\\s_y y\\s_z z\end{pmatrix}",
            font_size=36,
        )
        example.to_edge(DOWN, buff=0.9)
        self.play(Write(example))

        # ── Note ──
        note = MathTex(r"s_i = 1 \Rightarrow \text{no change on that axis}", font_size=28, color=GREY_B)
        note.next_to(example, UP, buff=0.4)
        self.play(Write(note))
        self.wait(2)
