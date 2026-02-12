# Calcular ventas con varios parámetros y retorno
# e.Desarrolle un programa en Python que contenga una función llamada calcular_total.
# La función debe recibir dos parámetros:
# subtotal: el valor base de una venta.
# iva: el valor del impuesto al valor agregado (IVA).
# La función debe sumar el subtotal con el IVA y retornar el total a pagar.
# Luego, el programa debe mostrar en pantalla el total calculado utilizando una cadena formateada .

def iva(valor):
    preciosub= valor * 0.19
    total= valor + preciosub
    return total, preciosub

valor= float(input("Ingrese el valor del producto: "))
print(f"""
    ==============================================================================
    El subtotal de tu compra es de : {valor}
    El valor del iva es del: {iva(valor)[1]}
    El total de lo comprado con un iva del 19% es: {iva(valor)[0]}
""")