from pplay.window import *
from pplay.sprite import *
from math import cos, sin
from random import choice
import numpy as np

fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")

circulo = Sprite("assets\\sprites\\roda_alavanca.png")
circulo.set_position(580, 320)

aro = Sprite("assets\\sprites\\aro_alavanca.png")

velocidades = np.random.choice((2,3,4,5,6), size=5, replace=True)
print(velocidades)

class Alavanca():
    def __init__(self, janela, pos):

        self.velocidade = choice(velocidades)
        print(self.velocidade)
        self.janela = janela
        
        self.objeto = Sprite("assets\\sprites\\roda_alavanca.png")
        self.percurso = Sprite("assets\\sprites\\aro_alavanca.png")
        self.percurso.set_position(pos[0] - 100, pos[1] - 100)
        print(self.percurso.x, self.percurso.y)
        #self.objeto.set_position(640-20, 360-20+85)

        self.X0 = 640 - 25
        self.Y0 = 360 - 25
        self.raio = 84
        self.angulo = 0


    def circunferencia(self):
        self.angulo += self.velocidade * self.janela.delta_time()
        self.objeto.x = self.X0 + self.raio*cos(self.angulo)
        self.objeto.y = self.Y0 + self.raio*sin(self.angulo)

        self.percurso.draw()
        self.objeto.draw()
