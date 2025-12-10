sum_nums = 0


while True:
    num = int(input("Digite un numero (0 para salir): "))
    if num == 0:
        break

    sum_nums = sum_nums + num

print(f"La suma de los numeros es: {sum_nums}")
