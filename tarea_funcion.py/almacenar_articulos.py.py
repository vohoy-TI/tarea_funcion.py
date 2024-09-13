#crear un diccionario ue permita almacenar articulos
#utilizar como clave el nombre del producto y como valor el precio del mismo
#desarrollar las funciones de
#imprimir en forma completa el diccionario
#imprimir solo los articulos con precios superior a 100

def cargar():
    productos={}
    for x in range (5):
        nombre=input(" ingrese el nombre del producto ")
        precio=int(input(" ingrese el precio del mismo "))
        productos[nombre]=precio
        return productos

def imprimir(productos):
    print("listado de todos los articulos ")
    for nombre in productos:
        print (nombre, productos[nombre])

def imprimir_mayor100(productos):
    print("listado de productos mayores a 100 ")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)

#bloke principal

productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)
