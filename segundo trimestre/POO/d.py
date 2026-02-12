# d.Crea un programa en Python que calcule el valor del IVA (Impuesto al Valor Agregado) de una compra.
# El programa debe solicitar al usuario que ingrese el subtotal de la compra (valor antes de impuestos) 
# y luego debe calcular el IVA aplicando una tasa del 19%.
# Finalmente, el programa debe retornar el valor del IVA correspondiente

def iva(valor):
    preciosub= valor * 0.19
    total= valor + preciosub
    return total, preciosub

valor= float(input("Ingrese el valor del producto: "))
print(f"""
    El subtotal de tu compra es de : {valor}
    El valor del iva es del: {iva(valor)[1]}
    El total de lo comprado con un iva del 19% es: {iva(valor)[0]}
""")
