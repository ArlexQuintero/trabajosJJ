
purchase_value = float(input("Digite el valor de la compra: "))

if purchase_value > 100000:
    discount = purchase_value * 0.1
else:
    discount = 0


final_value = purchase_value - discount

print(f"El valor final a pagar es: {final_value}")
