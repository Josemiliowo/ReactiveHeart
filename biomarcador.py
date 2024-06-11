import itertools
from  collections import Counter

class Biomarcador:
    def __init__(self, nombre, enfermedades, valorEstable):
        self.nombre = nombre
        self.enfermedades = enfermedades
        self.valorEstable = valorEstable

    def getNombre(self):
        return self.nombre

    def getValorEstable(self):
        return self.valorEstable

    def getEnfermedades(self):
        return self.enfermedades

    def __str__(self):
        return f"{self.nombre}"

    def __repr__(self):
        return f"{self.nombre}"

