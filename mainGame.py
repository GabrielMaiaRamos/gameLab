from pplay.window import *
from pplay.sprite import *

#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)


#=====[Sprites]=====
player = Sprite("sprites\\player.png")
player.set_position(largura/2 + 200, altura/2)

salao_jantar = Sprite("sprites\\fundo_salao_jantar.png")

quadro = Sprite("sprites\\quadro.png")
quadro.set_position(250, 30)

lareira = Sprite("sprites\\lareira.png")
lareira.set_position(0, 0)

armario = Sprite("sprites\\armario.png")
armario.set_position(1080, 200)

mesa_jantar = Sprite("sprites\\mesa_jantar.png")
mesa_jantar.set_position(largura/2 - 100, altura/2)

tv = Sprite("sprites\\tv.png")
tv.set_position(950, 30)
#=====[LOOP]=====
while True:


    #=====[draws]=====


    #=====[upadte]=====
    salao_jantar.draw()
    mesa_jantar.draw()
    quadro.draw()
    armario.draw()
    lareira.draw()
    tv.draw()
    player.draw()
    janela.update()