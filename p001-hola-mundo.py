# Leer y mostrar datos 

print('leyendo datos del usuario, luego envia un saludo')

nombre = input ('Dame tu nombre  :' )
edad   = input ('dame tu edad     :')
peso   = float (input ('dame tu peso   :')) # float convierte la cadena introducida a flotante

print(f'Bienvenido al lenguaje python {nombre} tu edad {edad} tu peso {peso}')

print( '\n')

print (type (nombre))
print (type (edad))
print (type (peso))


