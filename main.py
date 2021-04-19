import os
import time
import cursor

from Juego import Juego

juego = Juego();
cursor.hide();


os.system("cls");

print("\033[%d;%dH" % (0, 0));

print(juego.obtener_pantalla());

time.sleep(1);