from GameObject import GameObject
from Disparo import Disparo

class Enemigo(GameObject):
    def __init__(self, caracter, x, y):
        super().__init__(caracter, x, y);

        self.disparos = [];

    def update(self):
        pass;

    def update_disparos(self):
        for disparo in self.disparos:
            disparo.update();

            if disparo.posicion.x < 0 or disparo.posicion.x > 14:
                self.disparos.remove(disparo);