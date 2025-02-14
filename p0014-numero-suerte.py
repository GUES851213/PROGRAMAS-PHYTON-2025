# Calcular el numero de la suerte 

import math


print('Vamos a conocer tu numero de la suerte')


print('Proporciona el año en que naciste')


añodenacimiento = int(input('En que año naciste: '))

millares = math.trunc (añodenacimiento / 1000)
centenas = math.trunc( (añodenacimiento - (millares * 1000)) / 100 )
decenas = math.trunc( ((añodenacimiento - (millares *1000)) - (centenas * 100)) / 10 )
unidades = math.trunc(añodenacimiento - millares *1000 - centenas * 100 - decenas *10)


print(f'millares: {millares}, centenas: {centenas}, decenas: {decenas} , unidades {unidades}')

suma = millares + centenas + decenas + unidades

print (f'tu numero de la suerte es:  {suma} ')