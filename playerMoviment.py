from pplay.window import *
from pplay.sprite import *
from pplay.keyboard import *

class Movimentacao():
    def __init__(self, player, janela):
        self.speedUP = 100
        self.speedDOWN = 100
        self.speedRIGHT = 100
        self.speedLEFT = 100
        self.player = player
        self.janela = janela

    def moviment(self):
        if (Window.keyboard.key_pressed("w") or Window.keyboard.key_pressed("UP")) and (self.player.y + 130 > 160):
            self.player.y -= self.speedUP * self.janela.delta_time()
        if (Window.keyboard.key_pressed("s") or Window.keyboard.key_pressed("DOWN")) and (self.player.y+100 < self.janela.height):
            self.player.y += self.speedDOWN * self.janela.delta_time()
        if (Window.keyboard.key_pressed("d") or Window.keyboard.key_pressed("RIGHT")) and (self.player.x+60 < self.janela.width):
            self.player.x += self.speedRIGHT * self.janela.delta_time()
        if (Window.keyboard.key_pressed("a") or Window.keyboard.key_pressed("LEFT")) and (self.player.x+33 > 0):
            self.player.x -= self.speedLEFT * self.janela.delta_time()
