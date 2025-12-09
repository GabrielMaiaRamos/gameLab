from pplay.window import *
from pplay.sprite import *
from pplay.sound import *
from minigames.teclado_letras import Palavra
from minigames.gameAlavanca import Alavanca
from minigames.gameMemoria import Memoria
from playerScripts.hint import Hint

door_type = 0

#=====[SONS]=====
efeito_pop_up = Sound("assets\\sounds\\efeito_pop_up_geral.ogg")
efeito_armario = Sound("assets\\sounds\\efeito_armario.ogg")
efeito_final = Sound("assets\\sounds\\efeito_final.ogg")
efeito_correto = Sound("assets\\sounds\\efeito_correto.ogg")
efeito_errado = Sound("assets\\sounds\\efeito_errado.ogg")
efeito_submit = Sound("assets\\sounds\\efeito_submit.ogg")
efeito_coleta = Sound("assets\\sounds\\efeito_coleta.ogg")

#=====[SPRITES]=====
fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")
salao_jantar = Sprite("assets\\sprites\\fundo_salao_jantar.png")
lareira_pop = Sprite("assets\\sprites\\lareira_janela.png")
mesa_pop = Sprite("assets\\sprites\\mesa_pop.png")
carrinho_pop = Sprite("assets\\sprites\\carrinho_pop1.png")

retornar = Sprite("assets\\sprites\\return.png")
retornar.set_position(540, 250)
sair = Sprite("assets\\sprites\\sair.png")
sair.set_position(540, 400)
menu = Sprite("assets\\sprites\\pause.png")
menu.set_position(440, 50)

bolsa = Sprite("assets\\sprites\\bolsa.png")
bolsa.set_position(772, 370)

quadro = Sprite("assets\\sprites\\quadro.png")
quadro.set_position(250, 30)

lareira = Sprite("assets\\sprites\\lareira.png")
lareira.set_position(0, 0)

armario = Sprite("assets\\sprites\\armario.png")
armario.set_position(1143, 75)

mesa_jantar = Sprite("assets\\sprites\\mesa_jantar.png")
mesa_jantar.set_position(540, 360)

bussula = Sprite("assets\\sprites\\bussula.png")
bussula.set_position(320, 262)

bussula1 = Sprite("assets\\sprites\\bussula_1.png")
bussula1.set_position(320, 262)

bussula2 = Sprite("assets\\sprites\\bussula_2.png")
bussula2.set_position(320, 262)

bussula3 = Sprite("assets\\sprites\\bussula_3.png")
bussula3.set_position(320, 262)

tv = Sprite("assets\\sprites\\tv.png")
tv.set_position(800, 30)

tv_tela = Sprite("assets\\sprites\\tv_popup.png")
tv_tela.set_position(290, 140)

circulo_1 = Sprite("assets\\sprites\\circulo_apagado.png")
circulo_1.set_position(460, 450)

circulo_2 = Sprite("assets\\sprites\\circulo_apagado.png")
circulo_2.set_position(500, 450)

circulo_3 = Sprite("assets\\sprites\\circulo_apagado.png")
circulo_3.set_position(540, 450)

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

duvida = Sprite("assets\\sprites\\duvida.png")
duvida.set_position(1230, 0)

ordem = Sprite("assets\\sprites\\ordem.png")
ordem.set_position(465, 185)

alavanca = Sprite("assets\\sprites\\alavanca_off.png")
alavanca.set_position(625, 590)

cabinet = Sprite("assets\\sprites\\armario_pop.png")

frame = Sprite("assets\\sprites\\quadro_pop.png")

crossword = Sprite("assets\\sprites\\crossword.png")
crossword.set_position(385.5, 37.5)

one = Sprite("assets\\sprites\\crossword\\one.png")
one.set_position(505, 80)

two = Sprite("assets\\sprites\\crossword\\two.png")
two.set_position(400, 195)

three = Sprite("assets\\sprites\\crossword\\three.png")
three.set_position(460, 295)

four = Sprite("assets\\sprites\\crossword\\four.png")
four.set_position(725, 80)

door = {
    0: Sprite("assets\\sprites\\porta.png"),
    1: Sprite("assets\\sprites\\porta_win.png")
}

dica_type = "notpop"

