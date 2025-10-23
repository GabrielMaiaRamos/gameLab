from pplay.window import *
from pplay.sprite import *
from math import cos, sin
from random import choice
import numpy as np

fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")

circulo = Sprite("assets\\sprites\\roda_alavanca.png")
circulo.set_position(580, 320)

aro = Sprite("assets\\sprites\\aro_alavanca.png")

velocidades = np.random.choice((5,6,7,8), size=5, replace=True)

# dicionario com as imagens de cada posição
imagem = {
    1: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_leste.png"),
    2: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_nordeste.png"),
    3: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_noroeste.png"),
    4: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_norte.png"),
    5: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_oeste.png"),
    6: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_sudeste.png"),
    7: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_sudoeste.png"),
    8: Sprite("assets\\sprites\\alavancas_hitbox\\alavanca_acerto_sul.png")
}

# dicionario com a coordenada de cada posição
coordenada = {
    1: (540 + 164, 260 + 77),
    2: (540 + 136, 260 + 20),
    3: (540 + 20, 260 + 20),
    4: (540 + 77, 260),
    5: (540, 260 + 77),
    6: (540 + 136, 260 + 136),
    7: (540 + 20, 260 + 136),
    8: (540 + 77, 260 + 163)
}

pos_selecionada = np.random.choice((1,2,3,4,5,6,7,8), size=15, replace=True)

class Alavanca():
    def __init__(self, janela):

        self.velocidade = choice(velocidades)
        self.janela = janela
        
        # aqui ele acessa ambos os dicionarios para criar a hitbox da vez
        selecionado = choice(pos_selecionada)
        self.acerto = imagem[selecionado]
        self.acerto.set_position(coordenada[selecionado][0], coordenada[selecionado][1])

        self.objeto = Sprite("assets\\sprites\\roda_alavanca.png")
        self.percurso = Sprite("assets\\sprites\\aro_alavanca.png")
        self.percurso.set_position(540, 260)
        #self.objeto.set_position(640-20, 360-20+85)

        self.X0 = 640 - 35/2
        self.Y0 = 360 - 35/2
        self.raio = 84
        self.angulo = 0


    def circunferencia(self):
        fundo_pop.draw()
        self.angulo += self.velocidade * self.janela.delta_time()
        self.objeto.x = self.X0 + self.raio*cos(self.angulo)
        self.objeto.y = self.Y0 + self.raio*sin(self.angulo)

        self.percurso.draw()
        self.acerto.draw()
        self.objeto.draw()
