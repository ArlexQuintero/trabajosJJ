num_positives = 0
while True:
    num = int(input("Digite un numero (0 para salir): "))

    if num == 0:
        break

    if (num > 0):
        num_positives = num_positives + 1

print("La cantidad de numeros positivos es: ", num_positives)
