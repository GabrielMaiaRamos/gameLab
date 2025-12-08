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
fim = Sprite("assets\\sprites\\fundo_fim.png")
fase = "jantar"
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

#=====[Cutscene]=====
fundo_cutscene = Sprite("assets\\sprites\\cutscene_fundo.png")
fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")
player = Sprite("assets\\sprites\\cutscene_player.png")
player_x = 0
player.set_position(player_x, 300)
camera = Sprite("assets\\sprites\\cutscene_camera.png")
camera.set_position(890, 250)
box = Sprite("assets\\sprites\\cutscene_dialogo.png")
box.set_position(390, 500)
dialogo = 0
text = 0

#=====[Modularização]=====
from playerScripts.playerMoviment import Movimentacao
move_player = Movimentacao(looking, hitbox_player, janela)

from rooms.salaJantar import Jantar
sala1 = Jantar(janela, looking[0]) #passo o looking[0] (olhando pra esquerda) pq tanto faz, as duas posicoes smp sao atualizadas

from playerScripts.dialogo import Dialogue
texto = Dialogue(janela)

#=====[LOOP]=====
while True:
    match fase:
        case "menu":
            fundo.draw()
            start.draw()
            exit.draw()
            if Window.mouse.is_over_object(start) and Window.mouse.is_button_pressed(1):
                efeito_pop_up.play()
                fase = "cut"
            if Window.mouse.is_over_object(exit) and Window.mouse.is_button_pressed(1):
                break
        case "cut":
            timer += janela.delta_time()
            fundo_cutscene.draw()
            fundo_pop.draw()

            if timer >= 0.005 and player_x < 230:
                player_x += 1
                player.set_position(player_x, 300)
                timer = 0
            
            match dialogo:
                case 0:
                    player.draw()
                    if player_x == 230:
                        dialogo = 1
                case 1:
                    player.draw()
                    box.draw()
                    if texto.conversa(text):
                        dialogo += 1
                        text += 1
                case 2:
                    camera.draw()
                    box.draw()
                    if texto.conversa(text):
                        if text == 3:
                            text = 3.4
                        else:
                            dialogo -= 1
                            if text == 5.4:
                                fase = "jantar"
                            text += 1
        case "jantar":
            if not sala1.menu:
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
            if sala1.sair:
                break
        case "win":
            fim.draw()
            exit.set_position(210, 470)
            exit.draw()
            if Window.mouse.is_over_object(exit) and Window.mouse.is_button_pressed(1):
                break
            min = timer / 60
            seg = timer % 60
            janela.draw_text("Parabéns!", 210, 120, 50, (255,255,255))
            janela.draw_text("Você conseguiu escapar da", 150, 190, 30, (255,255,255))
            janela.draw_text(f"mansão em {min:.0f}min e {seg:.2f}s!", 150, 230, 30, (255,255,255))
            janela.draw_text("Com isso você ganhou", 150, 280, 30, (255,255,255))
            janela.draw_text(f"{min * (1+seg):.2f} mil dólares!", 150, 320, 30, (255,255,255))
            janela.draw_text("Aproveite o seu prêmio e até", 150, 370, 30, (255,255,255))
            janela.draw_text("o próximo desafio!", 150, 410, 30, (255,255,255))
    
    #=====[update]=====
    janela.update()