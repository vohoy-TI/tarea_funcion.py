#programa permite cargar 5 nombres de personas con sus edades
nombres =[]
edades = []

for x in range (5):
    nombre = input ("ingrese el nombre ")
    nombres.append(nombre)

    edad= int(input(" ingrese la edad de dicha persona "))
    edades.append(edad)

print (" nombres de las personas mayores de edad ")
for x in range (5):
    if edades [x] >= 18:
        print (nombres [x])
