# Calcular el volumen de un cilindro 

import math

print('Vamos a calcular el volumen de un cilindro ')
print ('Necesito que me proporciones la medida del radio y la altura ')

Radio =  int (input('Cual es la medida del radio:  '))
Altura = int (input('Cual es la medida de la altura:  '))
PI = math.pi

Volumen = PI * (Radio * Radio) * Altura





print(f'El volumen del cilindro es:  {Volumen}')