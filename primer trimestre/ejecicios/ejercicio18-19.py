total = 0
for i in range(1, 6):
    hours = int(input(f"Digite las horas trabajadas en el dia {i}: "))
    value_hour = float(input(f"Digite el valor de la hora: "))

    salary = hours * value_hour

    if hours > 40:
        extra_hours = (hours - 40) * value_hour * 0.5
        salary = salary + extra_hours

    print(f"El salario del dia {i} es: {salary}")
    total = total + salary

print(f"El total de la semana es: {total}")
