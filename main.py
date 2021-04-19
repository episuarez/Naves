import os
import msvcrt
import cursor
import time

from Juego import Juego

cursor.hide();
os.system("cls");

juego = Juego();

while True:

    if msvcrt.kbhit():
        tecla = msvcrt.getch();
        
        juego.player.update(tecla);

        for enemigo in juego.enemigos:
            enemigo.update();
            enemigo.update_disparos();

    juego.player.update_disparos(juego.enemigos);


    print("\033[%d;%dH" % (0, 0));
    print(juego.obtener_pantalla());

    time.sleep(0.1);