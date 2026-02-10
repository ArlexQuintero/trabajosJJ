
for i in range(1, 6):
    values = []

    for j in range(1, 4):
        value = int(input(f"Digite la nota {j} del alumno {i}: "))
        values.append(value)

    avarage = sum(values) / len(values)

    if avarage >= 3:
        print(f"El alumno {i} tiene un promedio de {avarage} y esta aprobado")
    else:
        print(f"El alumno {i} tiene un promedio de {avarage} y esta reprobado")
