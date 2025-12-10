days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sábado"]
total = 0
total_passages = 0
total_refreshments = 0

for i in range(len(days)):
    passage = float(input(f"Digite lo gastado en pasajes el dia {days[i]}: "))
    refreshment = float(
        input(f"Digite lo gastado en refrigerio el dia {days[i]}: "))

    total = total + passage + refreshment
    total_passages = total_passages + passage
    total_refreshments = total_refreshments + refreshment


print(f"El total gastado en pasajes es: {total_passages}")
print(f"El total gastado en refrigerios es: {total_refreshments}")
print(f"El total gastado en la semana es de: {total}")
