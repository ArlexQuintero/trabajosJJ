from Carro import Carro
from CarroElectrico import CarroElectrico

Carro_gasolina = Carro("Mazda","rojo",100)
print(Carro_gasolina.encender)
print(Carro_gasolina.acelerar(60))
print(Carro_gasolina.frenar())
print(Carro_gasolina)

Carro_Electrico =CarroElectrico("tesla","negro",250,100)

print(Carro_Electrico.encender)
print(Carro_Electrico.acelerar(100))
print(Carro_Electrico.acelerar(200))
print(Carro_Electrico.frenar())
print(Carro_Electrico)