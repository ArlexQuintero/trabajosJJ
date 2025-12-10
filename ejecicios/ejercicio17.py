total_positives = 0
total_negatives = 0
for i in range(1, 6):
    num = float(input(f"Digite un numero: "))

    if num > 0:
        total_positives = total_positives + 1
    elif num < 0:
        total_negatives = total_negatives + 1

print(f"La cantidad de numeros positivos es: {total_positives}")
print(f"La cantidad de numeros negativos es: {total_negatives}")
