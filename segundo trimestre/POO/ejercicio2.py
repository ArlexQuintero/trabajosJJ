# 2.Desarrollar una función en Python que recibe los gastos de pasajes de los 6 días de la semana 
# y calcular el total gastado. 
# Haz una mejora al ejercicio de acuerdo a lo siguiente:
# Usando un ciclo while True y try: except valueError: debes controlar 
# que al ingresar un valor en el dia que no sea numérico, el programa no arroje error. 
# Debes mostrar emojis para cada impresión o mensaje al usuario.

def calcular_gastos(gastos):
    total_gastos = sum(gastos)
    return total_gastos
gastos = []
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
for dia in dias_semana:
    while True:
        try:
            gasto = float(input(f"Ingresa el gasto de pasajes para {dia}: "))
            gastos.append(gasto)
            break
        except ValueError:
            print("¡Error! Por favor, ingresa un número válido. 🚫")
total = calcular_gastos(gastos)
print(f"El total gastado en pasajes durante la semana es: {total} 💸")