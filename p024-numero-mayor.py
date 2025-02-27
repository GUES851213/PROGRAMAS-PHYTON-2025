## Numero Mayor 

print('Escribe tres numeros para ver cual es el mayor')

n1 = int (input('Dame el primer numero '))

n2 = int (input('Dame el segundo numero '))

n3 = int (input ('Dame el tercer numero  '))

if n1>n2 and n1>n3:
    print(f'El numero mayor es {n1} ')

elif n2>n1 and n2>n3:
    print(f'El numero mayor es {n2} ')
    
else:
    print(f'El numero mayor es { n3 } ')
