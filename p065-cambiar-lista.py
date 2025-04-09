# Ejemplificar la modificacion de elementos de una lista de numeros 


import os; os.system('clear')


nums = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(' Modificar elemento de una lista ')

print ( f' la lista es {nums}, contiene {len(nums)} elementos')

print ('modificar elemoento 0 y elemnto 1 :')
nums[0]=7
nums[1]=7
print(f'la lista es {nums}, contiene {len(nums)} elementos  ')
print ('\n modificar el rango de elementos de la posicion 2  en la posicion 5')

nums[2:5] = [9,9,9]

print ('la lista es {nums}, contiene {len(nums)} elementos')


