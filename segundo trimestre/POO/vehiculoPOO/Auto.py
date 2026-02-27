from Vehiculos import Vehiculos
class Auto(Vehiculos):
    def __init__(self,marca, modelo, precio_alquiler,Num_puertas):
        super().__init__(marca, modelo, precio_alquiler)
        self.Num_puertas=Num_puertas
    def mostrar_informacion(self):
        return f"Vehiculo de Marca {self.marca} de modelo {self.modelo}, tiene un precio de alquiler de {self.precio_alquiler} y se encuentra en estado {self.disposible} para la disposicion, con numero de puertas {self.Num_puertas}" 
    def __str__(self):
        pass