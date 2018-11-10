import random
import math
class Perceptron:
    def __init__(self, dimensiones, es_salida=False):
        self.anteriores = []
        self.siguientes = []
        self.salida = 0
        self.delta = 0
        self.fallos = 0
        self.dimensiones = 0
        self.peso = []
        self.learning_rate = 1
        es_salida = False
        self.dimensiones = dimensiones
        for i in range(dimensiones):
            self.peso.append(random.uniform(-2, 2))
        self.bias = random.uniform(-2, 2)
        self.es_salida = es_salida

    def funcion_activacion(self, x):
        aux = 0
        for i in range(self.dimensiones):
            aux += self.peso[i] * x[i]
        if (aux + self.bias > 0):
            return 1
        else:
            return 0

    def aprender_with_input(self, entradas):
        for i in range(self.dimensiones):
            self.peso[i] = self.peso[i] + self.learning_rate * entradas[i] * self.delta
        self.bias += self.learning_rate * self.delta

    def aprender(self):
        for i in range(self.dimensiones):
            self.peso[i] = self.peso[i] + self.learning_rate * self.anteriores[i].salida * self.delta
        self.bias += self.learning_rate * self.delta

    def alimentar_input(self, entradas):
        self.error = 0
        self.salida = self.funcion_activacion(entradas)
        return self.salida

    def alimentar(self):
        entradas = []
        for anterior in self.anteriores:
            entradas.append(anterior.salida)
        return self.alimentar_input(entradas)

    def calcular_delta(self):
        self.delta = self.error * self.salida * (1 - self.salida)
        for indice in range(len(self.anteriores)):
            self.anteriores[indice].error += self.peso[indice] * self.delta

    def calcular_delta_with_input(self, error):
        self.error = error /2
        self.calcular_delta()
