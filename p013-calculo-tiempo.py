# Calcular el tiempo 

import math


print('Vamos a dar la equivalencia en dias minutos y segundos de la cantidad de horas que nos proporciones')


Horas = int (input('Dame la cantidad de horas :  '))

Dias = float (Horas/24)

Minutos = int (Horas * 60)

Segundos = int (Horas * 3600 )


print(f'Las {Horas} corresponden a {Dias} dias, {Minutos} minutos, y {Segundos} segundos')