from Lavadora import Lavadora
from LavadoraEstandar import LavadoraEstandar
from LavadoraInteligente import LavadoraInteligente
from GenerarPDF import GenerarPDF


class SistemaLavaSmart:

    @staticmethod
    def ejecutar():

        total_dia = 0
        clientes = 0
        reportes = []

        while True:

            print("\n====== Smart Lava ======")

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

            # cálculos
            costo_base, aumento, iva_valor, total, utilidad = lavadora.calcular_costos()
            consumo, costo_energia = lavadora.calcular_energia()

            # guardar reporte
            reporte = {
                "cliente": nombre,
                "kilos": kilos,
                "tipo": tipo,
                "estrato": estrato,
                "costo_base": costo_base,
                "aumento": aumento,
                "iva": iva_valor,
                "total": total,
                "consumo": consumo,
                "costo_energia": costo_energia
            }

            reportes.append(reporte)

            total_dia += total
            clientes += 1

            while True:
                try:
                    repetir = int(input("\n¿Desea registrar otro lavado? (1=SI / 2=NO): "))
                    if repetir in [1, 2]:
                        break
                    print("Debe ingresar 1 o 2.")
                except ValueError:
                    print("Solo números.")

            if repetir == 2:
                break

        print("\n======= RESUMEN DEL DIA =======")
        print(f"Clientes atendidos: {clientes}")
        print(f"Total recaudado: ${total_dia:,.0f}")
        print("================================")

        # generar PDF
        GenerarPDF.generar(reportes, clientes, total_dia)



if __name__ == "__main__":
    SistemaLavaSmart.ejecutar()
