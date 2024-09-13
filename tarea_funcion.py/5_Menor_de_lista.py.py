#crear una lista de 5 pociciones pidiendo los valores por teclado
lista = []
for x in range (5):
    valor=int(input("ingrese un numero entero "))
    lista.append(valor)

menor = lista[0]
posicion = 0

for x in range (1,5):
    if lista[x]<menor:
        menor= lista[x]
        posicion = x

print (" lista completa ")
print (lista)
print (" el numero menor es: ")
print (menor)
print (" se encuentra en la posicion ")
print (posicion)
    
