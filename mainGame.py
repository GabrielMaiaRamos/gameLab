from pplay.window import *
from pplay.sprite import *
import math

#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)
#comeco da parede em -> y = 160
fase = "menu"

#=====[Sprites]=====
player = Sprite("sprites\\player.png")
player.set_position(largura/2 + 200, altura/2)

quadro1 = Sprite("sprites\\quadro.png")
quadro1.set_position(600, 200)

hitbox_player = Sprite("sprites\\hitbox_player.png")
hitbox_player.set_position(largura/2 + 208, altura/2 + 135)

#=====[Modularização]=====
from playerMoviment import Movimentacao
move_player = Movimentacao(player, hitbox_player, janela)

from salaJantar import Jantar
sala1 = Jantar(janela, player)

from minigames import gameAlavanca


#=====[LOOP]=====
while True:
    match fase:
        case "menu":
            fase = "jantar"
            pass
        case "jantar":
            sala1.desenho_jantar()
            if not sala1.interativo:
                move_player.moviment(sala1.objetos_jantar)
            player.draw()
            sala1.colisoes()

            #=====[upadte]=====

    janela.update()