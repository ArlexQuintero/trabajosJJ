from abc import ABC, abstractmethod
from datetime import datetime
import time
import winsound


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

    # definir los sonidos

    def _sonido(self, tipo):
        if tipo == "encendido":
            winsound.Beep(1000, 400)
        elif tipo == "llenado":
            winsound.Beep(800, 400)
        elif tipo == "lavado":
            winsound.Beep(600, 400)
        elif tipo == "enjuague":
            winsound.Beep(500, 400)
        elif tipo == "secado":
            winsound.Beep(400, 400)
        elif tipo == "finalizado":
            winsound.Beep(1200, 700)

    # metodos publicos

    def encender(self):
        self.__estado = "encendida"
        print(" Lavadora encendida")
        self._sonido("encendido")

    def ciclo_terminado(self, nombre_cliente):
        self._sonido("finalizado")
        print("\n Ciclo finalizado")
        self._mostrar_reporte_cliente(nombre_cliente)

    # metodos protegidos

    def _validar_kilos(self):
        if self._kilos < 5 or self._kilos > 40:
            raise ValueError("Los kilos deben estar entre 5 y 40.")

    def _llenar(self):
        print(" Llenando agua...")
        self._sonido("llenado")
        time.sleep(2)

    def enjuagar(self):
        print(" Enjuagando...")
        self._sonido("enjuague")
        time.sleep(2)

    def secar(self):
        print(" Secando...")
        self._sonido("secado")
        time.sleep(2)

    # metodos privados

    def __calcular_costos(self):
        costo_base = self._kilos * self._precio_kilo

        aumento = 0
        if self._tipo_ropa.lower() in ["interior", "pijamas", "vestidos"]:
            aumento = costo_base * self._aumento_especial

        subtotal = costo_base + aumento
        iva_valor = subtotal * self._iva
        total = subtotal + iva_valor
        utilidad = total * 0.30

        return costo_base, aumento, iva_valor, total, utilidad

    def __calcular_consumo_energia(self):
        tiempo_horas = self._tiempo_lavado / 60
        consumo = self._potencia_kw * tiempo_horas

        tarifas = {2: 867.8, 3: 737.6, 4: 867.8, 5: 1041}
        valor_kwh = tarifas.get(self._estrato, 867.8)
        costo_energia = consumo * valor_kwh

        return consumo, costo_energia

    def _mostrar_reporte_cliente(self, nombre_cliente):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        costo_base, aumento, iva_valor, total, utilidad = self.__calcular_costos()
        consumo, costo_energia = self.__calcular_consumo_energia()

        print("\n=========== COMPROBANTE ===========")
        print(f"Cliente: {nombre_cliente}")
        print(f"Fecha: {fecha}")
        print(f"Kilos: {self._kilos}")
        print(f"Tipo prenda: {self._tipo_ropa}")
        print(f"Costo base: ${costo_base:,.0f}")
        print(f"Aumento especial: ${aumento:,.0f}")
        print(f"IVA: ${iva_valor:,.0f}")
        print(f"Total a pagar: ${total:,.0f}")
        print(f"Consumo energía (kWh): {consumo:.2f}")
        print(f"Costo energía: ${costo_energia:,.0f}")
        print("Gracias por usar Lava Smart ")
        print("===================================")

    # ---------------- POLIMORFISMO ----------------

    @abstractmethod
    def lavar(self):
        pass