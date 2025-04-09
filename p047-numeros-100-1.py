# Numeros del 100 al 1 con for


print('Numeros del x al 0 con for \n')

x= int (input( 'desde donde?  '))
i= int (input('decremento ?  '))

for n in range(x,  0, -i):
    print(n, end='  ')
print ('\n llegamos al final')