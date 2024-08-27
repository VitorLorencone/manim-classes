from manim import*

class Main(Scene):
    def construct(self):
        # Título
        title = Text("Área entre curvas", weight=BOLD).scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))

        # Escrevendo a Questão:
        question = [Text("Calcule a área entre as curvas").scale(0.75),
                    Text("y = x", t2c={"y = x":BLUE}).scale(0.75), 
                    Text("y = 5x - x²", t2c={"y = 5x - x²":RED}).scale(0.75)]

        question[0].next_to(title, DOWN*5)
        self.play(Write(question[0]))

        for i in range(1, len(question)):
            question[i].next_to(question[i-1], DOWN*2)
            self.play(Write(question[i]))

        self.wait(3)
        self.play(FadeOut(title), FadeOut(question[0]), FadeOut(question[1]), FadeOut(question[2]))
        self.wait(1)

        # Criando o plano cartesiano
        plano = NumberPlane(x_range=[-1, 6, 1], y_range=[-3, 7, 1], background_line_style={"stroke_opacity":0.3}).scale(0.6)
        
        # Desenhando a reta y = x
        r1 = plano.plot(lambda x: x, color=BLUE, x_range=[-1, 6])
        labelR1 = MathTex("y = x").next_to(r1, RIGHT, buff=0.5).set_color(BLUE)

        # Desenhando a parábola y = 5x - x^2
        r2 = plano.plot(lambda x: 5*x - x**2, color=RED, x_range=[-0.5, 5.5])
        labelR2 = MathTex("y = 5x - x^2").move_to(UP + RIGHT*3.9).set_color(RED)
        
        # Adicionando os elementos à cena
        self.play(Create(plano, run_time=2))
        self.wait(0.5)
        self.play(Create(r1, run_time=1), Write(labelR1, run_time=1))
        self.wait(0.5)
        self.play(Create(r2, run_time=1), Write(labelR2, run_time=1))
        
        # Manter a cena por alguns segundos
        self.wait(2)

        # Ponto entre as curvas
        d1 = MathTex("x = 5x - x^2").move_to(DOWN*0.8 + RIGHT*4.2)
        d2 = MathTex("x = 0").next_to(d1, DOWN)
        d3 = MathTex("x = 4").next_to(d2, DOWN)

        dot2 = Dot(plano.c2p(0, 0))
        dot2L = MathTex("(0,0)").next_to(dot2, LEFT, buff=0.2).scale(0.8)

        dot3 = Dot(plano.c2p(4, 4))
        dot3L = MathTex("(4,4)").next_to(dot3, RIGHT, buff=0.2).scale(0.8)

        self.play(Write(d1, run_time = 1))
        self.wait(2)
        self.play(Transform(d1,d2), Write(d3))
        self.wait(2)
        self.play(Transform(d1, dot2), Transform(d3, dot3))
        self.play(Write(dot2L), Write(dot3L))
        self.wait(2)

        # Área entre os gráficos
        area2 = plano.get_area(
            graph=r2,  # Curva superior (y = 5x - x^2)
            x_range=[0, 4],  # Intervalo de x para preencher
            color=YELLOW,  # Cor da área preenchida
            opacity=0.5  # Opacidade da área preenchida
        )

        a2 = MathTex("A2 = \int_0^4 5x-x^2 dx").set_color(YELLOW).move_to(LEFT*4.5 + UP*2.5)
        a1 = MathTex("A1 = \int_0^4 x dx").set_color(PINK).next_to(a2,DOWN)

        area1 = plano.get_area(
            graph=r1,  # Curva superior (y = 5x - x^2)
            x_range=[0, 4],  # Intervalo de x para preencher
            color=PINK,  # Cor da área preenchida
            opacity=0.5  # Opacidade da área preenchida
        )

        # Diferença entre áreas
        area3 = Difference(area2,area1,color=GREEN,fill_opacity=0.75)
        a3 = MathTex("A = A2 - A1").set_color(GREEN).next_to(a1, DOWN*6)
        a3_2 = MathTex("A = int_0^4 5x - x^2 - x dx")
        a3_3 = MathTex("A = int_0^4 4x - x^2 dx")

        self.play(FadeIn(area2,run_time=1), Write(a2),run_time = 1)
        self.wait(2)
        self.play(FadeIn(area1,run_time=1), Write(a1),run_time = 1)
        self.wait(2)
        self.play(Transform(area2, area3,run_time=1.0), Transform(area1, area3,run_time=1.0), Write(a3), run_time = 1)
        self.wait(2)
        self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        self.wait(1)

        # Conclusão e cálculo final
        a3 = MathTex("A = A2 - A1").set_color(GREEN)
        a3_1 = MathTex("A = \int_0^4 5x - x^2 dx - \int_0^4 x dx")
        a3_2 = MathTex("A = \int_0^4 5x - x^2 - x dx")
        a3_3 = MathTex("A = \int_0^4 4x - x^2 dx")
        a3_4 = MathTex(r"A = \left. 2x^2 - \frac{x^3}{3} \right|_{0}^{4}")
        a3_5 = MathTex(r"A = 32 - \frac{64}{3}")
        a3_6 = MathTex(r"A = \frac{32}{3}")
        a4 = Text("Logo, a área entre os gráficos é de 32/3 u²").scale(0.6)

        self.play(Write(a3))
        self.wait(2)
        self.play(Transform(a3, a3_1))
        self.wait(2.5)
        self.play(Transform(a3, a3_2))
        self.wait(2.5)
        self.play(Transform(a3, a3_3))
        self.wait(2.5)
        self.play(Transform(a3, a3_4))
        self.wait(2.5)
        self.play(Transform(a3, a3_5))
        self.wait(2.5)
        self.play(Transform(a3, a3_6))
        self.wait(2.5)
        self.play(Transform(a3, a4), run_time=1)
        self.wait(5)

