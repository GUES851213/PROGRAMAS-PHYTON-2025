# Dividir un numero entero de 3 cifras en unidades, decenas, y centenas 
#145

import os; os.system ('clear')

print('Dividir un numero entero de 3 cifras en unidades, decenas y centenas')

n= int (input('Dame un número entero de 3 cifras: '))

# n = 145

u = n % 10
n = n // 10
d = n % 10
n = n // 10
c = n

print(f'Centenas: {c} \nDecenas: {d}\nUnidades: {u}')
