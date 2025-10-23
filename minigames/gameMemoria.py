from pplay.window import *
from pplay.sprite import *

class Memoria():
    def __init__(self, objetos):
        self.lista_obj = objetos

    def mostrar_obejtos(self):
        for i in range(len(self.lista_obj)):
            self.lista_obj[i] = Sprite("assets\\sprites\\circulo_apagado.png")