class Intro(Scene):
    def construct(self):
        # Título
        title = Text("Área entre curvas", weight=BOLD).scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))

        # Escrevendo a Questão:
        question = [Text("Calcule a área entre as curvas").scale(0.75),
                    Text("y = x", t2c={"y = x":BLUE}).scale(0.75), 
                    Text("y = 5x - x²", t2c={"y = 5x - x²":RED}).scale(0.75)]

        question[0].next_to(title, DOWN*5)
        self.play(Write(question[0]))

        for i in range(1, len(question)):
            question[i].next_to(question[i-1], DOWN*2)
            self.play(Write(question[i]))

        self.wait(6)

        self.play(FadeOut(title), FadeOut(question[0]), FadeOut(question[1]), FadeOut(question[2]))

        self.wait(1)

class Draw(Scene):
    def construct(self):
        # Criando o plano cartesiano
        plano = NumberPlane(x_range=[-1, 6, 1], y_range=[-3, 7, 1], background_line_style={"stroke_opacity":0.3}).scale(0.6)
        
        # Desenhando a reta y = x
        r1 = plano.plot(lambda x: x, color=BLUE, x_range=[-1, 6])
        labelR1 = MathTex("y = x").next_to(r1, RIGHT, buff=0.5).set_color(BLUE)

        # Desenhando a parábola y = 5x - x^2
        r2 = plano.plot(lambda x: 5*x - x**2, color=RED, x_range=[-0.5, 5.5])
        labelR2 = MathTex("y = 5x - x^2").move_to(UP + RIGHT*3.9).set_color(RED)
        
        # Adicionando os elementos à cena
        self.play(Create(plano, run_time=2))
        self.wait(0.5)
        self.play(Create(r1, run_time=1), Write(labelR1, run_time=1))
        self.wait(0.5)
        self.play(Create(r2, run_time=1), Write(labelR2, run_time=1))
        
        # Manter a cena por alguns segundos
        self.wait(2)

        # Ponto entre as curvas
        d1 = MathTex("x = 5x - x^2").move_to(DOWN*0.8 + RIGHT*4.2)
        d2 = MathTex("x = 0").next_to(d1, DOWN)
        d3 = MathTex("x = 4").next_to(d2, DOWN)

        dot2 = Dot(plano.c2p(0, 0))
        dot2L = MathTex("(0,0)").next_to(dot2, LEFT, buff=0.2).scale(0.8)

        dot3 = Dot(plano.c2p(4, 4))
        dot3L = MathTex("(4,4)").next_to(dot3, RIGHT, buff=0.2).scale(0.8)

        self.play(Write(d1, run_time = 1))
        self.wait(2)
        self.play(Transform(d1,d2), Write(d3))
        self.wait(2)
        self.play(Transform(d1, dot2), Transform(d3, dot3))
        self.play(Write(dot2L), Write(dot3L))
        self.wait(2)

        # Área entre os gráficos

        area2 = plano.get_area(
            graph=r2,  # Curva superior (y = 5x - x^2)
            x_range=[0, 4],  # Intervalo de x para preencher
            color=YELLOW,  # Cor da área preenchida
            opacity=0.5  # Opacidade da área preenchida
        )

        a2 = MathTex("A2 = \int_0^4 5x-x^2 dx").set_color(YELLOW).move_to(LEFT*4.5 + UP*2.5)
        a1 = MathTex("A1 = \int_0^4 x dx").set_color(PINK).next_to(a2,DOWN)

        area1 = plano.get_area(
            graph=r1,  # Curva superior (y = 5x - x^2)
            x_range=[0, 4],  # Intervalo de x para preencher
            color=PINK,  # Cor da área preenchida
            opacity=0.5  # Opacidade da área preenchida
        )

        area3 = Difference(area2,area1,color=GREEN,fill_opacity=0.75)
        a3 = MathTex("A = A2 - A1").set_color(GREEN).next_to(a1, DOWN*6)
        a3_2 = MathTex("A = int_0^4 5x - x^2 - x dx")
        a3_3 = MathTex("A = int_0^4 4x - x^2 dx")

        self.play(FadeIn(area2,run_time=1), Write(a2),run_time = 1)
        self.wait(2)
        self.play(FadeIn(area1,run_time=1), Write(a1),run_time = 1)
        self.wait(2)
        self.play(Transform(area2, area3,run_time=1.0), Transform(area1, area3,run_time=1.0), Write(a3), run_time = 1)
        self.wait(2)
        self.play(*[FadeOut(mobject) for mobject in self.mobjects])

class End(Scene):
    def construct(self):
        a3 = MathTex("A = A2 - A1").set_color(GREEN)
        a3_1 = MathTex("A = \int_0^4 5x - x^2 dx - \int_0^4 x dx")
        a3_2 = MathTex("A = \int_0^4 5x - x^2 - x dx")
        a3_3 = MathTex("A = \int_0^4 4x - x^2 dx")
        a3_4 = MathTex(r"A = \left. 2x^2 - \frac{x^3}{3} \right|_{0}^{4}")
        a3_5 = MathTex(r"A = 32 - \frac{64}{3}")
        a3_6 = MathTex(r"A = \frac{32}{3}")

        self.play(Write(a3))
        self.wait(2)
        self.play(Transform(a3, a3_1))
        self.wait(2.5)
        self.play(Transform(a3, a3_2))
        self.wait(2.5)
        self.play(Transform(a3, a3_3))
        self.wait(2.5)
        self.play(Transform(a3, a3_4))
        self.wait(2.5)
        self.play(Transform(a3, a3_5))
        self.wait(2.5)
        self.play(Transform(a3, a3_6))
        self.wait(5)