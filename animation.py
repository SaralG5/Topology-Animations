from manim import *

class MyFirstAnimation(Scene):
    def construct(self):
        # Create basic mobjects
        square = Square()
        label_top = Tex("b")
        label_bottom = Tex("b")
        label_left = Tex("a")
        label_right = Tex("a")

        label_top.next_to(square.get_top(), UP)
        label_bottom.next_to(square.get_bottom(), DOWN)
        label_left.next_to(square.get_left(), LEFT)
        label_right.next_to(square.get_right(), RIGHT)

        self.add(square,label_top, label_bottom, label_left, label_right)

        # Animate Fade in of the star that takes 2 seconds
        self.play(FadeIn(square, run_time=2))
        # Wait for a second
        self.wait()
