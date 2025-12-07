from pplay.window import *
from pplay.sprite import *
from pplay.sound import *

#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)
#comeco da parede em -> y = 160
fundo = Sprite("assets\\sprites\\fundo_jogo.png")
start = Sprite("assets\\sprites\\jogar.png")
start.set_position(280, 600)
exit = Sprite("assets\\sprites\\sair.png")
exit.set_position(800, 600)
fase = "menu"
timer = 0

#=====[Sprites]=====
looking = {
    0: Sprite("assets\\sprites\\player_right.png"),
    1: Sprite("assets\\sprites\\player_left.png")
}
looking[0].set_position(largura/2 + 200, altura/2)
looking[1].set_position(largura/2 + 200, altura/2)

hitbox_player = Sprite("assets\\sprites\\hitbox_player.png")
hitbox_player.set_position(largura/2 + 208, altura/2 + 135)

#=====[Sons]=====
musica_ambiente = Sound("assets\\sounds\\ambiente1.ogg")
musica_ambiente.set_volume(50)
musica_ambiente.stop()
musica_ambiente.loop = True
musica_ambiente.play()

efeito_pop_up = Sound("assets\\sounds\\efeito_pop_up_geral.ogg")

#=====[Modularização]=====
from playerScripts.playerMoviment import Movimentacao
move_player = Movimentacao(looking, hitbox_player, janela)

from rooms.salaJantar import Jantar
sala1 = Jantar(janela, looking[0]) #passo o looking[0] (olhando pra esquerda) pq tanto faz, as duas posicoes smp sao atualizadas

#=====[LOOP]=====
while True:
    match fase:
        case "menu":
            fundo.draw()
            start.draw()
            exit.draw()
            if Window.mouse.is_over_object(start) and Window.mouse.is_button_pressed(1):
                efeito_pop_up.play()
                fase = "jantar"
            if Window.mouse.is_over_object(exit) and Window.mouse.is_button_pressed(1):
                break
        case "jantar":
            timer += janela.delta_time()
            sala1.desenho_jantar()
            if sala1.move:
                move_player.moviment(sala1.objetos_jantar)
            if move_player.looking:
                looking[0].draw()
            else:
                looking[1].draw()
            if sala1.colisoes():
                fase = "win"
        case "win":
            pass
    
    #=====[update]=====
    janela.update()