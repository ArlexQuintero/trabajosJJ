from Carro import Carro
from CarroElectrico import CarroElectrico
from CarroHibrido import CarroHibrido
from CarroDeportivo import CarroDeportivo

print ("======================================================================")
Carro_gasolina = Carro("Mazda","Azul",100)
print(Carro_gasolina.encender)
print(Carro_gasolina.acelerar(60))
print(Carro_gasolina.frenar())
print(Carro_gasolina)

Carro_Electrico =CarroElectrico("tesla","negro",250,50)
print ("======================================================================")
print(Carro_Electrico.encender)
print(Carro_Electrico.acelerar(100))
print(Carro_Electrico.acelerar(200))
print(Carro_Electrico.frenar())
print(Carro_Electrico)

print ("======================================================================")
carro_Hibrido = CarroHibrido("Svj","verde",300,10,100) 
print(carro_Hibrido.encender())
print(carro_Hibrido.acelerar(100))
print(carro_Hibrido.hibrido())
print(carro_Hibrido.acelerar(200))
print(carro_Hibrido.hibrido())
print(carro_Hibrido.frenar())
print(carro_Hibrido)

print ("======================================================================")
mi_deportivo = CarroDeportivo("Fxx Evolucion", "Rojo", 400, 100)
print(mi_deportivo.encender())
print(mi_deportivo.acelerar(100))
print(mi_deportivo.activar_turbo())
print(mi_deportivo.acelerar(150))
print(mi_deportivo.frenar())
print(mi_deportivo)

