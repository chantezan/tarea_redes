# Perceptron
import random
import math
import matplotlib.pyplot as plt

class Perceptron:


    def __init__(self, dimensiones, es_salida=False):
        self.anteriores = []
        self.siguientes = []
        self.salida = 0
        self.delta = 0
        self.error = 0
        self.dimensiones = 0
        self.peso = []
        self.learning_rate = 0.1
        es_salida = False
        self.dimensiones = dimensiones
        for i in range(dimensiones):
            self.peso.append(random.uniform(-1, 1))
        self.bias = random.uniform(-1, 1)
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


# Sigmoid

class Sigmoid(Perceptron):
  def funcion_activacion(self,x):
    aux = 0
    for i in range(self.dimensiones):
      aux += self.peso[i] * x[i]
    return 1/(1 + math.exp(-(aux + self.bias)))


import copy


class Red:
    def __init__(self, dim_input=2, capas=1, activacion=["sigmoid"], cantidad=[2], dim_output = 1):
        dimension = dim_input
        self.capas = []
        self.errores = []
        lista_anterior = []
        for i in range(capas):
            if (activacion[i] == "sigmoid"):
                neurona = Sigmoid
            else:
                neurona = Perceptron
            lista_neuronas = []
            for j in range(cantidad[i]):
                neurona_aux = neurona(dimension)
                lista_neuronas.append(neurona_aux)
                if (lista_anterior):
                    for neurona_anterior in lista_anterior:
                        neurona_aux.anteriores.append(neurona_anterior)
                        neurona_anterior.siguientes.append(neurona_aux)
            self.capas.append(lista_neuronas)
            lista_anterior = lista_neuronas.copy()
            dimension = cantidad[i]
        neuronas_salidas = []
        for i in range(dim_output):
            neurona_aux = neurona(dimension, es_salida=True)
            for neurona_anterior in lista_anterior:
                neurona_aux.anteriores.append(neurona_anterior)
                neurona_anterior.siguientes.append(neurona_aux)
            neuronas_salidas.append(neurona_aux)
        self.capas.append(neuronas_salidas)

    def forward(self, entradas):
        primera = True
        salidas = []
        for neuronas_capa_i in self.capas:
            for neurona_capa_i in neuronas_capa_i:
                if (primera):
                    neurona_capa_i.alimentar_input(entradas)
                else:
                    neurona_capa_i.alimentar()
            primera = False
        for neurona in neuronas_capa_i:
            salidas.append(neurona.salida)
        return salidas

    def backprogration(self, salidas_esperadas,salidas):
        primera = True
        index_neurona = 0
        for indice in range(1, len(self.capas) + 1):
            for neurona_capa_i in self.capas[-indice]:
                if (primera):
                    neurona_capa_i.calcular_delta_with_input(salidas_esperadas[index_neurona] - salidas[index_neurona])
                else:
                    neurona_capa_i.calcular_delta()
            primera = False

    def aprender(self, entradas):
        primera = True
        for neuronas_capa_i in self.capas:
            for neurona_capa_i in neuronas_capa_i:
                if (primera):
                    neurona_capa_i.aprender_with_input(entradas)
                else:
                    neurona_capa_i.aprender()
            primera = False

    def entrenar(self, entradas, salidas_esperadas, epocas=100):
        epoca = 0
        while(epoca < epocas):
            indice = 0
            error = 0
            for entrada in entradas:
                salidas = self.forward(entrada)
                self.backprogration(salidas_esperadas[indice], salidas)
                self.aprender(entrada)
                for i_salida in range(len(salidas)):
                    error = error + (salidas_esperadas[indice][i_salida] - salidas[i_salida])
                indice = indice + 1

            self.errores.append(error**2)
            epoca = epoca + 1
            #print(epoca)
        print (self.errores)

    def test(self,entradas,salidas_esperadas):
        error = 0
        index = 0
        for entrada in entradas:
            index_salida = 0
            for salida in self.forward(entrada):
                error = error + ((salidas_esperadas[index][index_salida] - salida)**2)**0.5
                index_salida = index_salida + 1
            index = index + 1
        print("error es " + str(error))
        return error

    def imprmirError(self,neuronas,epocas):
        plt.title("Neuronas "+ str(neuronas) + " epocas " + str(epocas))
        plt.plot(range(0, len(self.errores)), self.errores)
        plt.axis([0,len(self.errores),0,1])
        plt.show()


