from pplay.window import *
from pplay.sprite import *
from minigames.teclado_letras import Palavra
from minigames.gameAlavanca import Alavanca
from minigames.gameMemoria import Memoria

door_type = 0

#=====[SPRITES]=====
fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")
salao_jantar = Sprite("assets\\sprites\\fundo_salao_jantar.png")
lareira_pop = Sprite("assets\\sprites\\lareira_janela.png")

quadro = Sprite("assets\\sprites\\quadro.png")
quadro.set_position(250, 30)

lareira = Sprite("assets\\sprites\\lareira.png")
lareira.set_position(0, 0)

armario = Sprite("assets\\sprites\\armario.png")
armario.set_position(1143, 75)

mesa_jantar = Sprite("assets\\sprites\\mesa_jantar.png")
mesa_jantar.set_position(540, 360)

bussula = Sprite("assets\\sprites\\bussula.png")
bussula.set_position(560, 375)

tv = Sprite("assets\\sprites\\tv.png")
tv.set_position(800, 30)

tv_tela = Sprite("assets\\sprites\\tv_popup.png")
tv_tela.set_position(290, 140)

circulo_1 = Sprite("assets\\sprites\\circulo_apagado.png")
circulo_1.set_position(460, 450)

circulo_2 = Sprite("assets\\sprites\\circulo_apagado.png")
circulo_2.set_position(490, 450)

circulo_3 = Sprite("assets\\sprites\\circulo_apagado.png")
circulo_3.set_position(520, 450)

circulos = [circulo_1, circulo_2, circulo_3]

carrinho = Sprite("assets\\sprites\\carrinho.png")
carrinho.set_position(1050, 500)

retrato = Sprite("assets\\sprites\\retrato.png")
retrato.set_position(160, 320)

copo = Sprite("assets\\sprites\\copo.png")
copo.set_position(1125, 505)

oculos = Sprite("assets\\sprites\\oculos.png")
oculos.set_position(590, 660)

lustre = Sprite("assets\\sprites\\lustre.png")


ordem = Sprite("assets\\sprites\\ordem.png")
ordem.set_position(465, 185)

lever = {
    0: Sprite("assets\\sprites\\alavanca_off.png"),
    1: Sprite("assets\\sprites\\alavanca_on.png")
}

cabinet = {
    0: Sprite("assets\\sprites\\armario_pop.png"),
    1: Sprite("assets\\sprites\\armario_pop_2.png"),
}

frame = {
    0: Sprite("assets\\sprites\\quadro_pop.png"),
    1: Sprite("assets\\sprites\\quadro_pop_2.png")
}

door = {
    0: Sprite("assets\\sprites\\porta.png"),
    1: Sprite("assets\\sprites\\porta_win.png")
}

