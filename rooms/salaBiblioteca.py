from pplay.window import *
from pplay.sprite import *
from minigames.teclado_letras import Palavra
from minigames.gameAlavanca import Alavanca
from minigames.gameMemoria import Memoria
from playerScripts.hint import Hint

door_type = 0

fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")
salao_biblioteca = Sprite("assets\\sprites\\fase2\\fundo_salao_biblioteca.png")

armario = Sprite("assets\\sprites\\fase2\\armario.png")
armario.set_position(1143, 215)

door = {
    0: Sprite("assets\\sprites\\porta.png"),
    1: Sprite("assets\\sprites\\porta_win.png")
}

class Biblioteca():
    def __init__(self, janela, player):
        self.janela = janela
        self.player = player
        self.objetos_biblioteca = [armario]

        #permite o player se mover
        self.move = True
    
    def desenho_biblioteca(self):
        salao_biblioteca.draw()
        armario.draw()
        porta = door[door_type]
        porta.set_position(540, 20)
