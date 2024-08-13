from manim import*

class IncendioCampo(Scene):
    def construct(self):

        # Título
        title = Text("Taxa de Aumento da Área de um Incêndio").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        # Escrevendo a Questão:
        question = [Text("Um incêndio em um campo aberto se alastra em forma de círculo.").scale(0.55),
                    Text("O raio do círculo aumenta à razão de 0,5 m/min.", t2c={"0,5 m/min":BLUE}).scale(0.55), 
                    Text("Determine a taxa à qual a área incendiada está aumentando").scale(0.55),
                    Text("quando o raio é de 12 m.", t2c={"12 m":GREEN}).scale(0.55)]

        question[0].next_to(title, DOWN*5)
        self.play(Write(question[0]))

        for i in range(1, len(question)):
            question[i].next_to(question[i-1], DOWN)
            self.play(Write(question[i]))

        self.wait(6)

        self.play(FadeOut(title), FadeOut(question[0]), FadeOut(question[1]), FadeOut(question[2]), FadeOut(question[3]))

        self.wait(1)

        # Desenhando a representação
        title = Text("Incêndio")
        title.to_edge(UP)
        self.play(Write(title))

        self.wait(1)

        fire = Circle(radius=0.1, color=RED).set_fill(RED, opacity=0.6)
        fire.move_to(ORIGIN)

        self.play(Create(fire))
        self.wait(0.5)
        self.play(fire.animate.scale(20), run_time=2)
        self.wait(1)

        radius = Line(start=ORIGIN, end=fire.get_right(), color=BLACK, stroke_width=6)
        self.play(Write(radius))
        self.wait(1)

        text_radius = MathTex("12m").scale(1.4)
        text_radius.next_to(radius, UP)
        self.play(Write(text_radius), run_time=1)

        self.wait(3)

        self.play(FadeOut(title), FadeOut(radius), FadeOut(fire), FadeOut(text_radius))

        self.wait(1)

        # Definindo as variáveis e resolvendo o problema
        title = Text("Resolução")
        title.to_edge(UP)
        self.play(Write(title))

        self.wait(1)

        variables1 = MathTex(r"\frac{dr}{dt} = 0.5 \, \text{m/min}", color=BLUE).scale(0.8)
        variables2 = MathTex(r"\, r = 12 \, \text{m}", color=GREEN).scale(0.8)

        variables1.next_to(title, DOWN).shift(LEFT * 2)
        variables2.next_to(variables1, RIGHT).shift(RIGHT * 1)

        self.play(Write(variables1))
        self.play(Write(variables2))

        self.wait(2)

        # Fórmula da área do círculo
        area_formula = MathTex(r"A = \pi r^2").scale(0.8)
        area_formula.next_to(title, DOWN).shift(DOWN*1.3)
        self.play(Write(area_formula))

        self.wait(3)

        # Derivada da área em relação ao tempo
        area_derivada = MathTex(r"\frac{dA}{dt} =", r"\frac{d}{dt} (\pi r^2)")
        area_derivada2 = MathTex(r"\frac{dA}{dt} =", r"2\pi", r"r", r"\frac{dr}{dt}")
        area_derivada2[2].set_color(GREEN)
        area_derivada2[3].set_color(BLUE)

        area_derivada.next_to(area_formula, DOWN).shift(DOWN*0.8)
        area_derivada2.next_to(area_formula, DOWN).shift(DOWN*0.8)

        self.play(Write(area_derivada))
        self.wait(3)
        
        self.play(Transform(area_derivada, area_derivada2))

        valores = MathTex(r"\frac{dA}{dt} =", r"2\pi (12) (0.5) = 12\pi \, \text{m}^2/\text{min}").scale(0.8)
        self.wait(3)

        # Substituindo os valores
        area_derivada3 = MathTex(r"\frac{dA}{dt} =", r"2\pi", r"(12)", r"(0.5)")
        area_derivada3[2].set_color(GREEN)
        area_derivada3[3].set_color(BLUE)

        area_derivada3.next_to(area_formula, DOWN).shift(DOWN*0.8)
        
        self.play(Transform(area_derivada, area_derivada3))
        self.wait(3)

        area_derivada4 = MathTex(r"\frac{dA}{dt} =", r"12\pi")

        area_derivada4.next_to(area_formula, DOWN).shift(DOWN*0.8)
        
        self.play(Transform(area_derivada, area_derivada4))
        self.wait(3)

        # Conclusão
        conclusao = Text("A taxa de aumento da área é de 12π m²/min").scale(0.6).set_color(RED)
        conclusao.next_to(area_derivada, DOWN).shift(DOWN*0.6)
        self.play(Write(conclusao))

        self.wait(6)