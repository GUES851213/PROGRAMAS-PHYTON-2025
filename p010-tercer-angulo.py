# Calcular el terer angulo de un triangulo 



print('Vamos a calcular el tercer angulo de un triangulo ')
print ('Necesito que me proporciones la medida de dos angulos')

angulo1 = int (input('Cuantos grados tiene el angulo  1:  '))
angulo2 = int (input('Cuantos grados tiene el angulo  2:  '))



angulo3 = 180 - (angulo1 + angulo2)



print(f'La medida del tercer angulo es:  {angulo3}')
