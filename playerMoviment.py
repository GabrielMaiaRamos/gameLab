from pplay.window import *
from pplay.sprite import *
from pplay.keyboard import *

class Movimentacao():
    def __init__(self, player, hitbox, janela):
        self.speed = 170
        self.player = player
        self.hitbox = hitbox
        self.janela = janela


    def verify_colision(self, lista_objetos):
        #se a hitbox do player colidir com qualquer objeto da lista, retorna True
        for objeto in lista_objetos:
            if self.hitbox.collided(objeto):
                return True
        return False

    #verificacoes simples e diretas de movimento
    def moviment(self, lista_objetos):
        if (Window.keyboard.key_pressed("w") or Window.keyboard.key_pressed("UP")) and (self.hitbox.y > 170):
            self.hitbox.y -= self.speed * self.janela.delta_time()
            #para todas as direcoes: se verificar colisao com um objeto naquela direcao, faz a operacao inversa na posicao do y
            #assim, y do player continua = 0, sem se movimentar
            if self.verify_colision(lista_objetos):
                self.hitbox.y += self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("s") or Window.keyboard.key_pressed("DOWN")) and (self.hitbox.y + 15 < self.janela.height):
            self.hitbox.y += self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.y -= self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("d") or Window.keyboard.key_pressed("RIGHT")) and (self.hitbox.x+60 < self.janela.width):
            self.hitbox.x += self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.x -= self.speed * self.janela.delta_time()

        if (Window.keyboard.key_pressed("a") or Window.keyboard.key_pressed("LEFT")) and (self.hitbox.x > 0):
            self.hitbox.x -= self.speed * self.janela.delta_time()
            if self.verify_colision(lista_objetos):
                self.hitbox.x += self.speed * self.janela.delta_time()

        #posicao do player é igual o da hitbox com pequenas alteracoes de acordo com o sprite
        self.player.x = self.hitbox.x - 8
        self.player.y = self.hitbox.y - 135
