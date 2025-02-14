# Calcular la Hipotenusa de un triangulo

import math


print('Vamos a calcular la Hipotenusa de un triangulo ')
print ('Necesito que me proporciones las longitudes de dos lados')

longlado1 = int (input('Dame la longitud del lado 1:  '))
longlado2 = int (input('Dame la longitud del lado 2:  '))
raizcuadrada = math.sqrt
hipotenusa = raizcuadrada ( longlado1 * longlado1 + longlado2 * longlado2 )



print(f'la medida de la hipotenusa es {hipotenusa}')

