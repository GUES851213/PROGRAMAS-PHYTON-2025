##  Computacion aplicada Primer Examen Parcial 

print ('Universidad Patito SA de CV ')
print ('Sistema de inscripcion Congreso de Sistemas ')

print ('El congreso tiene distintos precios de inscripcion dependido de si eres Alumno, Trabajador o Docente y puedes participar en diferentes actividades que te señalamos abajo ')
print ('Estos son los precios Alumno:$100 Tranbajador:200 Docente:500')
print (' Paquetes \n solo conferencia $600 \n Con evento social:$800 \n Con kit de acceso:$900 ')




usuario = int(input('indica el tipo de usuario que eres: \n para alumno escribe 1 \n para Trabajador escribe 2 \n para Docente escribe 3 :  '))
paquete= int (input('cual paquete quieres \n Solo Conferencia escribe 1 \n Con evento social escribe 2 \n con kit de acceso escribe 3: '))
cantidad= int (input(' Que cantidad de paquetes requires: '))

estudiante = 100
trabajador = 200
docente = 500
conferencia = 600 
social = 800 
kit = 900


sub1= cantidad * (estudiante +conferencia)
sub2= cantidad * (estudiante + social)
sub3= cantidad * (estudiante + kit)
sub4= cantidad *(trabajador + conferencia)
sub5= cantidad * (trabajador + social)
sub6= cantidad * (trabajador + kit)
sub7= cantidad *(docente + conferencia)
sub8= cantidad * (docente + social)
sub9= cantidad * (docente + kit)

desal1 = (sub1*80)/100
total1= sub1 - desal1
desal2 = (sub2*80)/100
total2= sub2 - desal2
desal3= (sub3*80)/100
total3= sub3-desal3
destrab1= (sub4*90)/100
total4 = sub4-destrab1
destrab2= (sub5*90)/100
total5 = sub5-destrab2
destrab3= (sub6*90)/100
total6 = sub6-destrab3
desdoc1= (sub7*95)/100
total7 = sub7-desdoc1
desdoc2 = (sub8*95)/100
total8 = sub8 - desdoc2
desdoc3 = (sub9*95)/100
total9 = sub9 - desdoc3






if usuario == 1 and paquete == 1 and sub1>= 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: solo conferencia \n Subtotal:{sub1}, con un descuento de 20%:{desal1} y un total de: {total1}')
elif usuario == 1 and paquete == 1 and sub1 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: solo conferencia \n Subtotal:{sub1} total de: {sub1}')
elif usuario==1 and paquete ==2 and sub2 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub2}, con un descuento de 20%:{desal2} y un total de: {total2}')
elif usuario == 1 and paquete == 2 and sub2 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub2} total de: {sub2}')
elif usuario==1 and paquete ==3 and sub2 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub3}, con un descuento de 20%:{desal3} y un total de: {total3}')
elif usuario == 1 and paquete == 3 and sub3 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub3} total de: {sub3}')
elif usuario==2 and paquete ==1 and sub4 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub4}, con un descuento de 20%:{destrab1} y un total de: {total4}')
elif usuario == 2 and paquete == 1 and sub4 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub4} total de: {sub4}')
elif usuario==2 and paquete ==2 and sub5 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub5}, con un descuento de 20%:{destrab2} y un total de: {total5}')
elif usuario == 2 and paquete == 2 and sub5 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub5} total de: {sub5}')
elif usuario==2 and paquete ==3 and sub6 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub6}, con un descuento de 20%:{destrab3} y un total de: {total6}')
elif usuario == 2 and paquete == 3 and sub6 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub6} total de: {sub6}')
elif usuario==3 and paquete ==1 and sub7 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub7}, con un descuento de 20%:{desdoc1} y un total de: {total7}')
elif usuario == 3 and paquete == 1 and sub7 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub7} total de: {sub7}')
elif usuario==3 and paquete ==2 and sub8 >=5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub8}, con un descuento de 20%:{desdoc2} y un total de: {total8}')
elif usuario == 3 and paquete == 2 and sub8 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub8} total de: {sub8}')
elif usuario==3 and paquete ==3 and sub9 >5000 :
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub9}, con un descuento de 20%:{desdoc3} y un total de: {total9}')
elif usuario == 3 and paquete == 3 and sub2 < 5000:
    print (f' Tu pedido fue {cantidad}, Tipo de usuario : Alumno , Tipo de paquete: conferencia y evento social \n Subtotal:{sub9} total de: {sub9}')

else: 
    print ('Rectifica los datos que ingresaste')




