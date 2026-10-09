from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3


class Planeta:

    def __init__(self, nombre=None, cantidad_satelites=0, masa=0,
                 volumen=0, diametro=0, distancia_sol=0,
                 tipo=None, observable=False):

        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable

    def imprimir(self):
        print("Nombre del planeta =", self.nombre)
        print("Cantidad de satélites =", self.cantidad_satelites)
        print("Masa del planeta =", self.masa)
        print("Volumen del planeta =", self.volumen)
        print("Diámetro del planeta =", self.diametro)
        print("Distancia al Sol =", self.distancia_sol)
        print("Tipo de planeta =", self.tipo.name)
        print("Es observable =", self.observable)

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        ua = 149597870
        limite = ua * 3.4

        if self.distancia_sol > limite:
            return True
        else:
            return False


p1 = Planeta(
    "Tierra",
    1,
    5.9736E24,
    1.08321E12,
    12742,
    150000000,
    TipoPlaneta.TERRESTRE,
    True
)

p1.imprimir()
print("Densidad del planeta =", p1.calcular_densidad())
print("Es planeta exterior =", p1.es_planeta_exterior())

print()

p2 = Planeta(
    "Júpiter",
    79,
    1.899E27,
    1.4313E15,
    139820,
    750000000,
    TipoPlaneta.GASEOSO,
    True
)

p2.imprimir()
print("Densidad del planeta =", p2.calcular_densidad())
print("Es planeta exterior =", p2.es_planeta_exterior())
