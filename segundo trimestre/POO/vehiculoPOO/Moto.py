from Vehiculos import Vehiculos
class Moto(Vehiculos):
    def __init__(self,marca, modelo, precio_alquiler,cilidrada):
        super().__init__(marca,modelo,precio_alquiler)
        self.cilidrada=cilidrada
    def mostrar_informacion(self):
        return f"Vehiculo de Marca {self.marca} de modelo {self.modelo}, tiene un precio de alquiler de {self.precio_alquiler} y se encuentra en estado {self.disposible} para la disposicion, con una cilindrada de {self.cilidrada}" 
    def __str__(self):
        pass     