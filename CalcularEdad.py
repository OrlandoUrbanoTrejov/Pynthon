################################################
# Author : Orlando Urbano Trejo (Lando)        #
# Fecha  : 19102021                            #
################################################

Fecha_Nacimiento = input ("Digite anio de nacimiento: ")
Diferencia = (2021 - int(Fecha_Nacimiento))

if Diferencia >= 18:
    print("Con ", Diferencia," es mayor de edad")
else: 
    print("Con ", Diferencia," es menor de edad")

