from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Tanvi Khadap \n Welcome to Manim", font_size=50)
        text.scale(2)
        # text.to_edge(MIDDLE)

        self.play(Write(text, run_time=5))
        self.wait(2)
