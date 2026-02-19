from Carro import Carro

class CarroElectrico(Carro):
    def __init__(self, marca,color,velocidad_max,bateria_max):

        super().__init__(marca,color,velocidad_max)

        self.bateria = bateria_max

        self.bateria_max = bateria_max
    def Recarga (self):

        self.bateria = self.bateria_max

        return "bateria esta al 100%"
    
    def acelerar(self, aumentar):

        if not self.encendido:

            return "el carro esta apagado. primero enciendelo"
        
        if self.bateria <= 0:

            return "bateria agotada, no se puede acelelar"
        
        mensaje_velocida = super().acelerar(aumentar)

        self.bateria -= 5

        return f"{mensaje_velocida}| bateria {self.bateria} %"
    def __str__(self):
        return f"carro electrico {self.marca} de color {self.color}"
