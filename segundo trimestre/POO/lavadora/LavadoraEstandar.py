
from Lavadora import Lavadora
import time


class LavadoraEstandar(Lavadora):

    def lavar(self):
        print(" Lavando en modo ESTANDAR...")
        self._sonido("lavado")
        time.sleep(self._tiempo_lavado)