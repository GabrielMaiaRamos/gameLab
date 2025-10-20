from pplay.window import *
from pplay.sprite import *

#=====[JANELA]=====
largura = 1280
altura = 720
janela = Window(largura, altura)


#=====[Sprites]=====
player = Sprite("C:\\Users\\Computador\\Documents\\GitHub\\gameLab\\spirtes\\00-final-product.png")
player.set_position(largura/2, altura/2)

salao_jantar = Sprite("C:\\Users\\Computador\\Documents\\GitHub\\gameLab\spirtes\\fundo_salao_jantar.png")

mesa_jantar = Sprite("spirtes\mesa_jantar.png")
mesa_jantar.set_position(largura/2, altura/2)
#=====[LOOP]=====
while True:


    #=====[draws]=====


    #=====[upadte]=====
    salao_jantar.draw()
    mesa_jantar.draw()
    player.draw()
    janela.update()