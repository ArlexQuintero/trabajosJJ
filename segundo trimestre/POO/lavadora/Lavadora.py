#importaciones necesarias
from abc import ABC, abstractmethod
from datetime import datetime
import time
import winsound
import os

#clase padre
class Lavadora(ABC):

    def __init__(self, kilos, tipo_ropa, estrato):
        self._kilos = kilos
        self._tipo_ropa = tipo_ropa
        self.__estado = "apagada"
        self._tiempo_lavado = 5
        self._precio_kilo = 10000
        self._aumento_especial = 0.05
        self._iva = 0.19
        self._potencia_kw = 1.5
        self._estrato = estrato

    #definir los sonidos
    def _sonido(self, tipo):
        
        base_path = os.path.join(os.path.dirname(__file__), "sonidos")

        sonidos = {
            "encendido": "encendido.wav",
            "llenado": "llenado.wav",
            "lavado": "lavado.wav",
            "enjuague": "enjuague.wav",
            "secado": "secado.wav",
            "finalizado": "finalizado.wav"
        }

        if tipo in sonidos:
            ruta = os.path.join(base_path, sonidos[tipo])
            winsound.PlaySound(ruta, winsound.SND_FILENAME)

    #validaciones de todos los campos para solo datos validos
    @staticmethod
    def pedir_nombre():
        while True:
            nombre = input("Nombre del cliente: ").strip()
            if nombre.replace(" ", "").isalpha():
                return nombre
            print(" El nombre solo debe contener letras.")

    @staticmethod
    def pedir_kilos():
        while True:
            try:
                kilos = float(input("Ingrese kilos (5-40): "))
                if 5 <= kilos <= 40:
                    return kilos
                print(" Los kilos deben estar entre 5 y 40.")
            except ValueError:
                print(" Solo se permiten números.")

    @staticmethod
    def pedir_prenda():
        prendas = {
            1: "algodon",
            2: "lana",
            3: "sintetico",
            4: "interior",
            5: "pijamas",
            6: "vestidos"
        }

        print("\nSeleccione tipo de prenda:")
        for numero, prenda in prendas.items():
            print(f"{numero}. {prenda}")

        while True:
            try:
                opcion = int(input("Seleccione opción: "))
                if opcion in prendas:
                    return prendas[opcion]
                print(" Opción inválida.")
            except ValueError:
                print(" Solo se permiten números.")

    @staticmethod
    def pedir_estrato():
        while True:
            try:
                estrato = int(input("Estrato (2-5): "))
                if estrato in [2, 3, 4, 5]:
                    return estrato
                print(" El estrato debe estar entre 2 y 5.")
            except ValueError:
                print(" Solo se permiten números.")

    @staticmethod
    def pedir_tipo_lavadora():
        print("\nTipo de lavadora:")
        print("1. Estandar")
        print("2. Inteligente")

        while True:
            try:
                opcion = int(input("Seleccione opción: "))
                if opcion in [1, 2]:
                    return opcion
                print(" Opción inválida.")
            except ValueError:
                print(" Solo se permiten números.")

    @staticmethod
    def pedir_secado():
        while True:
            try:
                opcion = int(input("¿Desea secar? (1=Si / 2=No): "))
                if opcion in [1, 2]:
                    return opcion
                print(" Debe ingresar 1 o 2.")
            except ValueError:
                print(" Solo se permiten números.")

    #metodos para cada paso y sonidos 
    def encender(self):
        self.__estado = "encendida"
        print(" Lavadora encendida")
        self._sonido("encendido")

    def ciclo_terminado(self, nombre_cliente):
        self._sonido("finalizado")
        print("\n Ciclo finalizado...")
        self.Mostrar_Reporte(nombre_cliente)

    def validar_datos(self):
        self.validar_kilos()
        self.validar_tipo_ropa()
        self.validar_estrato()


    def validar_kilos(self):
        if not isinstance(self._kilos, (int, float)):
            raise ValueError("Los kilos deben ser un número.")
        if self._kilos < 5 or self._kilos > 40:
            raise ValueError("Los kilos deben estar entre 5 y 40.")

    def validar_tipo_ropa(self):
        tipos_validos = [
            "algodon",
            "lana",
            "sintetico",
            "interior",
            "pijamas",
            "vestidos"
        ]
        if self._tipo_ropa.lower() not in tipos_validos:
            raise ValueError("Tipo de ropa inválido.")

    def validar_estrato(self):
        if self._estrato not in [2, 3, 4, 5]:
            raise ValueError("El estrato debe estar entre 2 y 5.")

    def llenar(self):
        print(" Llenando agua...")
        self._sonido("llenado")
        time.sleep(1)

    def enjuagar(self):
        print(" Enjuagando...")
        self._sonido("enjuague")
        time.sleep(1)

    def secar(self):
        print(" Secando...")
        self._sonido("secado")
        time.sleep(1)
    #calcular los precios 
    def calcular_costos(self):
        costo_base = self._kilos * self._precio_kilo

        aumento = 0
        if self._tipo_ropa.lower() in ["interior", "pijamas", "vestidos"]:
            aumento = costo_base * self._aumento_especial

        subtotal = costo_base + aumento
        iva_valor = subtotal * self._iva
        total = subtotal + iva_valor
        utilidad = total * 0.30

        return costo_base, aumento, iva_valor, total, utilidad

    def calcular_energia(self):
        tiempo_horas = self._tiempo_lavado / 60
        consumo = self._potencia_kw * tiempo_horas

        tarifas = {2: 867.8, 3: 737.6, 4: 867.8, 5: 1041}
        valor_kwh = tarifas.get(self._estrato, 867.8)
        costo_energia = consumo * valor_kwh

        return consumo, costo_energia
    
    #mostrar el reporte final
    def Mostrar_Reporte(self, nombre_cliente):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        costo_base, aumento, iva_valor, total, utilidad = self.calcular_costos()
        consumo, costo_energia = self.calcular_energia()

        print("\n=========== COMPROBANTE ===========")
        print(f"Cliente: {nombre_cliente}")
        print(f"Fecha: {fecha}")
        print(f"Kilos: {self._kilos}")
        print(f"Tipo prenda: {self._tipo_ropa}")
        print(f"Total a pagar: ${total:,.0f}")
        print("Gracias por usar Smart Lava")
        print("===================================")

    @abstractmethod
    def lavar(self):
        pass