"""1.1 벡터란 무엇인가 — Manim 애니메이션

렌더링 예시:
    manim -pqm scenes/01_vectors/1_1_what_is_vector.py ScalarVsVector
    manim -pqm scenes/01_vectors/1_1_what_is_vector.py VectorInCoordinate
    manim -pqm scenes/01_vectors/1_1_what_is_vector.py VectorPosition

참고: LaTeX 설치 후 MathTex / include_numbers 로 전환하면 수식이 더 깔끔해집니다.
"""

from manim import *


def add_axis_labels(ax, x_range, y_range, font_size=18):
    """축에 Text 기반 숫자 라벨을 추가한다 (LaTeX 불필요)."""
    labels = VGroup()
    for x in range(int(x_range[0]), int(x_range[1]) + 1):
        if x == 0:
            continue
        lbl = Text(str(x), font_size=font_size)
        lbl.next_to(ax.c2p(x, 0), DOWN, buff=0.15)
        labels.add(lbl)
    for y in range(int(y_range[0]), int(y_range[1]) + 1):
        if y == 0:
            continue
        lbl = Text(str(y), font_size=font_size)
        lbl.next_to(ax.c2p(0, y), LEFT, buff=0.15)
        labels.add(lbl)
    return labels


class ScalarVsVector(Scene):
    """스칼라(크기만) vs 벡터(크기+방향) 비교"""

    def construct(self):
        # ── 제목 ──
        title = Text("스칼라 vs 벡터", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── 왼쪽: 스칼라 ──
        scalar_label = Text("스칼라", font_size=30, color=YELLOW)
        scalar_label.move_to(LEFT * 3.5 + UP * 2)

        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=5,
            include_numbers=False,
        )
        number_line.move_to(LEFT * 3.5 + DOWN * 0.5)

        # 수동 숫자 라벨
        nl_labels = VGroup()
        for i in range(0, 11, 2):
            lbl = Text(str(i), font_size=16)
            lbl.next_to(number_line.n2p(i), DOWN, buff=0.15)
            nl_labels.add(lbl)

        dot = Dot(number_line.n2p(5), color=YELLOW, radius=0.12)
        dot_label = Text("5", font_size=36, color=YELLOW)
        dot_label.next_to(dot, UP, buff=0.3)

        scalar_desc = Text("크기만 있다", font_size=22, color=GREY_B)
        scalar_desc.next_to(number_line, DOWN, buff=0.6)

        # ── 오른쪽: 벡터 ──
        vector_label = Text("벡터", font_size=30, color=BLUE)
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

        vec_label = Text("v", font_size=36, color=BLUE, slant=ITALIC)
        vec_label.next_to(arrow.get_center(), UL, buff=0.2)

        vector_desc = Text("크기 + 방향", font_size=22, color=GREY_B)
        vector_desc.next_to(plane, DOWN, buff=0.4)

        # ── 구분선 ──
        divider = DashedLine(UP * 3, DOWN * 3, color=GREY, dash_length=0.15)

        # ── 애니메이션 ──
        self.play(Create(divider))

        # 스칼라 쪽
        self.play(FadeIn(scalar_label))
        self.play(Create(number_line), FadeIn(nl_labels))
        self.play(FadeIn(dot), Write(dot_label))
        self.play(FadeIn(scalar_desc))
        self.wait(0.5)

        # 벡터 쪽
        self.play(FadeIn(vector_label))
        self.play(Create(plane), FadeIn(plane_labels))
        self.play(GrowArrow(arrow), Write(vec_label))
        self.play(FadeIn(vector_desc))

        self.wait(2)


