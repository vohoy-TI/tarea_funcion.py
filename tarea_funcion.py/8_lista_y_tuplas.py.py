#definir una tupla con tres valores enteros convertirla a lista modificarla
#y convertirla en tupla
fechatupla1=(25, 12, 2016)
print ("imprimimos la primera tupla ")
print (fechatupla1)

#convertimos la tupla en lista
fechalista1=list(fechatupla1)
print (" imprimimos la lista copiada de la tupla ")
print (fechalista1)
#modificamos la lista
fechalista1[0]=31
print (" imprimimos la lista modificada ")
print (fechalista1)
#convertimos la lista en tupla
fechatupla2=tuple(fechalista1)
print (" imprimimos la nueva tupla ")
print (fechatupla2)
