from GameObject import GameObject

class Disparo(GameObject):
    def __init__(self, caracter, x, y, direccion):
        super().__init__(caracter, x, y);
        self.direccion = direccion;

    def update(self):
        self.posicion.x += self.direccion;