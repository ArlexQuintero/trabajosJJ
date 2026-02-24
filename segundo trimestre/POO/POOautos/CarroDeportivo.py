# CarroDeportivo
# Características:
# Tiene modo turbo
# Acelera más rápido que un carro normal
# Consume más combustible al acelerar fuerte
# También sobrescribe acelerar().
from Carro import Carro

class CarroDeportivo(Carro):
    def __init__(self, marca, color, velocidad_max, tanque_max):
        super().__init__(marca, color, velocidad_max)
        self.tanque = tanque_max
        self.tanque_max = tanque_max
        self.turbo = False  

    def activar_turbo(self):
        self.turbo = True
        return f"Turbo activado en el {self.marca} "

    def desactivar_turbo(self):
        self.turbo = False
        return f"Turbo desactivado en el {self.marca} "

    def acelerar(self, aumento):
        if not self.encendido:
            return "El carro está apagado, primero enciéndelo"
        
        incremento_vel = aumento * 1.5 if self.turbo else aumento

        if self.velocidad + incremento_vel <= self.velocidad_max:
            self.velocidad += incremento_vel
        else:
            self.velocidad = self.velocidad_max


        if self.turbo:
            gasto = incremento_vel * 0.2 
        else:
            gasto = incremento_vel * 0.1

        if self.tanque - gasto >= 0:
            self.tanque -= gasto
        else:
            self.tanque = 0
            return "Sin combustible, no se puede acelerar"

        modo = "Turbo" if self.turbo else "Normal"
        return f"Velocidad: {self.velocidad} Km/h | Modo: {modo} | Tanque: {self.tanque:.1f} ml"

    def __str__(self):
        return f"Carro Deportivo {self.marca} de color {self.color} | Tanque: {self.tanque} ml"