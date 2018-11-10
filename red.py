import pickle
import matplotlib.pyplot as plt
import time
import copy
from Perceptron import Perceptron
from Sigmoid import Sigmoid


class Red:
    def __init__(self, dim_input=2, capas=1, activacion=["sigmoid"], cantidad=[2], dim_output = 1):
        dimension = dim_input
        self.numero_salidas = dim_output
        self.capas = []
        self.errores = []
        self.presicion = []
        self.fallos = 0
        self.aciertos = 0
        self.errores_por_clase = []
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

    def entrenar(self, entradas, salidas_esperadas,entradas_test, salidas_esperadas_test ,epocas=100,guardar = False):
        epoca = 0
        inicio = time.time()

        while(epoca < epocas):
            indice = 0
            error = 0
            for entrada in entradas:
                salidas = self.forward(entrada)
                self.backprogration(salidas_esperadas[indice], salidas)
                self.aprender(entrada)
                for i_salida in range(len(salidas)):
                    error = error + ((salidas_esperadas[indice][i_salida] - salidas[i_salida])**2)**0.5
                indice = indice + 1

            presicion = self.test(entradas_test,salidas_esperadas_test)
            self.presicion.append(presicion)
            self.errores.append(error)
            epoca = epoca + 1
            if(epoca % 100 == 0):
                print("epoca " + str(epoca) + " tiempo " + str(time.time() - inicio) +"-------------------------------------------------------")
                inicio = time.time()
                self.detalleError()
                print (epoca,error)
                print (epoca,presicion)
                print ( 1.0 * self.aciertos/(1.0 * self.aciertos + self.fallos))
                if(guardar):
                    filehandler = open("red_neuronal", "wb")
                    pickle.dump(self,filehandler, pickle.HIGHEST_PROTOCOL)
                    #pickle.dump(self, filehandler)
            if(epoca % 500 == 0):
                self.imprmirError(10,epocas)


    def detalleError(self):
        for indice in range(len(self.errores_por_clase)):
            print("errores clase "+ str(indice))
            totales = self.errores_por_clase[indice][0] + self.errores_por_clase[indice][1]
            print("cantidad de errores " + str(totales))

            if(totales > 0):
                # deberian dar 1 pero su output es 0
                print("positivos falsos: " + str(1.0 * self.errores_por_clase[indice][1] / totales))
                # deberian dar 0 pero su output es 1
                print("falsos positivo: " + str(1.0 * self.errores_por_clase[indice][0] / totales))

    def test(self,entradas,salidas_esperadas):
        error = 0
        index = 0
        self.errores_por_clase = []
        for indice in range(self.numero_salidas):
            self.errores_por_clase.append([0,0])
        self.aciertos = 0
        self.fallos = 0
        totales = [0,0,0,0,0]
        for entrada in entradas:
            index_salida = 0
            acierto = True
            for salida in self.forward(entrada):
                dif = ((salidas_esperadas[index][index_salida] - salida)**2)**0.5
                error = error + dif
                if(dif > 0.5):
                    acierto = False
                    self.errores_por_clase[index_salida][salidas_esperadas[index][index_salida]] += 1
                index_salida = index_salida + 1
            if(acierto):
                self.aciertos = self.aciertos + 1
            else:
                self.fallos = self.fallos + 1
            index = index + 1
        #print("error es " + str(error))
        return error

    def imprmirError(self,neuronas,epocas):
        plt.title("Neuronas "+ str(neuronas) + " epocas " + str(epocas))
        plt.plot(range(0, len(self.errores)), self.errores)
        plt.show()
        plt.title("Neuronas " + str(neuronas) + " epocas " + str(epocas))
        plt.plot(range(0, len(self.errores)), self.presicion)
        plt.show()


