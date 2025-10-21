from pplay.window import *
from pplay.sprite import *
from teclado_letras import Palavra

fundo_pop = Sprite("sprites\\fundo_pop.png")

#=====[Sala de Jantar]=====
salao_jantar = Sprite("sprites\\fundo_salao_jantar.png")

quadro = Sprite("sprites\\quadro.png")
quadro.set_position(250, 30)

lareira = Sprite("sprites\\lareira.png")
lareira.set_position(0, 0)

armario = Sprite("sprites\\armario.png")
armario.set_position(1143, 75)

mesa_jantar = Sprite("sprites\\mesa_jantar.png")
mesa_jantar.set_position(540, 360)

bussula = Sprite("sprites\\bussula.png")
bussula.set_position(560, 375)

tv = Sprite("sprites\\tv.png")
tv.set_position(800, 30)

tv_tela = Sprite("sprites\\tv_popup.png")
tv_tela.set_position(290, 140)

porta = Sprite("sprites\\porta.png")
porta.set_position(540, 20)

carrinho = Sprite("sprites\\carrinho.png")
carrinho.set_position(1050, 500)

retrato = Sprite("sprites\\retrato.png")
retrato.set_position(160, 320)

copo = Sprite("sprites\\copo.png")
copo.set_position(1125, 505)

objetos_jantar = [lareira, armario, mesa_jantar, carrinho]

class Jantar():
    def __init__(self, janela, player):
        self.objetos_jantar = objetos_jantar
        self.player = player
        self.janela = janela
        self.interativo = False
        self.palavra_1 = Palavra(self.janela)
        self.corretas = ["radar", "ordem", "morde", "dorme", "poder", "podre", "depor"]
        self.acertos = 0

    def colisoes(self):
        if Window.keyboard.key_pressed("e") and self.player.collided(tv):
            self.interativo = True
        
        if self.interativo:
            fundo_pop.draw()
            tv_tela.draw()
            self.palavra_1.input_letra()

            if Window.keyboard.key_pressed("enter"):
                if self.palavra_1.palavra in self.corretas:
                    for i in range(len(self.corretas)):
                        remover = 0
                        if self.palavra_1.palavra == "radar":
                            remover = 1
                        elif self.palavra_1.palavra in ["ordem", "morde", "dorme"]:
                            remover = 2
                        else:
                            remover = 3
                        break
                    if remover == 1:
                        self.corretas.remove("radar")
                    if remover == 2:
                        self.corretas.remove("ordem")
                        self.corretas.remove("morde")
                        self.corretas.remove("dorme")
                    if remover == 3:
                        self.corretas.remove("poder")
                        self.corretas.remove("podre")
                        self.corretas.remove("depor")
                    self.acertos += 1
                self.palavra_1.palavra = ""
                print(self.acertos)
                print(self.corretas)
            
            if Window.keyboard.key_pressed("esc"):
                self.interativo = False
                self.palavra_1 = Palavra(self.janela)
        
    def desenho_jantar(self):
        #===abaixo do player
        salao_jantar.draw()
        quadro.draw()
        armario.draw()
        lareira.draw()
        retrato.draw()
        tv.draw()
        porta.draw()
        mesa_jantar.draw()
        bussula.draw()
        carrinho.draw()
        copo.draw()
        