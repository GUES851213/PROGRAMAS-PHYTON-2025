## Calculo de Notas 

print('Escribe  las 5 calificaciones ')

n1 = int (input('Dame la nota 1  '))
n2 = int (input('Dame la nota 2  '))
n3 = int (input('Dame la nota 3  '))
n4 = int (input('Dame la nota 4  '))
n5 = int (input('Dame la nota 5  '))

promedio = ((n1 + n2 + n3 + n4 + n5)/5)

if promedio > 0 and promedio < 6:  
    print ( 'Quedas reprobado')

elif promedio > 6 and promedio < 7:  
    print ( 'Pasas de panzazo')
elif promedio > 7 and promedio < 8:  
    print ( 'Muy bien, puedes mejorar')

elif promedio > 8 and promedio < 9:  
    print ( 'Excelente sigue asi')

elif promedio > 9 and promedio <= 10:  
    print ( 'Perfecto tu esfuerzo valio la pena')
    
else:
    print('ERROR ')