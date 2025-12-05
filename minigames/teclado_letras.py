from pplay.window import *
from pplay.keyboard import *

pygame.init()

class Palavra():
    def __init__(self, janela):
        self.letra = ""

        self.palavra = ""
        self.janela = janela
        self.timer = -0.15

    def input_letra(self, caso):
        self.timer += self.janela.delta_time()
        
        if self.timer >= 0.15:
            if Window.keyboard.key_pressed("a"):
                self.letra = "a"
                self.timer = 0
            elif Window.keyboard.key_pressed("b"):
                self.letra = "b"
                self.timer = 0
            elif Window.keyboard.key_pressed("c"):
                self.letra = "c"
                self.timer = 0
            elif Window.keyboard.key_pressed("d"):
                self.letra = "d"
                self.timer = 0
            elif Window.keyboard.key_pressed("e"):
                self.letra = "e"
                self.timer = 0
            elif Window.keyboard.key_pressed("f"):
                self.letra = "f"
                self.timer = 0
            elif Window.keyboard.key_pressed("g"):
                self.letra = "g"
                self.timer = 0
            elif Window.keyboard.key_pressed("h"):
                self.letra = "h"
                self.timer = 0
            elif Window.keyboard.key_pressed("i"):
                self.letra = "i"
                self.timer = 0
            elif Window.keyboard.key_pressed("j"):
                self.letra = "j"
                self.timer = 0
            elif Window.keyboard.key_pressed("k"):
                self.letra = "k"
                self.timer = 0
            elif Window.keyboard.key_pressed("l"):
                self.letra = "l"
                self.timer = 0
            elif Window.keyboard.key_pressed("m"):
                self.letra = "m"
                self.timer = 0
            elif Window.keyboard.key_pressed("n"):
                self.letra = "n"
                self.timer = 0
            elif Window.keyboard.key_pressed("o"):
                self.letra = "o"
                self.timer = 0
            elif Window.keyboard.key_pressed("p"):
                self.letra = "p"
                self.timer = 0
            elif Window.keyboard.key_pressed("q"):
                self.letra = "q"
                self.timer = 0
            elif Window.keyboard.key_pressed("r"):
                self.letra = "r"
                self.timer = 0
            elif Window.keyboard.key_pressed("s"):
                self.letra = "s"
                self.timer = 0
            elif Window.keyboard.key_pressed("t"):
                self.letra = "t"
                self.timer = 0
            elif Window.keyboard.key_pressed("u"):
                self.letra = "u"
                self.timer = 0
            elif Window.keyboard.key_pressed("v"):
                self.letra = "v"
                self.timer = 0
            elif Window.keyboard.key_pressed("w"):
                self.letra = "w"
                self.timer = 0
            elif Window.keyboard.key_pressed("x"):
                self.letra = "x"
                self.timer = 0
            elif Window.keyboard.key_pressed("y"):
                self.letra = "y"
                self.timer = 0
            elif Window.keyboard.key_pressed("z"):
                self.letra = "z"
                self.timer = 0
            elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                self.letra = "BACKSPACE"
                self.timer = 0
        else:
            self.letra = ""
        
        self.mostrar_letra(caso)

    def mostrar_letra(self, caso):
        if self.letra == "BACKSPACE":
            self.palavra = self.palavra[:len(self.palavra)-1]
        else:
            self.palavra += self.letra
        if caso == "palpite":
            self.janela.draw_text(self.palavra, 470, 400 , 30)