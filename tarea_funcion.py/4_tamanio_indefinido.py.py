#crear una lista y pedir los valoes por teclado
lista =[]
valor = int(input(" ingrese un numero entero o 0 para salir "))
while valor != 0:
    lista.append(valor)
    valor = int(input(" ingrese un numero entero o 0 para salir "))

print ("el tamanio de la lista es: ")
print (len(lista))
                
