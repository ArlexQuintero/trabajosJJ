# Diccionarios
# Planteamiento:
# Un programa debe almacenar información básica de aprendices usando un diccionario. Por tanto…

# 1.Cree un diccionario con el nombre del estudiante como clave y su edad como valor.
# 2.Muestre todos los estudiantes y sus edades.
# 3.Agregue un nuevo estudiante.
# 4.Busque la edad de un estudiante específico.
# }

#  Resultado esperado
# Mostrar todos los estudiantes con sus edades.
# Agregar un estudiante nuevo.
# Consultar la edad de un estudiante ingresado.

estudiantes=[{"nombre":"pepe","edad":30},{"nombre":"Jairo","edad":20},{"nombre":"Carlos","edad":15},{"nombre":"Camilo","edad":20}]
for estudiante in estudiantes:
    print(f"El estudiante {estudiante['nombre']} tiene {estudiante['edad']} años.")

nue_est=input("Ingrese el nombre del nuevo estudiante: ")
nue_edad=int(input(f"Ingrese la edad de {nue_est}: "))
estudiantes.append({"nombre":nue_est,"edad":nue_edad})
print("Estudiantes actualizados:")
for estudiante in estudiantes:
    print(f"El estudiante {estudiante['nombre']} tiene {estudiante['edad']} años.")
bus=input("Ingrese el nombre del estudiante a buscar: ")
for estudiante in estudiantes:
    if estudiante["nombre"]==bus:
        print(f"{estudiante['nombre']} tiene {estudiante['edad']} años.")