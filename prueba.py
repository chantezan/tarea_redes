from red import Red

f=open("wine.csv", "r")
contents =f.readlines()

entradas = []

salidas = []
primera = True
for lineas in contents:
    #print (lineas)
    x = lineas.split(";")
    if(primera):
        primera = False
    else:
        entradas.append([float(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[4]),float(x[5]),float(x[6]),float(x[7]),float(x[8]),float(x[9]),float(x[10])])
        salidas.append([float(x[11])/10])

entradas_train = entradas[:4000]
entradas_test = entradas[4000:]
salidas_train = salidas[:4000]
salidas_test = salidas[4000:]
j=0
while(j<20):
    red = Red(cantidad=[10+j],dim_input=11)
    red.entrenar(entradas_train,salidas_train,epocas = 200)
    red.imprmirError(20+j,200)
    red.test(entradas_test,salidas_test)
    j = j + 1