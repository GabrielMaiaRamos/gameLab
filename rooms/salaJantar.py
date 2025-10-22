from pplay.window import *
from pplay.sprite import *
from minigames.teclado_letras import Palavra

fundo_pop = Sprite("sprites\\fundo_pop.png")

#=====[SPRITES]=====
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

circulo_1 = Sprite("sprites\\circulo_apagado.png")
circulo_1.set_position(580, 320)

circulo_2 = Sprite("sprites\\circulo_apagado.png")
circulo_2.set_position(610, 320)

circulo_3 = Sprite("sprites\\circulo_apagado.png")
circulo_3.set_position(640, 320)

circulos = [circulo_1, circulo_2, circulo_3]

porta = Sprite("sprites\\porta.png")
porta.set_position(540, 20)

carrinho = Sprite("sprites\\carrinho.png")
carrinho.set_position(1050, 500)

retrato = Sprite("sprites\\retrato.png")
retrato.set_position(160, 320)

copo = Sprite("sprites\\copo.png")
copo.set_position(1125, 505)

class Jantar():
    def __init__(self, janela, player):
        self.objetos_jantar = [lareira, armario, mesa_jantar, carrinho]
        self.player = player
        self.janela = janela
        self.interativo = False
        #inicializa o input do player
        self.palpite = Palavra(self.janela)
        #lista de respostas corretas
        self.corretas = ["radar", "ordem", "morde", "dorme", "poder", "podre", "depor"]
        self.acertos = 0

    def colisoes(self):
        #se apertar "e" enquanto esta proximo da tv, abre um sprite de "tela da tv"
        if Window.keyboard.key_pressed("e") and self.player.collided(tv):
            self.interativo = True
        
        if self.interativo:
            fundo_pop.draw()
            tv_tela.draw()
            #desenha a lista de 3 circulos
            for c in range(len(circulos)):
                circulos[c].draw()
            self.palpite.input_letra()

            #se der enter, verifica se a palavra formada esta na lista de corretas
            if Window.keyboard.key_pressed("enter"):
                #se estiver na lista de corretas, entao inicializa um loop para retirar as palavras correspondentes
                if self.palpite.palavra in self.corretas:
                    if self.palpite.palavra == "radar":
                        self.corretas.remove("radar")

                    elif self.palpite.palavra in ["ordem", "morde", "dorme"]:
                        self.corretas.remove("ordem")
                        self.corretas.remove("morde")
                        self.corretas.remove("dorme")

                    elif self.palpite.palavra in ["poder", "podre", "depor"]:
                        self.corretas.remove("poder")
                        self.corretas.remove("podre")
                        self.corretas.remove("depor")
                    self.acertos += 1

                    #muda o sprite de um circulo ao acertar
                    circulos[self.acertos-1] = Sprite("sprites\\circulo_aceso.png")
                    circulos[self.acertos-1].set_position(580 + ((self.acertos-1)*30), 320)
                    
                #reinicia o palpite para uma string vazia
                self.palpite.palavra = ""
            #se apertar esc, fecha o sprite "tela da tv" e retorna à sala de jantar
            if Window.keyboard.key_pressed("esc"):
                self.interativo = False
                #reinicia o objeto palpite
                self.palpite = Palavra(self.janela)
        
    def desenho_jantar(self):
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
        carrinho.draw()
        copo.draw()
        