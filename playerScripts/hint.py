from pplay.window import *
from pplay.sprite import *

fundo = Sprite("assets\\sprites\\dica_fundo.png")
fundo.set_position(980, 50)

class Hint():
    def __init__(self, janela):
        self.janela = janela

    def dica(self, tela):
        fundo.draw()
        if not tela:
            self.janela.draw_text("Use o botão esquerdo do mouse ", 1020, 70, 20, (255,255,255))
            self.janela.draw_text("para interagir com objetos", 1020, 100, 20, (255,255,255))
        else:
            self.janela.draw_text("Aperte E próximo à um objeto", 1020, 70, 20, (255,255,255))
            self.janela.draw_text("para interagir com o mesmo""", 1020, 100, 20, (255,255,255))
        self.janela.draw_text("Pressione ESC para fechar a", 1020, 130, 20, (255,255,255))
        self.janela.draw_text("interação ou abrir o menu", 1020, 160, 20, (255,255,255))