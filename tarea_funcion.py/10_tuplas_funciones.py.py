#desarrollar una funcion ue solicite la carga del dia, mes y anio y
#almacenar dichos datos en una tupla ue luego debe retornar
#la segunda funciona implementar debe recibir una tupla
#con la fecha y mostrarla por pantalla

def cargar_fecha():
    dia = int(input("Ingrese el numero de día: "))
    mes = int(input("Ingrese el numero de mes: "))
    año = int(input("Ingrese el año: "))
    return (dia, mes, año)

def mostrar_fecha(fecha):
    dia, mes, año = fecha
    print(f"La fecha ingresada es: {dia}/{mes}/{año}")

fecha = cargar_fecha()
mostrar_fecha(fecha)
