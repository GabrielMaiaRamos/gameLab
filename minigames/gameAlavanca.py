from pplay.window import *
from pplay.sprite import *
from math import cos, sin

fundo_pop = Sprite("sprites\\fundo_pop.png")

circulo = Sprite("sprites\\roda_alavanca.png")
circulo.set_position(580, 320)

aro = Sprite("sprites\\aro_alavanca.png")



class Alavanca():
    def __init__(self, x0, y0, raio, velocidade, janela, objeto):
        self.X0 = x0
        self.Y0 = y0
        self.raio = raio
        self.velocidade = velocidade
        self.angulo = 0

        self.janela = janela
        self.objeto = objeto
    def circunferencia(self):
        self.angulo += self.velocidade * self.janela.delta_time()
        self.objeto.x = self.X0 + self.raio*cos(self.angulo)
        self.objeto.y = self.Y0 + self.raio*sin(self.angulo)
        self.objeto.draw()