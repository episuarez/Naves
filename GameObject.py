from Vector2D import Vector2D

class GameObject():
    def __init__(self, caracter, x, y):
        self.caracter = caracter;
        self.posicion = Vector2D(x, y);
