import random
import string
import matplotlib.pyplot as plt
import time

class Genetico:

	def __init__(self,generador,objetivo,number_children = 10,iteraciones = 1000):
		self.generador = generador
		self.objetivo = objetivo
		self.number_children = number_children
		self.number_sampling = number_children * 3 / 4
		self.iteraciones = iteraciones
		self.valores = []
		self.promedios =  []

	def iniciar(self):
		lista = []
		suma = 0
		for i in range(self.number_children):
			objeto = []
			for j in range(self.objetivo):
				objeto.append(self.generador(self.objetivo))
			aux = self.fitness(objeto)
			suma += aux
			self.valores.append(aux)
			lista.append(objeto)
		self.promedios.append(suma * 1.0 / self.number_children)
		return lista

	def fitness(self,hijo):
		indice = 0
		no_libres = []
		for numero in hijo:
			libre = True
			terminar = False
			indice2 = indice + 1
			for numero2 in hijo[indice2:]:
				dif = indice2 - indice
				#print "comparando",numero,numero2
				if(numero == numero2):
					no_libres.append(indice)
					no_libres.append(indice2)
					break
				if(int(numero)+dif == int(numero2)):
						#print "diagonal",indice2,numero,numero2
					no_libres.append(indice)
					no_libres.append(indice2)
					terminar = True
					break
				if(int(numero)-dif == int(numero2)):
						#print "diagonal",indice2,numero,numero2
					no_libres.append(indice)
					no_libres.append(indice2)
					terminar = True
					break
				if(terminar):
					break
				indice2 += 1
			indice += 1
		#print no_libres
		return self.objetivo - len(set(no_libres))

	def torneo(self,generados_evaluados):
		best = None
		best_fit = -1
		for indice in range(self.number_sampling):
			aux = random.randint(0, self.number_children - 1)
			aux_fit = self.valores[aux]
			if(best == None or (aux_fit > best_fit)):
				best = aux
				best_fit = aux_fit
		return best

	def generarHijos(self,padre1,padre2):
		hijos = []
		probabilidad_mutation = 1
		self.valores = []
		suma = 0
		for indice in range(self.number_children):
			punto = random.randint(0, len(padre1) - 1)
			nuevo_hijo = padre1[:punto] + padre2[punto:]
			hijo = []
			for letra in nuevo_hijo:
				if(random.randint(1, 100) <= probabilidad_mutation):
					hijo.append(self.generador(self.objetivo))
				else:
					hijo.append(letra)
			aux = self.fitness(hijo)
			suma += aux
			self.valores.append(aux)
			hijos.append(hijo)
		self.promedios.append(suma * 1.0 / self.number_children)
		return hijos

	def run(self):
		tiempo_inicial = time.time()
		aleatorios = self.iniciar()
		j = 0
		while(self.iteraciones > j):
			terminar = False
			solucion = None
			indice = 0
			for fit in self.valores:
				if(fit == self.objetivo):
					solucion = aleatorios[indice]
					terminar = True
				indice += 1
			if(terminar):
				print "solucion encontrada",solucion
				break
			padre1 = self.torneo(aleatorios)
			padre2 = self.torneo(aleatorios)
			aleatorios = self.generarHijos(aleatorios[padre1],aleatorios[padre2])
			j += 1
		#print aleatorios
		plt.title(str(self.objetivo) + " Reinas - iteraciones: " + str(j) + "," + str(time.time() - tiempo_inicial)+"s")
        plt.plot(range(0, 1), [1])
        plt.show()

def generator_string_number():
	return random.choice(string.ascii_lowercase + ' ' + string.digits)

def generator_string():
	return random.choice(string.ascii_lowercase + ' ')

def generator_byte():
	return random.randint(0, 1)

def generador_queen(n):
	return random.randint(0, n-1)

for j in range(12):
	for i in range(4):
		seed = i + 15
		random.seed(seed) #17 objetivo 16
		objetivo = j + 4
		genetico = Genetico(generador_queen,objetivo,number_children = 200,iteraciones = 10000)
		print "seed-----------------------------------------------------------------",seed
		#print genetico.fitness("2031")
		#print genetico.fitness("2013")
		#print genetico.fitness("3102")
		genetico.run()


