mayor_persons = 0
minors_persons = 0

while True:
    age = int(input("Digite la edad: (0 para salir) "))

    if age == 0:
        break

    if age >= 18:
        print(f"Puedes entrar al evento")
        mayor_persons = mayor_persons + 1
    else:
        print(f"No puedes entrar al evento")
        minors_persons = minors_persons + 1
