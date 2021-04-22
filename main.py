import os
import msvcrt
import cursor
import time
import threading

from Juego import Juego

cursor.hide();
os.system("cls");

juego = Juego();

def gestion_enemigos():
    while not juego.gameover:
        for enemigo in juego.enemigos:
            enemigo.update();
            juego.gameover = enemigo.update_disparos(juego.player.posicion);

        time.sleep(0.5);

def gestion_disparos():
    while not juego.gameover:
        juego.player.update_disparos(juego.enemigos);

        time.sleep(0.1);

hilo_enemigos = threading.Thread(target=gestion_enemigos);
hilo_disparos = threading.Thread(target=gestion_disparos);

hilo_enemigos.start();
hilo_disparos.start();

while not juego.gameover:
    if msvcrt.kbhit():
        tecla = msvcrt.getch();
        juego.player.update(tecla);

    print("\033[%d;%dH" % (0, 0));
    print(juego.obtener_pantalla());

os.system("cls");
print(f"¡Has perdido! Con tantos puntos {juego.player.puntos}");