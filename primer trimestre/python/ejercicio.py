import math 
smmlv=1423500
axt=200000
demanda=3740000

horas=float(input("ingrese cuantas horas trabajo esta semana: "))
valor=float(input("ingrese el valor de la hora: "))
salario_S=horas*valor
p=float(input("se realizaron algunas horas extras (1=si, 2=no)"))
if p==1:
    horas_ex=float(input("cuantas horas extras trabajo: "))
    valor_ex=horas_ex*(valor*1.25)
else:
    valor_ex=0
salario_M=(salario_S+valor_ex)*4
emi=salario_M*0.03
fune=salario_M*0.02

f=float(input("de cuanto porsentaje para el fondo de empleados ? "))
fondo=salario_M*(f/100)
total_des=emi+fune+fondo
if salario_M>demanda:
    retencion=salario_M*0.30
else:
    retencion=0
salario_neto=salario_M-total_des-retencion
if salario_M< smmlv*2:
    auxilio=axt
else:
    auxilio=0
total_s=salario_neto+auxilio
print(f"""
      =============================================
      Su salario mensual es de ${salario_M}
      =============================================
      DEDUCCIONES
      =============================================
      Emi:${math.floor(emi)}
      Funeraria: ${math.floor(fune)}
      Aprote al fondo de empleados: ${math.floor(fondo)}
      Retencion demanda de alimetos: ${math.floor(retencion)}
      =============================================
      AUMENTOS
      =============================================
      Auxilio de trasporte: ${math.floor(auxilio)}
      =============================================
      Salario Neto:${math.floor(salario_neto)}
      Salario Total a pagar con el auxilio de transporte es de : ${math.floor(total_s)}
      =============================================
      """)