class Jantar():
    def __init__(self, janela, player):
        self.objetos_jantar = [lareira, armario, mesa_jantar, carrinho]
        self.player = player
        self.janela = janela

        #popups
        self.pop_up_armario = False
        self.pop_up_lareira = False
        self.interativo = False
        self.pop_up_quadro = False

        #inicializa o minigame da memoria
        self.minigame_memoria = False
        self.memoria = Memoria(self.janela, "lustre")
        self.win_memoria = False

        #inicializa o minigame da alavanca
        self.win_alavanca = False
        self.alavanca = Alavanca(self.janela)
        self.minigame_alavanca = False

        #inicializa o input do player
        self.palpite = Palavra(self.janela)
        self.corretas = ["radar", "morde", "dorme", "poder", "podre", "depor"] #lista de respostas corretas
        self.acertos_txt = 0
        self.oculos = False

        #estado de cada sprite
        self.frame_type = 0
        self.lever_type = 0
        self.cabinet_type = 0

        self.move = True

    def colisoes(self):
        global door_type
        #===================TELEVISAO POP======================
    
        #se apertar "e" enquanto esta proximo da tv, abre um sprite de "tela da tv"
        if Window.keyboard.key_pressed("e") and self.player.collided(tv):
            self.interativo = True
            self.move = False
        
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

                    elif self.palpite.palavra in ["morde", "dorme"]:
                        self.corretas.remove("morde")
                        self.corretas.remove("dorme")

                    elif self.palpite.palavra in ["poder", "podre", "depor"]:
                        self.corretas.remove("poder")
                        self.corretas.remove("podre")
                        self.corretas.remove("depor")
                    self.acertos_txt += 1

                    #muda o sprite de um circulo ao acertar
                    circulos[self.acertos_txt-1] = Sprite("assets\\sprites\\circulo_aceso.png")
                    circulos[self.acertos_txt-1].set_position(460 + ((self.acertos_txt-1)*30), 450)
                    
                #reinicia o palpite para uma string vazia
                self.palpite.palavra = ""
            #se apertar esc, fecha o sprite "tela da tv" e retorna à sala de jantar
            if Window.keyboard.key_pressed("esc"):
                self.move = True
                self.interativo = False
                #reinicia o objeto palpite
                self.palpite = Palavra(self.janela)
        
        if self.acertos_txt == 3:
           door_type = 1
        
        porta = door[door_type]
        porta.set_position(540, 20)

        if self.acertos_txt == 3 and Window.keyboard.key_pressed("e") and self.player.collided(porta):
            return True

        #===================MINIGAME ALAVANCA======================

        if Window.keyboard.key_pressed("e") and self.player.collided(lareira):
            self.pop_up_lareira = True
            self.move = False
        
        alavanca = lever[self.lever_type]
        alavanca.set_position(625, 590)

        if self.pop_up_lareira:
            lareira_pop.draw()
            alavanca.draw()

            if Window.mouse.is_over_object(alavanca) and Window.mouse.is_button_pressed(1) and not self.win_alavanca:
                self.minigame_alavanca = True
            if Window.keyboard.key_pressed("esc"):
                self.move = True
                self.pop_up_lareira = False
        
        # aqui inicia o jogo da alavanca
        if self.minigame_alavanca:
            self.win_alavanca = self.alavanca.circunferencia()
            # se o player aperta ESC o jogo fecha
            if Window.keyboard.key_pressed("esc"):
                self.alavanca = Alavanca(self.janela)
                self.move = True
                self.minigame_alavanca = False
        
        if self.win_alavanca:
            # DESCE O LUSTRE QUE CONTEM O JOGO DA MEMORIA
            self.cabinet_type = 1
            self.lever_type = 1
            lustre.set_position(350, 0)
            self.objetos_jantar.append(lustre)

        #==========================ARMARIO POP======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(armario):
            self.pop_up_armario = True
            self.move = False
        
        if Window.keyboard.key_pressed("esc"):
            self.move = True
            self.pop_up_armario = False
            
        if self.pop_up_armario:
            cabinet[self.cabinet_type].draw()
            if self.win_alavanca:
                if not self.oculos:
                    oculos.draw()
                    if Window.mouse.is_over_object(oculos) and Window.mouse.is_button_pressed(1): # PERMITE QUE O PLAYER "EQUIPE" O OCULOS
                        self.frame_type = 1
                        self.oculos = True

        #==========================QUADRO POP======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(quadro):
            self.pop_up_quadro = True
            self.move = False
        
        if self.pop_up_quadro:
            fundo_pop.draw()
            quadro_pop = frame[self.frame_type]
            quadro_pop.set_position(465, 10)
            quadro_pop.draw()

            if Window.keyboard.key_pressed("esc"):
                self.move = True
                self.pop_up_quadro = False

        #==========================MINIGAME MEMORIA======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(lustre):
            self.minigame_memoria = True
            self.move = False

        if self.minigame_memoria:
            self.memoria.win_memoria = self.memoria.mostrar_obejtos()
            if self.memoria.perdi:
                self.memoria = Memoria(self.janela, "lustre")
            if Window.keyboard.key_pressed("esc"):
                self.minigame_memoria = False
        
        if self.memoria.win_memoria:
            self.minigame_memoria = False
            fundo_pop.draw()
            ordem.draw()
            if Window.keyboard.key_pressed("esc"):
                self.move = True
                self.memoria.win_memoria = False
                


    def desenho_jantar(self):
        #===abaixo do player===
        porta = door[door_type]
        porta.set_position(540, 20)
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
        if self.win_alavanca:
            lustre.draw()
        