import time

from GameObject import GameObject
from Disparo import Disparo

class Player(GameObject):
    def __init__(self, caracter, x, y):
        super().__init__(caracter, x, y);
        self.tiempo_disparo = 0;

        self.puntos = 0;
        self.disparos = [];

    def update(self, tecla):
        if str(tecla) == "b'M'":
            if self.posicion.y < 39:
                self.posicion.y += 1;
        if str(tecla) == "b'K'":
            if self.posicion.y > 0:
                self.posicion.y -= 1;

        if str(tecla) == "b'g'":
            if time.time() > self.tiempo_disparo + 0.5:
                self.tiempo_disparo = time.time();
                self.disparos.append(Disparo("J", self.posicion.x - 1, self.posicion.y, -1));

    def update_disparos(self, enemigos):
        for disparo in self.disparos:
            disparo.update();

            for enemigo in enemigos:
                if enemigo.posicion.x == disparo.posicion.x and enemigo.posicion.y == disparo.posicion.y:
                    enemigos.remove(enemigo);
                    self.disparos.remove(disparo);
                    self.puntos += 25;

            if disparo.posicion.x < 0 or disparo.posicion.x > 14:
                self.disparos.remove(disparo);
