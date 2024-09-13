# Lista para almacenar los empleados y sus sueldos
empleados = []

# Función 1: Carga de empleados
def cargar_empleados():
    for i in range(5):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        sueldo = float(input(f"Ingrese el sueldo de {nombre}: "))
        empleados.append((nombre, sueldo))

# Función 2: Imprimir empleados y sus sueldos
def imprimir_empleados():
    print("\nLista de empleados y sus sueldos:")
    for nombre, sueldo in empleados:
        print(f"Empleado: {nombre}, Sueldo: {sueldo}")

# Función 3: Nombre del empleado con sueldo mayor
def empleado_sueldo_mayor():
    empleado_max = max(empleados, key=lambda x: x[1])  # Usamos la función max con el sueldo (índice 1 de la tupla)
    print(f"\nEl empleado con el sueldo mayor es {empleado_max[0]} con un sueldo de {empleado_max[1]}")

# Función 4: Cantidad de empleados con sueldo menor a 1000
def empleados_sueldo_menor_1000():
    cantidad = sum(1 for _, sueldo in empleados if sueldo < 1000)
    print(f"\nLa cantidad de empleados con sueldo menor a 1000 es: {cantidad}")

# Programa principal
cargar_empleados()
imprimir_empleados()
empleado_sueldo_mayor()
empleados_sueldo_menor_1000()
