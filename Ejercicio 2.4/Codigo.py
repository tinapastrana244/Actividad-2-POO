import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        hipotenusa = self.calcular_hipotenusa()
        return self.base + self.altura + hipotenusa

    def determinar_tipo(self):
        hipotenusa = self.calcular_hipotenusa()

        if self.base == self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            print("Es un triángulo isósceles")
        else:
            print("Es un triángulo escaleno")


circulo1 = Circulo(4)
print("Área del círculo:", circulo1.calcular_area())
print("Perímetro del círculo:", circulo1.calcular_perimetro())

rectangulo1 = Rectangulo(5, 3)
print("Área del rectángulo:", rectangulo1.calcular_area())
print("Perímetro del rectángulo:", rectangulo1.calcular_perimetro())

cuadrado1 = Cuadrado(6)
print("Área del cuadrado:", cuadrado1.calcular_area())
print("Perímetro del cuadrado:", cuadrado1.calcular_perimetro())

triangulo1 = TrianguloRectangulo(3, 4)
print("Área del triángulo:", triangulo1.calcular_area())
print("Perímetro del triángulo:", triangulo1.calcular_perimetro())
print("Hipotenusa del triángulo:", triangulo1.calcular_hipotenusa())
triangulo1.determinar_tipo()
