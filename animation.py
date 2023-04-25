from manim import *

class MyFirstAnimation(Scene):
    def construct(self):
        # Create basic mobjects
        square = Square()

        # Animate Fade in of the star that takes 2 seconds
        self.play(FadeIn(square, run_time=2))
        # Wait for a second
        self.wait()
