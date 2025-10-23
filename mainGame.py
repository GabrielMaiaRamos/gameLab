from pplay.window import *
from pplay.sprite import *


#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)
#comeco da parede em -> y = 160

#=====[Sprites]=====
player = Sprite("sprites\\player.png")
player.set_position(largura/2 + 200, altura/2)

<<<<<<< Updated upstream
=======
hitbox_player = Sprite("sprites\\hitbox_player.png")
hitbox_player.set_position(largura/2 + 208, altura/2 + 135)

<<<<<<< Updated upstream
#=====[sala de jantar]=====
>>>>>>> Stashed changes
salao_jantar = Sprite("sprites\\fundo_salao_jantar.png")

quadro = Sprite("sprites\\quadro.png")
quadro.set_position(250, 30)

lareira = Sprite("sprites\\lareira.png")
lareira.set_position(0, 0)

armario = Sprite("sprites\\armario.png")
<<<<<<< Updated upstream
armario.set_position(1080, 200)

mesa_jantar = Sprite("sprites\\mesa_jantar.png")
mesa_jantar.set_position(largura/2 - 100, altura/2)

tv = Sprite("sprites\\tv.png")
tv.set_position(950, 30)
=======
armario.set_position(1080, 75)

mesa_jantar = Sprite("sprites\\mesa_jantar.png")
mesa_jantar.set_position(largura/2 - 100, altura/2)

bussula = Sprite("sprites\\bussula.png")
bussula.set_position(560, 375)

tv = Sprite("sprites\\tv.png")
tv.set_position(800, 30)

porta = Sprite("sprites\\porta.png")
porta.set_position(540, 20)

carrinho = Sprite("sprites\\carrinho.png")
carrinho.set_position(1050, 500)

retrato = Sprite("sprites\\retrato.png")
retrato.set_position(300, 300)

objetos_jantar = [lareira, armario, mesa_jantar]
>>>>>>> Stashed changes

#=====[Modularização]=====
from playerMoviment import Movimentacao
move_player = Movimentacao(player, hitbox_player, janela)

=======
#=====[Modularização]=====s
from playerScripts.playerMoviment import Movimentacao
move_player = Movimentacao(player, hitbox_player, janela)

from rooms.salaJantar import Jantar
sala1 = Jantar(janela, player)

from minigames.gameAlavanca import Alavanca
alavanca1 = Alavanca(janela, (640, 360))



>>>>>>> Stashed changes
#=====[LOOP]=====
while True:
<<<<<<< Updated upstream
    print(player.x, janela.height, player.x+100)
    move_player.moviment()

    #=====[draws]=====

    #===abaixo do player===
    salao_jantar.draw()
    quadro.draw()
    armario.draw()
    lareira.draw()
    tv.draw()
    #===layer do player===
    player.draw()
    #===acima do player
    mesa_jantar.draw()

    #=====[upadte]=====
=======
    #print(player.x, janela.height, player.x+100)
    move_player.moviment(objetos_jantar)
    match fase:
        case "menu":
            fase = "jantar"
            pass
        case "jantar":
<<<<<<< Updated upstream
    #=====[draws]=====

            print(player.x, janela.height, player.x+100)
            move_player.moviment(objetos_jantar)

            #===abaixo do player===
            salao_jantar.draw()
            quadro.draw()
            armario.draw()
            lareira.draw()
            retrato.draw()
            tv.draw()
            porta.draw()
            mesa_jantar.draw()
            bussula.draw()
            #===layer do player===
            player.draw()
            #===acima do player
            carrinho.draw()

            hitbox_player.draw()
            #=====[upadte]=====
>>>>>>> Stashed changes

=======
            sala1.desenho_jantar()
            if not sala1.interativo:
                move_player.moviment(sala1.objetos_jantar)

            player.draw()
            sala1.colisoes()
            # janela.set_background_color((100,0,0))
            # memoria1.mostrar_obejtos()
            # alavanca1.circunferencia()
        
    #=====[update]=====
>>>>>>> Stashed changes
    janela.update()