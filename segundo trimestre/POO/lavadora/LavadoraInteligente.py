from Lavadora import Lavadora
import time


class LavadoraInteligente(Lavadora):

    def __init__(self, kilos, tipo_ropa, estrato):
        super().__init__(kilos, tipo_ropa, estrato)
        self._wifi = True
        self._sensores = True

    def detectar_tipoRopa(self):
        print(" Detectando tipo de ropa automaticamente...")

    def conectarWifi(self):
        if self._wifi:
            print(" Enviando reporte por WiFi...")

    def lavar(self):
        self.detectar_tipoRopa()
        print(" Lavado INTELIGENTE optimizado...")
        self._sonido("lavado")
        time.sleep(self._tiempo_lavado)
        self.conectarWifi()