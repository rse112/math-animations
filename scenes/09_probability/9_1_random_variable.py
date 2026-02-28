"""9.1 Random Variable — Manim Animation

확률변수, 확률실험, 표본공간에 대한 애니메이션

Rendering examples:
    manim -pqm scenes/09_probability/9_1_random_variable.py RandomExperiment
    manim -pqm scenes/09_probability/9_1_random_variable.py SampleSpace
"""

from manim import *
import random


class RandomExperiment(Scene):
    """확률실험: 주사위를 던져서 결과를 예측할 수 없는 실험"""

    def construct(self):
        title = Text("확률실험 (Random Experiment)", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 주사위 표현
        dice = Square(side_length=1.5, color=WHITE)
        dice.shift(UP * 0.5)

        dots_configs = {
            1: [(0, 0)],
            2: [(-0.3, 0.3), (0.3, -0.3)],
            3: [(-0.3, 0.3), (0, 0), (0.3, -0.3)],
            4: [(-0.3, 0.3), (0.3, 0.3), (-0.3, -0.3), (0.3, -0.3)],
            5: [(-0.3, 0.3), (0.3, 0.3), (0, 0), (-0.3, -0.3), (0.3, -0.3)],
            6: [(-0.3, 0.3), (0.3, 0.3), (-0.3, 0), (0.3, 0), (-0.3, -0.3), (0.3, -0.3)],
        }

        self.play(Create(dice))

        result_text = Text("결과: ?", font_size=28, color=YELLOW)
        result_text.next_to(dice, DOWN, buff=0.8)
        self.play(Write(result_text))

        # 주사위 굴리기 애니메이션 (여러 번)
        for trial in range(5):
            face = random.randint(1, 6)
            dots = VGroup()
            for dx, dy in dots_configs[face]:
                dot = Dot(
                    point=dice.get_center() + np.array([dx, dy, 0]),
                    radius=0.1,
                    color=BLUE,
                )
                dots.add(dot)

            self.play(
                Rotate(dice, angle=PI / 2, run_time=0.3),
                FadeOut(result_text),
            )

            new_result = Text(f"결과: {face}", font_size=28, color=YELLOW)
            new_result.next_to(dice, DOWN, buff=0.8)

            self.play(FadeIn(dots), FadeIn(new_result), run_time=0.4)
            self.wait(0.5)

            if trial < 4:
                self.play(FadeOut(dots), run_time=0.2)
                result_text = new_result

        # 결론
        conclusion = Text(
            "같은 조건에서 반복해도\n결과를 예측할 수 없다",
            font_size=24,
            color=GREEN,
        )
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)


class SampleSpace(Scene):
    """표본공간: 주사위 2번 던지기의 모든 가능한 결과"""

    def construct(self):
        title = Text("표본공간 (Sample Space)", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        subtitle = Text("주사위 2번 던지기", font_size=24, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # 6x6 격자로 표본공간 표현
        grid = VGroup()
        cell_size = 0.7
        start_x = -2.5
        start_y = 1.5

        for i in range(6):
            for j in range(6):
                cell = Square(side_length=cell_size, stroke_width=1, color=BLUE_C)
                cell.move_to(
                    np.array(
                        [
                            start_x + j * cell_size,
                            start_y - i * cell_size,
                            0,
                        ]
                    )
                )
                label = Text(f"({i+1},{j+1})", font_size=10)
                label.move_to(cell.get_center())
                grid.add(VGroup(cell, label))

        # 축 레이블
        first_label = Text("첫번째 주사위", font_size=18)
        first_label.next_to(grid, LEFT, buff=0.5).shift(UP * 0.3)
        first_label.rotate(PI / 2)

        second_label = Text("두번째 주사위", font_size=18)
        second_label.next_to(grid, DOWN, buff=0.3)

        self.play(Write(first_label), Write(second_label))
        self.play(LaggedStart(*[FadeIn(cell, scale=0.5) for cell in grid], lag_ratio=0.02))
        self.wait(0.5)

        # 총 개수 표시
        count_text = MathTex(r"|\Omega| = 6 \times 6 = 36", font_size=32, color=GREEN)
        count_text.to_edge(DOWN, buff=0.5)
        self.play(Write(count_text))
        self.wait(2)
