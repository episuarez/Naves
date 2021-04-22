import random

from Player import Player
from Enemigo import Enemigo

class Juego():
    gameover = False;

    def __init__(self, numero_enemigos=10, tamanno=(15, 40)):
        self.tamanno = tamanno;
        self.pantalla = [];
        self.generar_pantalla();

        self.player = Player("O", 14, 20);

        self.enemigos = [];
        self.posiciones_iniciales_enemigos = random.sample([numero for numero in range(0, 40) if numero % 2 == 0], numero_enemigos);

        for posicion in range(0, int(numero_enemigos / 2)):
            self.enemigos.append(Enemigo("V", 1, self.posiciones_iniciales_enemigos[posicion]));

        for posicion in range(int(numero_enemigos / 2), numero_enemigos):
            self.enemigos.append(Enemigo("V", 3, self.posiciones_iniciales_enemigos[posicion]));

    def generar_pantalla(self):
        for _ in range(0, self.tamanno[0]):
            listaTMP = [];
            for _ in range(0, self.tamanno[1]):
                listaTMP.append(" ");
            self.pantalla.append(listaTMP);

    def relleno_pantalla(self):
        self.limpiar_pantalla();

        self.pantalla[self.player.posicion.x][self.player.posicion.y] = self.player.caracter;

        for enemigo in self.enemigos:
            self.pantalla[enemigo.posicion.x][enemigo.posicion.y] = enemigo.caracter;
            for disparo in enemigo.disparos:
                self.pantalla[disparo.posicion.x][disparo.posicion.y] = disparo.caracter;

        for disparo in self.player.disparos:
            self.pantalla[disparo.posicion.x][disparo.posicion.y] = disparo.caracter;

    def limpiar_pantalla(self):
        for y in range(0, self.tamanno[0]):
            for x in range(0, self.tamanno[1]):
                self.pantalla[y][x] = " ";

    def obtener_pantalla(self):
        self.relleno_pantalla();

        contenido = "";

        contenido += "Juego de Naves hecho en Twitch\n";
        contenido += f"Puntos: {self.player.puntos}\n\n";
        
        contenido += "-" * ((self.tamanno[1] * 2) + 2) + "\n";

        for fila in self.pantalla:
            contenido += "|";
            for valor in fila:
                contenido += f"{valor} ";
            contenido += "|\n";

        contenido += "-" * ((self.tamanno[1] * 2) + 2) + "\n";

        return contenido;