from Vehiculos import Vehiculos
class Taxi(Vehiculos):
    def __init__(self,marca, modelo, precio_alquiler,precio_km,km):
        super().__init__(marca,modelo,precio_alquiler)
        self.precio_km=precio_km
        self.km=km
        self.total_km=0
    def Calcular_tarifa(self):
        self.total_km=self.precio_km*self.km
        return self.total_km
    def mostrar_informacion(self):
        return f"Vehiculo de Marca {self.marca} de modelo {self.modelo} Tiene un precio de alquiler de {self.precio_alquiler} Se encuentra en estado {self.disposible} para la disposicion"
    def devolver(self):
        if not self.disposible:
            self.disposible=True
            self.km=0
            return f"El vehiculo {self.marca} ha sido devuelto de manera correcta Los Km se an reiniciado a {self.km}"
        return f"Devolucion del vehiculo {self.marca} del modelo {self.modelo} ha sido devuelto correctamente "
    def __str__(self):
        pass