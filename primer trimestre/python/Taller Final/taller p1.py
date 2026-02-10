# Arreglos (Listas)
#  Planteamiento
# Un instructor requiere guardar las calificaciones de 5 aprendices  en una lista, para ello debe:
# 1.Crear una lista con 5 calificaciones para 5 aprendices que no aprobaron.
# 2.Muestre de cada uno  todas las calificaciones.
# 3.Calcule  para cada aprendiz el promedio de las calificaciones.
# 4.Muestre cuántas calificaciones son mayores o iguales a 3.5.

# Resultado esperado:

# Mostrar la lista de calificaciones.
# Mostrar el promedio de todos
# Mostrar cuántos estudiantes aprobaron (≥ 3.5).

calificaciones = []
for i in range(3):
    nombre=input(f"Ingrese el nombre del aprendiz {i+1}: ")
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j+1} para {nombre}: "))
        calificaciones.append((nombre, calificacion))
    promedio=sum([calificacion for aprendiz, calificacion in calificaciones if aprendiz==nombre])/len([calificacion for aprendiz, calificacion in calificaciones if aprendiz==nombre])  
    print(f"El promedio de calificaciones para {nombre} es: {promedio:.2f}")
    if promedio >= 3.5:
        print(f"{nombre} ha aprobado.")
    else:
        print(f"{nombre} no ha aprobado.")
