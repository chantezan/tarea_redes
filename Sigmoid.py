import random
import math
from Perceptron import Perceptron

class Sigmoid(Perceptron):
  def funcion_activacion(self,x):
    aux = 0
    for i in range(self.dimensiones):
      aux += self.peso[i] * x[i]
    return 1/(1 + math.exp(-(aux + self.bias)))