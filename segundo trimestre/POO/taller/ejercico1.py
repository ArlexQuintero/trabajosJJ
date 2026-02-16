# 1.Desarrollar una función que reciba tres números ingresados por el cliente y
#  devuelva la suma de ellos.   
# Mostrar la versión mejorada con while y try: except.
def suma (num1, num2, num3):
    return num1 + num2 + num3

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: ")) 
num3 = float(input("Ingrese el tercer número: "))
print(f"La suma de los números es: {suma(num1, num2, num3)}")