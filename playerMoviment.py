from pplay.window import *
from pplay.sprite import *
from pplay.keyboard import *

class Movimentacao():
<<<<<<< Updated upstream
    def __init__(self, player, janela):
        self.speedUP = 100
        self.speedDOWN = 100
        self.speedRIGHT = 100
        self.speedLEFT = 100
=======
    def __init__(self, player, hitbox, janela):
        self.speed = 100
>>>>>>> Stashed changes
        self.player = player
        self.hitbox = hitbox
        self.janela = janela

<<<<<<< Updated upstream
    def moviment(self):
        if (Window.keyboard.key_pressed("w") or Window.keyboard.key_pressed("UP")) and (self.player.y+100 > 190):
            self.player.y -= self.speedUP * self.janela.delta_time()
        if (Window.keyboard.key_pressed("s") or Window.keyboard.key_pressed("DOWN")) and (self.player.y+100 < self.janela.height):
            self.player.y += self.speedDOWN * self.janela.delta_time()
        if (Window.keyboard.key_pressed("d") or Window.keyboard.key_pressed("RIGHT")) and (self.player.x+60 < self.janela.width):
            self.player.x += self.speedRIGHT * self.janela.delta_time()
        if (Window.keyboard.key_pressed("a") or Window.keyboard.key_pressed("LEFT")) and (self.player.x+33 > 0):
            self.player.x -= self.speedLEFT * self.janela.delta_time()
=======

    def verify_colision(self, lista_objetos):
        for objeto in lista_objetos:
            if self.hitbox.collided(objeto):
                return True
        return False
                    

    def moviment(self, lista_objetos):
        if (Window.keyboard.key_pressed("w") or Window.keyboard.key_pressed("UP")) and (self.hitbox.y+100 > 190):
            self.hitbox.y -= self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.y += self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("s") or Window.keyboard.key_pressed("DOWN")) and (self.hitbox.y+100 < self.janela.height):
            self.hitbox.y += self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.y -= self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("d") or Window.keyboard.key_pressed("RIGHT")) and (self.hitbox.x+60 < self.janela.width):
            self.hitbox.x += self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.x -= self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("a") or Window.keyboard.key_pressed("LEFT")) and (self.hitbox.x+33 > 0):
            self.hitbox.x -= self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.x += self.speed * self.janela.delta_time()


        self.player.x = self.hitbox.x - 8
        self.player.y = self.hitbox.y - 135
>>>>>>> Stashed changes
