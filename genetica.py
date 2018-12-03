import random
import string

random.seed(13)

class Genetico:

	def __init__(self,generador,objetivo,number_children = 10, number_sampling = 5 ,iteraciones = 1000):
		self.generador = generador
		self.objetivo = objetivo
		self.number_children = number_children
		self.number_sampling = number_sampling
		self.iteraciones = iteraciones

	def iniciar(self,largo,cantidad):
		lista = []
		for i in range(cantidad):
			objeto = ""
			for j in range(largo):
				objeto += str(self.generador())
			lista.append(objeto)
		return lista

	def compararByte(self,byte1, byte2):
		cantidad = 0
		for indice in range(len(byte1)):
			if(byte1[indice] == byte2[indice]):
				cantidad += 1
		return cantidad

	def evaluar(self,objetivo, generados):
		aux = []
		mejor = None
		mejor_fit = -1
		for indice in range(len(generados)):
			fit = self.compararByte(objetivo,generados[indice])
			for indice2 in range(fit + 1):
				aux.append(generados[indice])
			if(fit > mejor_fit):
				mejor_fit = fit
				mejor = generados[indice]
		return aux,mejor

	def torneo(self,generados_evaluados, comparaciones,objetivo):
		best = None
		best_fit = -1
		for indice in range(comparaciones):
			aux = random.choice(generados_evaluados)
			aux_fit = self.compararByte(objetivo,aux)
			if(best == None or (aux_fit > best_fit)):
				best = aux
				best_fit = aux_fit
		return best

	def generarHijos(self,padre1,padre2,cantidad):
		hijos = []
		probabilidad_mutation = 1
		for indice in range(cantidad):
			punto = random.randint(0, len(padre1) - 1)
			nuevo_hijo = padre1[:punto] + padre2[punto:]
			hijo = ""
			for letra in nuevo_hijo:
				if(random.randint(1, 100) <= probabilidad_mutation):
					hijo += str(self.generador())
				else:
					hijo += letra
			hijos.append(hijo)
		return hijos
	def run(self):
		largo = len(objetivo)
		aleatorios = self.iniciar(largo,self.number_children)
		j = 0
		while(self.iteraciones > j):
			j += 1
			aleatorios_evaluados,mejor = self.evaluar(self.objetivo,aleatorios)
			if(mejor == objetivo):
				print ("encontro")
				print (mejor)
				break
			padre1 = self.torneo(aleatorios_evaluados,self.number_sampling,self.objetivo)
			padre2 = self.torneo(aleatorios_evaluados,self.number_sampling,self.objetivo)
			aleatorios = self.generarHijos(padre1,padre2,self.number_children)
		print (j)

def generator_string_number():
	return random.choice(string.ascii_lowercase + ' ' + string.digits)

def generator_string():
	return random.choice(string.ascii_lowercase + ' ')

def generator_byte():
	return random.randint(0, 1)

objetivo = "111001010101010101001010"
genetico = Genetico(generator_byte,objetivo,number_children = 10,number_sampling= 5,iteraciones = 10000)
genetico.run()


