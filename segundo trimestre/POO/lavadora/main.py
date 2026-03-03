
from LavadoraEstandar import LavadoraEstandar
from LavadoraInteligente import LavadoraInteligente


class SistemaLavaSmart:

    @staticmethod
    def ejecutar():

        try:
            print("====== Smart Lava ======")

            nombre = input("Nombre del cliente: ")
            kilos = float(input("Ingrese kilos (5-40): "))
            tipo = input("Tipo de prenda: ")
            estrato = int(input("Estrato (2-5): "))
            opcion = input("Tipo lavadora (1=Estandar, 2=Inteligente): ")

            if opcion == "1":
                lavadora = LavadoraEstandar(kilos, tipo, estrato)
            elif opcion == "2":
                lavadora = LavadoraInteligente(kilos, tipo, estrato)
            else:
                raise ValueError("Opcion invalida.")

            lavadora.encender()
            lavadora.validar_kilos()
            lavadora.llenar()
            lavadora.lavar()
            lavadora.enjuagar()

            secar = input("¿Desea secar? (s/n): ")
            if secar.lower() == "s":
                lavadora.secar()

            lavadora.ciclo_terminado(nombre)

        except ValueError as e:
            print(" Error:", e)
        except Exception as e:
            print(" Error inesperado:", e)


if __name__ == "__main__":
    SistemaLavaSmart.ejecutar()