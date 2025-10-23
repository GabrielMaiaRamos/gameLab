from pplay.window import *
from pplay.sprite import *
from math import cos, sin
from random import choice
import numpy as np

fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")

circulo = Sprite("assets\\sprites\\roda_alavanca.png")
circulo.set_position(580, 320)

aro = Sprite("assets\\sprites\\aro_alavanca.png")

velocidades = np.random.choice((6,7,8,9,10), size=10, replace=True)

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

ponto1 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto2 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto3 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto4 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto5 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto6 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto7 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto8 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto9 = Sprite("assets\\sprites\\circulo_apagado.png")
ponto10 = Sprite("assets\\sprites\\circulo_apagado.png")

pontos = [ponto1, ponto2, ponto3, ponto4, ponto5, ponto6, ponto7, ponto8, ponto9, ponto10]

pos_selecionada = np.random.choice((1,2,3,4,5,6,7,8), size=10, replace=True)

class Alavanca():
    def __init__(self, janela):

        self.turn = 0
        self.janela = janela
        self.timer = 0
        self.acertos_alavanca = -1
        

        self.objeto = Sprite("assets\\sprites\\roda_alavanca.png")
        self.percurso = Sprite("assets\\sprites\\aro_alavanca.png")
        self.percurso.set_position(540, 260)
        #self.objeto.set_position(640-20, 360-20+85)

        # posição inicial da rotação da bola
        self.X0 = 640 - 35/2
        self.Y0 = 360 - 35/2
        self.raio = 84
        self.angulo = 0


    def circunferencia(self):
        if self.turn == 10:
            return True
        self.acerto = imagem[pos_selecionada[self.turn]]
        self.acerto.set_position(coordenada[pos_selecionada[self.turn]][0], coordenada[pos_selecionada[self.turn]][1])
        self.velocidade = velocidades[self.turn]
        fundo_pop.draw()
        self.timer += self.janela.delta_time()

        #faz a roda girar
        self.angulo += self.velocidade * self.janela.delta_time()
        self.objeto.x = self.X0 + self.raio*cos(self.angulo)
        self.objeto.y = self.Y0 + self.raio*sin(self.angulo)

        self.percurso.draw()
        self.acerto.draw()
        self.objeto.draw()

        self.pontuacao()
        self.placar()
        
    
    def pontuacao(self):
        if self.timer >= 0.15:
            # se o player aperta Q enquanto a bola esta em na hitbox certa o jogo muda a velocidade e a posição da hitbox correta e um ponto é adicionado
            # caso o player aperte Q e não esteja na hitbox certa os pontos reiniciam
            if Window.keyboard.key_pressed("q") and self.objeto.collided(self.acerto):
                self.turn += 1
                self.acertos_alavanca += 1
                self.timer = 0
                
            elif Window.keyboard.key_pressed("q"):
                self.turn = 0
                self.acertos_alavanca = -1
                self.timer = 0
    
    def placar(self):
        # muda os sprites dos pontos de acordo com a jogada do player
        if self.acertos_alavanca >= 0:
            pontos[self.acertos_alavanca] = Sprite("assets\\sprites\\circulo_aceso.png")
            if self.turn <= 5:
                pontos[self.acertos_alavanca].set_position(540 + 50*(self.acertos_alavanca), 490)
            else:
                pontos[self.acertos_alavanca].set_position(540 + 50*(self.acertos_alavanca - 5), 520)
        else:
            for i in range(len(pontos)):
                pontos[i] = Sprite("assets\\sprites\\circulo_apagado.png")
                if i < 5:
                    pontos[i].set_position(540 + 50*i, 490)
                else:
                    pontos[i].set_position(540 + 50*(i - 5), 520)
        for ponto in pontos:
            ponto.draw()
