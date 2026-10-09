from enum import Enum


class Combustible(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"


class TipoAutomovil(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"


class Automovil:

    def __init__(self, marca, modelo, motor, combustible, tipo,
                 puertas, asientos, velocidad_maxima, color,
                 velocidad_actual):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getMotor(self):
        return self.motor

    def getCombustible(self):
        return self.combustible

    def getTipo(self):
        return self.tipo

    def getPuertas(self):
        return self.puertas

    def getAsientos(self):
        return self.asientos

    def getVelocidadMaxima(self):
        return self.velocidad_maxima

    def getColor(self):
        return self.color

    def getVelocidadActual(self):
        return self.velocidad_actual

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMotor(self, motor):
        self.motor = motor

    def setCombustible(self, combustible):
        self.combustible = combustible

    def setTipo(self, tipo):
        self.tipo = tipo

    def setPuertas(self, puertas):
        self.puertas = puertas

    def setAsientos(self, asientos):
        self.asientos = asientos

    def setVelocidadMaxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def setColor(self, color):
        self.color = color

    def setVelocidadActual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, velocidad):
        if self.velocidad_actual + velocidad <= self.velocidad_maxima:
            self.velocidad_actual += velocidad
        else:
            print("No se puede superar la velocidad máxima.")

    def desacelerar(self, velocidad):
        if self.velocidad_actual - velocidad >= 0:
            self.velocidad_actual -= velocidad
        else:
            print("La velocidad no puede ser menor que cero.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo(self, distancia):
        if self.velocidad_actual != 0:
            return distancia / self.velocidad_actual
        else:
            return None

    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Tipo de combustible =", self.combustible.name)
        print("Tipo de automóvil =", self.tipo.name)
        print("Número de puertas =", self.puertas)
        print("Cantidad de asientos =", self.asientos)
        print("Velocidad máxima =", self.velocidad_maxima)
        print("Color =", self.color.name)
        print("Velocidad actual =", self.velocidad_actual)


automovil1 = Automovil(
    "Toyota",
    2022,
    2.0,
    Combustible.GASOLINA,
    TipoAutomovil.SUV,
    5,
    5,
    200,
    Color.ROJO,
    100
)

automovil1.imprimir()

automovil1.acelerar(20)
print("Velocidad actual =", automovil1.getVelocidadActual())

automovil1.desacelerar(50)
print("Velocidad actual =", automovil1.getVelocidadActual())

automovil1.frenar()
print("Velocidad actual =", automovil1.getVelocidadActual())
