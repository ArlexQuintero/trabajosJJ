# Desarrollar un programa que permita por medio de la edad de una
# persona, determinar la categoría a la que pertenece con base en la
# siguiente tabla:

edad=int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 5:
    print("Usted pertenece a la categoria de Infante")
elif edad >= 6 and edad <= 10:
    print("Usted pertenece a la categoria de Niños")
elif edad >= 11 and edad <= 15:
    print("Usted pertenece a la categoria de Pre adolescentes")
elif edad >= 16 and edad <= 18:
    print("Usted pertenece a la categoria de Adolescentes")
elif edad >= 19 and edad <= 25:
    print("Usted pertenece a la categoria de Pre adultos")
elif edad >= 26 and edad <= 40:
    print("Usted pertenece a la categoria de Adultos")
elif edad >= 41 and edad <= 55:
    print("Usted pertenece a la categoria de Pre ancianos")
elif edad >56:
    print("Usted pertenece a la categoria de Ancianos")
else:
    print("La edad ingresada no es valida")