def iva(valor):
    preciosub= valor * 0.19
    total= valor + preciosub
    return total

valor= float(input("Ingrese el valor del producto: "))
print(f"el total de lo comprado con un iva del 19% es: {iva(valor)}")

