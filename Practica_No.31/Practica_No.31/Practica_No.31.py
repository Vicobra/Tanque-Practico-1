
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_

#Victor Alberto Rivera Cantero 19310429 6E2

#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
#def colores(*args):
	#pass

#colores('rojo', 'azul', 'verde', 'amarillo')
#colores('lila', 'negro', 'rojo')
#colores('rosa')
#colores('marrón', 'naranja')

# 4 argumentos en el primero
# 3 argumentos en el segundo
# 1 argumento en el tercero
# 2 argumentos en la cuarta


#Completa el siguiente fragmento de código:

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco esta mal.')

colores('azul', 'verde')

#Crea una función que realice la suma de cinco números utilizando solo *args.
# Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print("El resultado es: ", resultado)

suma(10,6,4,2,3)