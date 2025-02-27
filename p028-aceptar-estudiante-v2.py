## Aceptar estudiante 

print('Proceso de validacion de estudiantes ')

print (' el proceso de validacion requiere que proporciones tu nombre, sexo, edad y tres calificaciones para ver si eres aceptado ')


edad = int(input ('Dame tu edad:  '))
sexo = str.upper( input('Sexo: ') )

nombre = input(('Dame tu nombre : '))


cal1 = int(input (' Calificacion 1 :  '))

cal2 =  int (input (' Calificacion 2 :  '))
Cal3 =  int (input (' Calificacion 3 :  '))

promedio = int ((cal1 + cal2 + Cal3)/3)

if  edad > 21 and sexo=='M' and promedio >8 :
    
        print (f'{nombre} has sido aceptada, tu edad de {edad} y tus calificaciones {cal1}, {cal2}, y {Cal3}, lo permiten') 
elif sexo=='H' :
      print ('Lo siento solo se aceptan mujeres')

elif edad < 21:
      print (' Eres mujer, pero no tienes la edad, solo mayores a 21 años se aceptan')
elif promedio <8 :
      print ('Eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios mayores a 8 ')
else:
    print   ('error')


    

