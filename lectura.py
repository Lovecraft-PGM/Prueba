archivo = input('Por favor ingrese el nombre del archivo que quiere leer:')

miarchivo = open (archivo+'.txt','rb')
lista  = pickle.load(miarchivo)
miarchivo.close()

print(lista)