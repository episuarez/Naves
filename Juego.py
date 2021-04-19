from GameObject import GameObject

class Juego():
    def __init__(self, tamanno=(15, 40)):
        self.tamanno = tamanno;
        self.pantalla = [];
        self.generar_pantalla();

        self.player = GameObject("O", 14, 20);

    def generar_pantalla(self):
        for _ in range(0, self.tamanno[0]):
            listaTMP = [];
            for _ in range(0, self.tamanno[1]):
                listaTMP.append(" ");
            self.pantalla.append(listaTMP);

    def relleno_pantalla(self):
        self.limpiar_pantalla();

        self.pantalla[self.player.posicion.x][self.player.posicion.y] = self.player.caracter;

    def limpiar_pantalla(self):
        for y in range(0, self.tamanno[0]):
            for x in range(0, self.tamanno[1]):
                self.pantalla[y][x] = " ";

    def obtener_pantalla(self):
        self.relleno_pantalla();

        print(self.player.posicion.x, self.player.posicion.y);
        print(self.pantalla);

        contenido = "";

        contenido += "Juego de Naves hecho en Twitch\n";
        contenido += "Puntos: 0\n\n";
        
        contenido += "-" * ((self.tamanno[1] * 2) + 2) + "\n";

        for fila in self.pantalla:
            contenido += "|";
            for valor in fila:
                contenido += f"{valor} ";
            contenido += "|\n";

        contenido += "-" * ((self.tamanno[1] * 2) + 2) + "\n";

        return contenido;