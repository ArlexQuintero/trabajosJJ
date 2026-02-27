class Vehiculos:
    def __init__(self,marca, modelo, precio_alquiler):
        self.marca=marca
        self.modelo=modelo
        self.precio_alquiler=precio_alquiler
        self.disposible=False
        
    def mostrar_informacion(self):
        return f"Vehiculo de Marca {self.marca} de modelo {self.modelo}, tiene un precio de alquiler de {self.precio_alquiler} y se encuentra en estado {self.disposible} para la disposicion"
    def alquilar(self):
        if not self.disposible:
            return f"El vehiculo de marca {self.marca} y modelo {self.modelo} no esta disponible"
        self.disposible=False
        return "Vehiculo alquilado con exito"
    def devolver(self):
        if not self.disposible:
            self.disposible=True
            return f"El vehiculo {self.marca} ha sido devuelto de manera correcta"
        self.devolver=True
        return f"Devolucion del vehiculo {self.marca} del modelo {self.modelo} ha sido devuelto correctamente "
    def __str__(self):
        pass