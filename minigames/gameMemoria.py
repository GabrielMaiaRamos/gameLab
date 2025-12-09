from pplay.window import *
from pplay.sprite import *
from random import choices

fundo_pop = Sprite("assets\\sprites\\fundo_pop.png")

class Memoria():
    def __init__(self, janela, tipo):
        self.janela = janela
        self.lista_obj = []
        self.tipo = tipo #LUSTRE OU LIVROS
        self.stand_by = True  #verifica se clicu ou se tem que esperar o click
        self.mouse_timer = 0  #tic do mouse

        #logica de timer pra piscar os objetos 
        self.timer = 0
        self.on = False
        self.acendido=0
        
        #lista aleatoria de objetos que vao piscar (a ordem da lista criada ja é a ordem que o player deve seguir)
        self.lista_aleatorios = choices([0,1,2,3,4], k=5)

        #contagem da fase pra verificar quantos tem que piscar
        self.fase = 1
        #contagem de acertos do player (que devem ser igual ao numero da fase pra passar de fase)
        self.acertos = 0
        self.win_memoria = False
        self.perdi = False

        self.win = False


    #=====[FUNCAO QUE SEMPRE MOSTRA OS OBJETOS, BEM SIMPLES]
    def mostrar_obejtos(self):
        fundo_pop.draw()
        if self.tipo == "lustre":
            for i in range(5):
                self.lista_obj.append(Sprite("assets\\sprites\\circulo_apagado.png"))
                self.lista_obj[i].set_position(500 + 60*i, 360)
                self.lista_obj[i].draw()

                # TENTATIVA DE FAZER DESTACAR ONDE O MOUSE TA EM CIMA
                if not self.stand_by:
                    if Window.mouse.is_over_object(self.lista_obj[i]):
                        self.lista_obj[i] = Sprite("assets\\sprites\\circulo_is_over.png")
                    else:
                        self.lista_obj[i] = (Sprite("assets\\sprites\\circulo_apagado.png"))
                self.lista_obj[i].set_position(500 + 60*i, 360)

        elif self.tipo == "livros":
            pass #imitar a logica dos pontos

        #Essa funcao mesma ja puxa outras duas sempre
        if self.win:
            return True
        self.win = self.verifica_acerto()
        self.controle_de_ticks()
    
    #=====[FUNCAO DE VERIFICAR SE ACERTOU A SEQUENCIA]
    def verifica_acerto(self):
        self.mouse_timer += self.janela.delta_time() #aumenta o delay do mouse

        if self.mouse_timer > 0.5: #verifica se esta em um delay aceitavel
            #se clicar SOBRE o seguinte: lista_objetos[lista_aleatorios[acerto atual]] ou seja, pega o elemento de indice ACERTO ATUAL da lista gerada aleatoriamente
            # e envia isso como INDICE da lista de sprites (é justamente o uso que eu queria com a lista de aleatorios, a ideia é guardar indices que serao usados na lista
            # de sprtes)
            if Window.mouse.is_over_object(self.lista_obj[self.lista_aleatorios[self.acertos]]) and Window.mouse.is_button_pressed(1):
                self.acertos += 1     #aumenta o acerto atual (ou seja, a proxima verificacao desse if ja muda pro proximo indice da lista)
                self.mouse_timer = 0
            elif not Window.mouse.is_over_object(self.lista_obj[self.lista_aleatorios[self.acertos]]) and Window.mouse.is_button_pressed(1):
                self.perdi = True  #usa la no salaJantar pra criar um novo objeto dessa classe (reiniciar tudo)
                self.mouse_timer=0

            if self.acertos == 5:
                return True
                
        #se eu somei acertos == ao numero da fase, posso passar de fase
        if self.acertos == self.fase:
            self.acertos=0 #zero os acertos, pois em toda a fase tem que acertar do inicio ate o ultimo a piscar
            self.fase += 1
            self.stand_by = True #ja comeca a proxima fase piscando




    #=====[LOGICA DE CONTROLE DA FUNCAO DE PISCAR AS LUZES]=====
    def controle_de_ticks(self):
        #se a quantidade de luzes ja acendidas for menor que o numero da fase E o player nao estiver em um momento de clicar (estiver esperando a sequencia toda) entao eu
        # devo continuar mostrando
        if (self.acendido < self.fase and self.stand_by):
            self.acender_objetos(self.acendido) #passo acendido como parametro pra continuar piscando a partir dele, e nao repetir toda vez
        #mas, se a quantidade de acendidos for igual ao numero da fase, entao ja pisquei todos que deveria
        elif self.acendido == self.fase:
            self.acendido = 0 #zero os acendidos pra poder piscar todos de novo na proxima fase
            self.stand_by=False  #agora o player deve clicar em algo, ent o momento de espera acaba




    #=====[LOGICA DE PISCAR AS LUZES]=====
    def acender_objetos(self,objeto):
        self.timer += self.janela.delta_time()

        #SE ESTIVER ACESO E TIVER PASSADO DO TEMPO, APAGA
        if self.on and self.timer >= 0.25:
            self.on = False
            self.timer = 0
            self.acendido += 1

        #SE ESTIVER APAGADO E TIVER PASSADO DO TEMPO, ACENDE
        elif not self.on and self.timer >= 0.25:
            self.on = True
            self.timer = 0

        #SE ESTIVER ON, O SPRITE DO "OBJETO" É O ACESO
        if self.on:
            self.lista_obj[self.lista_aleatorios[objeto]] = Sprite("assets\\sprites\\circulo_aceso.png")
        #SE ESTIVER OFF, O SPRITE DO "OBJETO" É O APAGADO
        elif not self.on:
            self.lista_obj[self.lista_aleatorios[objeto]] = Sprite("assets\\sprites\\circulo_apagado.png")

