# En Colombia hay medidas que regulan la velocidad de los automóviles según las
# zonas donde se encuentre. A continuación, se listan las restricciones
# ✓ 30KM/H – Zonas Escolares
# ✓ 60KM/H – Vías Urbanas
# ✓ 80KM/H – Vías Rurales
# ✓ 100KM/H – Rutas Nacionales
# Realice un programa que permita determinar según una velocidad X generada
# automáticamente por el sistema, a qué grupo de restricciones pertenezco, la
# velocidad a la que va, a cuál debería ir y si estoy infringiendo los límites de
# velocidad. Usted debe redondear el kilometraje obtenido y aplicarle un decimal.
# Usted debe utilizar condicionales para resolver este ejercicio y aplicar todo lo visto.

import random
velocidad = round(random.randint(0,120),1)
if velocidad <= 30:
    print(f"""Con la velocidad que llevas actualmente estas para poder transcurrir en cualquier zona escolar
          Vas a {velocidad} KM/H
          Manten esta velocidad para no infringir superar los limites de la zona escolar.""")
elif velocidad > 30 and velocidad <= 60:
    print(f"""Con la velocidad que llevas actualmente estas para poder transcurrir en vias urbanas
          Vas a {velocidad} KM/H
          Manten esta velocidad para no infringir superar los limites de las vias urbanas.""")
elif velocidad > 60 and velocidad <= 80:
    print(f"""Con la velocidad que llevas actualmente estas para poder transcurrir en vias rurales, 
          Vas a {velocidad} KM/H
          Manten esta velocidad para no infringir superar los limites de las vias rurales.""")
elif velocidad > 80 and velocidad <= 100:
    print(f"""Con la velocidad que llevas actualmente estas para poder transcurrir en rutas nacionales, 
          Vas a {velocidad} KM/H 
          Manten esta velocidad para no infringir superar los limites de las rutas nacionales.""")
else:
    print(f"""ESTAS SOBREPASANDO TODOS LOS LIMITES DE VELOCIDAD, ESTAS INCLUMPIEDO LA NORMA DE TRANCITO, 
          VAS A {velocidad} KM/H 
          RESIVIRAS UNA MUTA POR SUPERAR EL LIMITE DE TODAS LAS VIAS.""")