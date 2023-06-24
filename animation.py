

from manim import *


class MyFirstAnimation(Scene):
    def construct(self):
        # Create basic mobjects
        square = Square(side_length=2, color=BLUE)
        label_top = Tex("b")
        label_bottom = Tex("b")
        label_left = Tex("a")
        label_right = Tex("a")

        label_top.next_to(square.get_top(), UP)
        label_bottom.next_to(square.get_bottom(), DOWN)
        label_left.next_to(square.get_left(), LEFT)
        label_right.next_to(square.get_right(), RIGHT)

        top_midpoint = square.get_edge_center(UP)
        x_coordinate = (square.get_left()[0] + square.get_right()[0]) / 2

        # make horizontal arrow
        arrow_horizontal = Arrow([x_coordinate, top_midpoint[1], 0], [x_coordinate, top_midpoint[1], 0], buff=0)
        arrow_horizontal.next_to(square, UP, buff=0)
        self.add(square, arrow_horizontal)
        self.add(square, label_top, label_bottom, label_left, label_right)
        #Randy
        # Animate Fade in of the star that takes 2 seconds
        self.play(FadeIn(square, run_time=2))
        # Wait for a second
        self.wait()