class VectorInCoordinate(Scene):
    """2D 좌표평면에서 벡터와 성분 분해"""

    def construct(self):
        # ── 제목 ──
        title = Text("좌표평면에서의 벡터", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── 좌표평면 ──
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

        # ── 벡터 (3, 2) ──
        vec_arrow = Arrow(
            plane.c2p(0, 0),
            plane.c2p(3, 2),
            buff=0,
            color=YELLOW,
            stroke_width=5,
        )
        vec_label = Text("v = (3, 2)", font_size=32, color=YELLOW)
        vec_label.next_to(vec_arrow.get_end(), UR, buff=0.2)

        self.play(GrowArrow(vec_arrow), run_time=1.2)
        self.play(Write(vec_label))
        self.wait(0.5)

        # ── 성분 분해: x 성분 (점선, 빨강) ──
        x_line = DashedLine(
            plane.c2p(0, 0),
            plane.c2p(3, 0),
            color=RED,
            dash_length=0.1,
            stroke_width=3,
        )
        x_label = Text("3", font_size=28, color=RED)
        x_label.next_to(x_line, DOWN, buff=0.25)

        # ── 성분 분해: y 성분 (점선, 초록) ──
        y_line = DashedLine(
            plane.c2p(3, 0),
            plane.c2p(3, 2),
            color=GREEN,
            dash_length=0.1,
            stroke_width=3,
        )
        y_label = Text("2", font_size=28, color=GREEN)
        y_label.next_to(y_line, RIGHT, buff=0.25)

        self.play(Create(x_line), FadeIn(x_label))
        self.play(Create(y_line), FadeIn(y_label))
        self.wait(0.5)

        # ── 성분 설명 텍스트 ──
        comp_parts = VGroup(
            Text("v = (", font_size=34),
            Text("3", font_size=34, color=RED),
            Text(", ", font_size=34),
            Text("2", font_size=34, color=GREEN),
            Text(")", font_size=34),
        ).arrange(RIGHT, buff=0.05)
        comp_parts.to_edge(DOWN, buff=0.7)

        x_comp = Text("x 성분", font_size=20, color=RED)
        y_comp = Text("y 성분", font_size=20, color=GREEN)
        x_comp.next_to(comp_parts[1], DOWN, buff=0.25)
        y_comp.next_to(comp_parts[3], DOWN, buff=0.25)

        self.play(Write(comp_parts))
        self.play(FadeIn(x_comp), FadeIn(y_comp))

        self.wait(2)


class VectorPosition(Scene):
    """자유벡터: 위치가 달라도 같은 벡터"""

    def construct(self):
        # ── 제목 ──
        title = Text("자유벡터", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # ── 좌표평면 ──
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

        # ── 벡터 (3, 2)를 여러 위치에서 그리기 ──
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

        # 첫 번째 벡터 (원점)
        vec_label = Text("v = (3, 2)", font_size=30, color=YELLOW)
        vec_label.next_to(arrows[0].get_end(), UR, buff=0.15)

        self.play(GrowArrow(arrows[0]), Write(vec_label))
        self.wait(0.5)

        # 두 번째, 세 번째 벡터 (평행이동)
        self.play(GrowArrow(arrows[1]), run_time=0.8)
        self.play(GrowArrow(arrows[2]), run_time=0.8)
        self.wait(0.5)

        # ── 설명 텍스트 ──
        desc = Text(
            "시작점이 달라도 크기와 방향이 같으면\n같은 벡터이다",
            font_size=26,
            color=WHITE,
            line_spacing=1.3,
        )
        desc_bg = BackgroundRectangle(desc, color=BLACK, fill_opacity=0.8, buff=0.3)
        desc_group = VGroup(desc_bg, desc)
        desc_group.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(desc_group))
        self.wait(1)

        # ── "= 자유벡터" 강조 ──
        free_vec = Text("= 자유벡터 (Free Vector)", font_size=28, color=BLUE)
        free_bg = BackgroundRectangle(free_vec, color=BLACK, fill_opacity=0.8, buff=0.2)
        free_group = VGroup(free_bg, free_vec)
        free_group.next_to(desc_group, UP, buff=0.3)

        self.play(FadeIn(free_group))

        self.wait(2)
