## Ejemplificar el acceso a una lista de numeros 



import os; os.system('clear')


nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]


print('Acceder a los elementos de una lista\n')

print(f'la lista completa es: {nums}, tiene {len(nums)} elementos ')
print(f'Primer elemento: {nums [0] }, ultimo elemnto : {nums[8]}')
print(f'Primero elemento: {nums [-9]}. ultimo elemento:{nums[-1]} ')
print(f'Del 2 al 6 : {nums[2:6]}')
print(f'Los primeros 3 : {nums[:3]} ')
print(f'Los últimos 3 : {nums[6:]}')