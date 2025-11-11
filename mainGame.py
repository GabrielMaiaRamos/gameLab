from pplay.window import *
from pplay.sprite import *

#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)
#comeco da parede em -> y = 160
fase = "menu"

#=====[Sprites]=====
player = Sprite("assets\\sprites\\player.png")
player.set_position(largura/2 + 200, altura/2)

quadro1 = Sprite("assets\\sprites\\quadro.png")
quadro1.set_position(600, 200)

hitbox_player = Sprite("assets\\sprites\\hitbox_player.png")
hitbox_player.set_position(largura/2 + 208, altura/2 + 135)

#=====[Modularização]=====
from playerScripts.playerMoviment import Movimentacao
move_player = Movimentacao(player, hitbox_player, janela)

from rooms.salaJantar import Jantar
sala1 = Jantar(janela, player)

#=====[LOOP]=====
while True:
    match fase:
        case "menu":
            fase = "jantar"
        case "jantar":
            sala1.desenho_jantar()
            if sala1.move:
                move_player.moviment(sala1.objetos_jantar)
            player.draw()
            if sala1.colisoes():
                fase = "enigma1"
        case "enigma1":
            fase = "jantar"
    
    #=====[update]=====
    janela.update()