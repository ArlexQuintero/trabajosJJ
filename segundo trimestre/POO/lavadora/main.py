from Lavadora import Lavadora
from LavadoraEstandar import LavadoraEstandar
from LavadoraInteligente import LavadoraInteligente


class SistemaLavaSmart:

    @staticmethod
    def ejecutar():

        print("====== Smart Lava ======")

        nombre = Lavadora.pedir_nombre()
        kilos = Lavadora.pedir_kilos()
        tipo = Lavadora.pedir_prenda()
        estrato = Lavadora.pedir_estrato()
        opcion = Lavadora.pedir_tipo_lavadora()

        if opcion == 1:
            lavadora = LavadoraEstandar(kilos, tipo, estrato)
        else:
            lavadora = LavadoraInteligente(kilos, tipo, estrato)

        lavadora.validar_datos()

        lavadora.encender()
        lavadora.llenar()
        lavadora.lavar()
        lavadora.enjuagar()

        if Lavadora.pedir_secado() == 1:
            lavadora.secar()

        lavadora.ciclo_terminado(nombre)


if __name__ == "__main__":
    SistemaLavaSmart.ejecutar()