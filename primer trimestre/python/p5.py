# En una entidad bancaria se brinda a los usuarios diferentes servicios y
# dependiendo de lo que requiera, la máquina dispensadora le genera un
# ticket con un consecutivo y lo direcciona para el área requerida.
# Se sabe que el menú de opciones ofrece 5 posibilidades:
# • Si el usuario va para el servicio de caja, selecciona la opción 1
# • Si va para servicio al cliente selecciona la opción 2.
# • Si va para pago de impuestos elige la opción 3.
# • Si se dirige para crédito hipotecario, presiona la opción 4.
# • Cuando el usuario requiera realizar operaciones con tarjeta de
# crédito debe elegir la opción 5.
# En caso que el usuario elija una opción que no esté en el menú, el sistema
# debe alertarlo y no generar el ticket o invalidarlo.
# Recuerde que el sistema debe decirle al usuario el Id de la sucursal, para
# que servicio va y generarle el ticket correspondiente, también le imprime la
# cedula, el nombre del usuario y la fecha actual.
# Recuerde que cuando el usuario llega a la máquina, esta le pregunta si
# desea continuar o no con la operación. Si la respuesta es sí, procede con
# todo el proceso, en caso que no, el sistema cancela la transacción.

import datetime

id_surcursal = 2341

fecha=datetime.datetime.now()
nombre=input("ingrese su nombre : ")
cedula=int(input("ingrese su cedula : "))
p=input("deseas ingresear al sistema (1 si/2 no): ")
while p=='1':    

    print(f"""Estas en la surcusarl N°: {id_surcursal}
            Menu de opciones:
            1. Servicio de caja
            2. Servicio al cliente
            3. Pago de impuestos
            4. Credito hipotecario
            5. Operaciones con tarjeta de credito""")
    opcion=int(input("Seleccione una opcion del menu (1-5): "))
    match opcion:
        case 1:            
            print(f"""
                  ============================================= 
                    Sucursal ID: {id_surcursal}
                    Nombre: {nombre}
                    Cedula: {cedula}
                    Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}
                    Servicio Realizado: Servicio de caja
                  ============================================= 
                  """)
        case 2:
            print(f"""
                  ============================================= 
                    Sucursal ID: {id_surcursal}
                    Nombre: {nombre}
                    Cedula: {cedula}
                    Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}
                    Servicio Realizado: Servicio al cliente
                  ============================================= 
                  """)
        case 3:
            print(f"""
                  ============================================= 
                    Sucursal ID: {id_surcursal}
                    Nombre: {nombre}
                    Cedula: {cedula}
                    Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}
                    Servicio Realizado: Pago de impuestos
                  ============================================= 
                  """)        
        case 4:
            print(f"""
                  ============================================= 
                    Sucursal ID: {id_surcursal}
                    Nombre: {nombre}
                    Cedula: {cedula}
                    Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}
                    Servicio Realizado: Credito hipotecario
                  ============================================= 
                  """)
        case 5:
            print(f"""
                  ============================================= 
                    Sucursal ID: {id_surcursal}
                    Nombre: {nombre}
                    Cedula: {cedula}
                    Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}
                    Servicio Realizado: Operaciones con tarjeta de credito
                  ============================================= 
                  """)
        case _:
            print("Opcion invalida, vuelve a intentar")

    p=input("deseas realizar alguna otra operacion (1 si/2 no): ")
print("¡Feliz dia, Gracias por escogernos el dia de hoy !")       
