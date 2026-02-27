from Vehiculos import Vehiculos
from Taxi import Taxi
from Auto import Auto
from Moto import Moto

print ("=======================================================")
vehiculo=Vehiculos("audi","tt",200000)
print(vehiculo.mostrar_informacion())
print(vehiculo.alquilar())
print("................................................")
print(vehiculo.devolver())
print(vehiculo.mostrar_informacion())
print ("=======================================================")

print ("=======================================================")
auto=Auto("ferrari","purosangre",1000000,2)
print(auto.mostrar_informacion())
print(auto.alquilar())
print("................................................")
print(auto.devolver())
print(auto.mostrar_informacion())
print ("=======================================================")

print ("=======================================================")
moto=Moto("ducaty","Moster",50000,990)
print(moto.mostrar_informacion())
print(moto.alquilar())
print("................................................")
print(moto.devolver())
print(moto.mostrar_informacion())
print ("=======================================================")

print ("=======================================================")
taxi=Taxi("Renold","sendero",100000,200,50)
print(taxi.mostrar_informacion())
print(taxi.alquilar())
print("tiene un valor a pagar de: ",taxi.Calcular_tarifa())
print("................................................")
print(taxi.devolver())
print(taxi.mostrar_informacion())