from pplay.window import *
from pplay.sprite import *
from pplay.keyboard import *

class Movimentacao():
    def __init__(self, player, janela):
        self.speed = 100
        self.player = player
        self.janela = janela

    def verify_colision(self, lista_objetos):
        for objeto in lista_objetos:
            if self.player.collided(objeto):
                return True
        return False
                    

    def moviment(self, lista_objetos):
        if (Window.keyboard.key_pressed("w") or Window.keyboard.key_pressed("UP")) and (self.player.y + 130 > 160):
            self.player.y -= self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.player.y += self.speed * self.janela.delta_time()
    
        if (Window.keyboard.key_pressed("s") or Window.keyboard.key_pressed("DOWN")) and (self.player.y+100 < self.janela.height):
            self.player.y += self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.player.y -= self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("d") or Window.keyboard.key_pressed("RIGHT")) and (self.player.x+60 < self.janela.width):
            self.player.x += self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.player.x -= self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("a") or Window.keyboard.key_pressed("LEFT")) and (self.player.x+33 > 0):
            self.player.x -= self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.player.x += self.speed * self.janela.delta_time()
