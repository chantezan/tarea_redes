from red import Red
import pickle
def normalizar(input,max,min):
    return 1.0*(input - min) / (1.0 * (max - min))
f=open("wine.csv", "r")
contents =f.readlines()

entradas = []
salidas = []
primera = True
max = [-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100]
min = [10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
total = [0,0,0,0,0]
for lineas in contents:
    dic = {3:0,4:0,5:1,6:2,7:3,8:4,9:4}
    x = lineas.split(";")
    if(primera):
        primera = False
    else:
        entradas.append([normalizar(float(x[0]),14.2,3.8),normalizar(float(x[1]),1.1,0.08),normalizar(float(x[2]),1.66,0),normalizar(float(x[3]),65.8,0.6),
                         normalizar(float(x[4]),0.346,.009),normalizar(float(x[5]),289.0,2.0),normalizar(float(x[6]),440.0,9.0),
                         normalizar(float(x[7]),1.04,0.99),normalizar(float(x[8]),3.82,2.72),normalizar(float(x[9]),1.08,0.22),normalizar(float(x[10]),14.2,8)])

        aux = [0,0,0,0,0,0,0]
        aux[dic[int(x[11])]] = 1
        total[dic[int(x[11])]] = total[dic[int(x[11])]] + 1
        salidas.append(aux)


entradas_train = entradas[:4500]
entradas_test = entradas[4500:]
salidas_train = salidas[:4500]
salidas_test = salidas[4500:]


neuronas = 5
epocas = 5000
red = Red(cantidad=[neuronas], activacion=["sigmoid"], dim_input=11, dim_output=5)
red.entrenar(entradas_train,salidas_train,entradas_test,salidas_test,epocas = epocas,guardar = True)



