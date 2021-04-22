import random

from GameObject import GameObject
from Disparo import Disparo

class Enemigo(GameObject):
    def __init__(self, caracter, x, y):
        super().__init__(caracter, x, y);
        self.direcion = 0;

        self.disparos = [];

    def update(self):
        if self.direcion == 0:
            self.posicion.y += 1;
            self.direcion = 1;
        elif self.direcion == 1:
            self.posicion.y -= 1;
            self.direcion = 0;

        if random.randint(0, 100) > 90:
            self.disparos.append(Disparo("J", self.posicion.x + 1, self.posicion.y, 1));

    def update_disparos(self, posicion_player):
        for disparo in self.disparos:
            disparo.update();

            if posicion_player.x == disparo.posicion.x and posicion_player.y == disparo.posicion.y:
                self.disparos.remove(disparo);
                return True;

            if disparo.posicion.x < 0 or disparo.posicion.x > 14:
                self.disparos.remove(disparo);