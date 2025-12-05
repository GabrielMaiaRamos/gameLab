from pplay.window import *
from pplay.sprite import *

#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)
#comeco da parede em -> y = 160
fase = "menu"

#=====[Sprites]=====
looking = {
    0: Sprite("assets\\sprites\\player_right.png"),
    1: Sprite("assets\\sprites\\player_left.png")
}
looking[0].set_position(largura/2 + 200, altura/2)
looking[1].set_position(largura/2 + 200, altura/2)

hitbox_player = Sprite("assets\\sprites\\hitbox_player.png")
hitbox_player.set_position(largura/2 + 208, altura/2 + 135)

#=====[Modularização]=====
from playerScripts.playerMoviment import Movimentacao
move_player = Movimentacao(looking, hitbox_player, janela)

from rooms.salaJantar import Jantar
sala1 = Jantar(janela, looking[0]) #passo o looking[0] (olhando pra esquerda) pq tanto faz, as duas posicoes smp sao atualizadas

from rooms.salaBiblioteca import Biblioteca
sala2 = Biblioteca(janela, looking[0])

#=====[LOOP]=====
while True:
    match fase:
        case "menu":
            fase = "biblioteca"
        case "jantar":
            sala1.desenho_jantar()
            if sala1.move:
                move_player.moviment(sala1.objetos_jantar)
            if move_player.looking:
                looking[0].draw()
            else:
                looking[1].draw()
            if sala1.colisoes():
                fase = "biblioteca"
        case "biblioteca":
            sala2.desenho_biblioteca()
            if sala2.move:
                move_player.moviment(sala2.objetos_biblioteca)
            if move_player.looking:
                looking[0].draw()
            else:
                looking[1].draw()
    
    #=====[update]=====
    janela.update()