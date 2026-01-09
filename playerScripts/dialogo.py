from pplay.window import *

class Dialogue():
    def __init__(self, janela):
        self.janela = janela
        self.timer = 0
        self.indice = 0
        self.fala = ""
    
    def conversa(self, texto):
        self.timer += self.janela.delta_time()
        match texto:
            case 0:
                script = "Ai, minha cabeça. Onde eu estou?"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
                    
            case 1:
                script = "Olá jogador."
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
            
            case 2:
                script = "Jogador? Como assim? Onde eu estou?"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
            
            case 3:
                script = "Seja bem vindo ao grande jogo."
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(3.1):
                        return True
            
            case 3.1:
                script = "O seu objetivo é simples:"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,550,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(3.2):
                        return True
            
            case 3.2:
                script = "Escape o mais rápido possível"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,580,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(3.3):
                        return True
            
            case 3.3:
                script = "e ganhe o grande prêmio."
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,610,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
            
            case 3.4:
                script = "Para escapar é simples:"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(3.5):
                        return True
            
            case 3.5:
                script = "Insira as 3 palavras certas na TV."
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,550,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(3.6):
                        return True
            
            case 3.6:
                script = "As dicas das palavras estão"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,580,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(3.7):
                        return True
            
            case 3.7:
                script = "espalhadas pela sala"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,610,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
            
            case 4.4:
                script = "Como assim? Que prêmio?"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
            
            case 5.4:
                script = "Ande com WASD. Em caso de dúvidas"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,520,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(5.1):
                        return True
            
            case 5.1:
                script = "botão esquerdo do mouse na interrogação"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,550,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(5.2):
                        return True
            
            case 5.2:
                script = "no canto superior direito da tela."
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,580,30,(255,255,255))
                if self.fala == script:
                    if self.conversa(5.3):
                        return True
            
            case 5.3:
                script = "Seu tempo começa agora. Boa sorte!"
                if self.timer >= 0.1 and self.indice < len(script):
                    self.indice += 1
                    self.timer = 0
                self.fala = script[:self.indice]
                self.janela.draw_text(self.fala, 410,610,30,(255,255,255))
                if self.fala == script:
                    if self.fimTexto():
                        return True
    
    def fimTexto(self):
        #self.janela.draw_text("==============PRESSIONE ESPAÇO==============", 470,670,15,(255,255,255))
        if Window.keyboard.key_pressed("space"):
            self.indice = 0
            self.fala = ""
            return True