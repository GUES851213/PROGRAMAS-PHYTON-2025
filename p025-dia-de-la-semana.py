## Dia de la semana

print('Escribe un numero entre el 1 y el 7 y te mostrare a que dia corresponde de la semana')

n1 = int (input('Dame un numero  '))


if n1== 1:
    print(f'El numero que me diste corresponde al Domingo')

elif n1==2:
    print(f'El numero que me diste corresponde al Lunes')

elif n1==3:
    print(f'El numero que me diste corresponde al Martes')
elif n1==4:
    print(f'El numero que me diste corresponde al Miercoles')
elif n1==5:
    print(f'El numero que me diste corresponde al Jueves')
elif n1==6:
    print(f'El numero que me diste corresponde al Viernes')
elif n1==7:
    print(f'El numero que me diste corresponde al Sabado')
    
else:
    print('ERROR ')
