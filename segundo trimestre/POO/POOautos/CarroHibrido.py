 #CarroHibrido
# Características:
# Tiene tanque de gasolina
# Tiene batería
# Puede usar ambos sistemas
# Si se acaba la batería → usa gasolina
# Si se acaba gasolina → usa batería
# Debe sobrescribir acelerar().
from CarroElectrico import CarroElectrico
from Carro import Carro  

class CarroHibrido(CarroElectrico):
    def __init__(self, marca, color, velocidad_max, bateria_max, tanque_max):
        
        super().__init__(marca, color, velocidad_max, bateria_max)

        self.tanque = tanque_max
        self.tanque_max = tanque_max
    
    def hibrido(self):
        if self.bateria > 0:
            self.bateria -= 5
            return "En modo eléctrico"
        elif self.tanque > 0:
            self.tanque -= 5
            return "En modo combustión"
        else:
            return "Sin energía disponible"
    

    def acelerar(self, aumentar):
        if not self.encendido:
            return "El carro está apagado. Primero enciéndelo"


        if self.bateria > 0:
            mensaje_velocidad = super().acelerar(aumentar)
            return f"{mensaje_velocidad} | Modo eléctrico | batería {self.bateria}% | tanque {self.tanque} ml"

      
        elif self.tanque > 0:
            mensaje_velocidad = Carro.acelerar(self, aumentar)
            self.tanque -= 5
            return f"{mensaje_velocidad} | Modo combustión | batería {self.bateria}% | tanque {self.tanque} ml"

        
        else:
            return "Sin batería y sin combustible. No se puede acelerar."
    

    def __str__(self):
        return f"Carro Híbrido {self.marca} de color {self.color}"