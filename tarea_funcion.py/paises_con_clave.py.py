#en el bloke principal del pragrama definir un diccionario, almacene los
#nombres de paises como clave y como valor la canridad de abitantes
#implementar una funcion para mostrar cada clave y valor

def imprimir(paises):
    for clave in paises:
        print (clave,paises[clave])


#bloke principal

paises={"argentina":40000000,"espana":46000000,"Brasil":190000000,"Uruguay":34000000}
imprimir(paises)