def mudaSprite(objeto):
    global alavanca, cabinet, frame, one, two, three, carrinho_pop, four
    match objeto:
        case "alavanca":
            alavanca = Sprite("assets\\sprites\\alavanca_on.png")
            alavanca.set_position(625, 590)
            cabinet = Sprite("assets\\sprites\\armario_pop_2.png")
        case "oculos":
            frame = Sprite("assets\\sprites\\quadro_pop_2.png")
            carrinho_pop = Sprite("assets\\sprites\\carrinho_pop2.png")
        case "one":
            one = Sprite("assets\\sprites\\crossword\\one_green.png")
            one.set_position(505, 80)
        case "two":
            two = Sprite("assets\\sprites\\crossword\\two_green.png")
            two.set_position(400, 195)
        case "three":
            three = Sprite("assets\\sprites\\crossword\\three_green.png")
            three.set_position(460, 295)
        case "four":
            four = Sprite("assets\\sprites\\crossword\\four_green.png")
            four.set_position(725, 80)

class Jantar():
    def __init__(self, janela, player):
        self.objetos_jantar = [lareira, armario, mesa_jantar, carrinho]
        self.player = player
        self.janela = janela

        #popups
        self.pop_up_armario = False
        self.pop_up_lareira = False
        self.pop_up_mesa = False
        self.interativo = False
        self.pop_up_quadro = False
        self.pop_up_carrinho = False
        self.pops = False
        self.menu = False
        self.sair = False
        self.timer_menu = 0

        #permite o player se mover
        self.move = True

        #dicas
        self.hint = Hint(self.janela)
        self.dica = False
        self.timer_dica = 0

        #mudança das bússulas
        self.bussulas = False
        self.bussulas_list = [bussula, bussula1, bussula2, bussula3]
        self.bussula_indice = 0
        self.timer = 0

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

        #minigame crossword
        self.minigame_bolsa = False
        self.primeira = Palavra(self.janela)
        self.segunda = Palavra(self.janela)
        self.terceira = Palavra(self.janela)
        self.final = Palavra(self.janela)
        self.um = False
        self.dois = False
        self.tres = False
        self.quatro = False
        self.diquinha = "cruz"

        #requisito para finalizar o jogo
        self.win = False

    def colisoes(self):
        global door_type, dica_type

        

        #===================TELEVISAO POP======================

        #se apertar "e" enquanto esta proximo da tv, abre um sprite de "tela da tv"
        if Window.keyboard.key_pressed("e") and self.player.collided(tv):
            #se for a primeira vez que abre
            if self.interativo == False:
                efeito_pop_up.play()
            self.interativo = True
            self.move = False
            self.pops = True
            
            
        
        if self.interativo:
            fundo_pop.draw()
            tv_tela.draw()
            #desenha a lista de 3 circulos
            for c in range(len(circulos)):
                circulos[c].draw()
            self.palpite.input_letra("palpite")

            #se der enter, verifica se a palavra formada esta na lista de corretas
            if Window.keyboard.key_pressed("enter"):
                #se estiver na lista de corretas, entao inicializa um loop para retirar as palavras correspondentes
                if self.palpite.palavra in self.corretas:
                    if self.palpite.palavra == "radar":
                        efeito_correto.play()
                        self.corretas.remove("radar")

                    elif self.palpite.palavra in ["morde", "dorme"]:
                        efeito_correto.play()
                        self.corretas.remove("morde")
                        self.corretas.remove("dorme")

                    elif self.palpite.palavra in ["poder", "podre", "depor"]:
                        efeito_correto.play()
                        self.corretas.remove("poder")
                        self.corretas.remove("podre")
                        self.corretas.remove("depor")
                    self.acertos_txt += 1

                    
                    #muda o sprite de um circulo ao acertar
                    circulos[self.acertos_txt-1] = Sprite("assets\\sprites\\circulo_aceso.png")
                    circulos[self.acertos_txt-1].set_position(460 + ((self.acertos_txt-1)*40), 450)
                else:
                    efeito_submit.play()
              
                #reinicia o palpite para uma string vazia
                self.palpite.palavra = ""
            #se apertar esc, fecha o sprite "tela da tv" e retorna à sala de jantar
            if Window.keyboard.key_pressed("esc") and self.player.collided(tv):
                efeito_pop_up.play()
                self.move = True
                self.pops = False
                self.interativo = False
                #reinicia o objeto palpite
                self.palpite = Palavra(self.janela)
        
        if self.acertos_txt == 3:
            self.win = True
            dica_type = "mudou"
            self.dica = True
            door_type = 1
            self.acertos_txt = 0
        
        porta = door[door_type]
        porta.set_position(540, 20)

        if self.win and Window.keyboard.key_pressed("e") and self.player.collided(porta):
            efeito_final.play()
            return True

        #===================MINIGAME ALAVANCA======================

        if Window.keyboard.key_pressed("e") and self.player.collided(lareira):
            self.pops = True
            efeito_pop_up.play()
            self.pop_up_lareira = True
            self.move = False

        if self.pop_up_lareira:
            lareira_pop.draw()
            alavanca.draw()

            if Window.mouse.is_over_object(alavanca) and Window.mouse.is_button_pressed(1) and not self.win_alavanca:
                self.minigame_alavanca = True
            if Window.keyboard.key_pressed("esc") and self.player.collided(lareira):
                efeito_pop_up.play()
                self.pops = False
                self.move = True
                self.pop_up_lareira = False
        
        # aqui inicia o jogo da alavanca
        if self.minigame_alavanca:
            self.win_alavanca = self.alavanca.circunferencia()
            # se o player aperta ESC o jogo fecha
            if Window.keyboard.key_pressed("esc") and self.player.collided(lareira):
                self.alavanca = Alavanca(self.janela)
                self.move = True
                self.minigame_alavanca = False
        
        if self.win_alavanca:
            self.minigame_alavanca = False
            dica_type = "mudou"
            self.dica = True
            # DESCE O LUSTRE QUE CONTEM O JOGO DA MEMORIA
            mudaSprite("alavanca")
            lustre.set_position(350, 0)
            self.objetos_jantar.append(lustre)
            self.win_alavanca = False

        #==========================ARMARIO POP======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(armario):
            efeito_armario.play()
            self.pops = True
            self.pop_up_armario = True
            self.move = False
        
        if Window.keyboard.key_pressed("esc") and self.player.collided(armario):
            efeito_armario.play()
            self.move = True
            self.pops = False
            self.pop_up_armario = False
            
        if self.pop_up_armario:
            cabinet.draw()
            if lustre in self.objetos_jantar:
                if not self.oculos:
                    oculos.draw()
                    if Window.mouse.is_over_object(oculos) and Window.mouse.is_button_pressed(1): # PERMITE QUE O PLAYER "EQUIPE" O OCULOS
                        efeito_coleta.play()
                        mudaSprite("oculos")
                        dica_type = "mudou"
                        self.dica = True
                        self.oculos = True

        #==========================QUADRO POP======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(quadro):
            efeito_pop_up.play()
            self.pop_up_quadro = True
            self.move = False
            self.pops = True
        
        if self.pop_up_quadro:
            fundo_pop.draw()
            frame.set_position(465, 10)
            frame.draw()

            if Window.keyboard.key_pressed("esc") and self.player.collided(quadro):
                efeito_pop_up.play()
                self.pops = False
                self.move = True
                self.pop_up_quadro = False

        #==========================MINIGAME MEMORIA======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(lustre):
            efeito_pop_up.play()
            self.minigame_memoria = True
            self.move = False
            self.pops = True

        if self.minigame_memoria:
            self.memoria.win_memoria = self.memoria.mostrar_obejtos()
            if self.memoria.perdi:
                self.memoria = Memoria(self.janela, "lustre")
            if Window.keyboard.key_pressed("esc") and self.player.collided(lustre):
                self.minigame_memoria = False
        
        if self.memoria.win_memoria:
            self.minigame_memoria = False
            fundo_pop.draw()
            ordem.draw()
            if Window.keyboard.key_pressed("esc") and self.player.collided(lustre):
                efeito_pop_up.play()
                self.pops = False
                self.move = True
                self.memoria.win_memoria = False
        
        #==========================MESA POP======================================

        if Window.keyboard.key_pressed("e") and self.player.collided(mesa_jantar):
            efeito_pop_up.play()
            self.pop_up_mesa = True
            self.move = False
            self.pops = True
        
        if self.pop_up_mesa:
            mesa_pop.draw()
            bolsa.draw()
            self.bussulas_list[self.bussula_indice].draw()
            if Window.mouse.is_over_object(bussula) and Window.mouse.is_button_pressed(1):
                self.bussulas = True
            
            if self.bussulas:
                self.timer += self.janela.delta_time()

            if self.timer > 1:
                self.bussula_indice += 1
                self.timer = 0
                if self.bussula_indice == 4:
                    self.bussula_indice = 0
                    self.bussulas = False

            if Window.keyboard.key_pressed("esc") and self.player.collided(mesa_jantar):
                efeito_pop_up.play()
                self.pops = False
                self.move = True
                self.minigame_bolsa = False
                self.pop_up_mesa = False
            
            if Window.mouse.is_over_object(bolsa) and Window.mouse.is_button_pressed(1):
                efeito_pop_up.play()
                self.minigame_bolsa = True
        
        #==========================MINIGAME CROSSWORDS======================================

        if self.minigame_bolsa:
            if self.diquinha == "cruz":
                self.dica = True
                dica_type = "cruz"
                self.diquinha = ""
            self.move = False
            fundo_pop.draw()
            crossword.draw()
            one.draw()
            two.draw()
            three.draw()
            four.draw()
            word = self.primeira.palavra[:5]
            word2 = self.segunda.palavra[:8]
            word3 = self.terceira.palavra[:5]
            word4 = self.final.palavra[:5]
            for i in range(len(word)):
                self.janela.draw_text(word[i], 515, 130 + 54*i, 50)

            for i in range(len(word2)):
                self.janela.draw_text(word2[i], 460 + 54*i, 184, 50)

            for i in range(len(word3)):
                self.janela.draw_text(word3[i], 515 + 54*i, 294, 50)

            for i in range(len(word4)):
                self.janela.draw_text(word4[i], 730, 130 + 54*i, 50)

            if Window.mouse.is_over_object(one) and Window.mouse.is_button_pressed(1):
                self.um = True
                self.dois = False
                self.tres = False
                self.quatro = False

            if Window.mouse.is_over_object(two) and Window.mouse.is_button_pressed(1):
                self.dois = True
                self.um = False
                self.tres = False
                self.quatro = False

            if Window.mouse.is_over_object(three) and Window.mouse.is_button_pressed(1):
                self.tres = True
                self.um = False
                self.dois = False
                self.quatro = False
            
            if Window.mouse.is_over_object(four) and Window.mouse.is_button_pressed(1):
                self.um = False
                self.dois = False
                self.tres = False
                self.quatro = True

            if self.um:
                if word == "certo":
                    mudaSprite("one")
                else:
                    self.primeira.input_letra("")  
            
            if self.dois:
                if word2 == "perigoso":
                    mudaSprite("two")
                else:
                    self.segunda.input_letra("")
                
            if self.tres:
                if word3 == "toque":
                    mudaSprite("three")
                else:
                    self.terceira.input_letra("")
            
            if self.quatro:
                if word4 == "poder":
                    mudaSprite("four")
                else:
                    self.final.input_letra("")
                
        #==========================MESA POP======================================  

        if Window.keyboard.key_pressed("e") and self.player.collided(carrinho):
            efeito_pop_up.play()
            self.pop_up_carrinho = True
            self.move = False
            self.pops = True
        
        if self.pop_up_carrinho:
            carrinho_pop.draw()
        
        if Window.keyboard.key_pressed("esc") and self.player.collided(carrinho):
            efeito_pop_up.play()
            self.pops = False
            self.move = True
            self.pop_up_carrinho = False

        #==========================DICAS======================================  
        
        
        self.timer_dica += self.janela.delta_time()
        if Window.mouse.is_over_object(duvida) and Window.mouse.is_button_pressed(1):
            if self.move:
                dica_type = "notpop"
            else:
                dica_type = "pop"
            if self.timer_dica >= 0.5 and not self.dica:
                self.dica = True
            elif self.timer_dica >= 0.5:
                self.dica = False
            self.timer_dica = 0
                
        if self.dica:
            if dica_type == "mudou":
                self.timer_dica += self.janela.delta_time()
            self.hint.dica(dica_type)

        duvida.draw()

        if self.pops:
            self.timer_menu = 0
        else:
            self.timer_menu += self.janela.delta_time()

        #===================PAUSE======================
        if self.timer_menu >= 0.2 and Window.keyboard.key_pressed("esc") and not self.pops:
            self.menu = True
        
        if self.menu:
            self.move = False
            fundo_pop.draw()
            menu.draw()
            retornar.draw()
            sair.draw()
            if Window.mouse.is_over_object(retornar) and Window.mouse.is_button_pressed(1):
                self.move = True
                self.menu = False
            if Window.mouse.is_over_object(sair) and Window.mouse.is_button_pressed(1):
                self.sair = True

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
        carrinho.draw()
        if lustre in self.objetos_jantar:
            lustre.draw()
        