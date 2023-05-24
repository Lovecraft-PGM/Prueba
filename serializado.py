import pickle

#Creación de archivo serializado
# lista1 = input('ingrese el nombre del archivo:')

# palabra = input('ingrese la palabra que va a guardar en el archivo:')

# lista = [ palabra ]

# miarchivo = open(lista1+'.txt','wb',)
# pickle.dump(lista, miarchivo)

# miarchivo.close() 



archivo = input('Por favor ingrese el nombre del archivo que quiere leer:')

miarchivo = open (archivos+'.txt','rb')
lista  = pickle.load(miarchivo)
miarchivo.close()

print(lista)