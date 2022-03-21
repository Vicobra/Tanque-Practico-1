#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-

#Crea un bucle while con las siguientes características:
#El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será mayor o igual a 30.
#La ejecución se deberá romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.

x = 0
while x < 30:
    x+=1
    if x == 4 or x == 6 or x == 10:
        print('se salto el valor ' + str(x) + " " + 'de x')
        continue 
     
    if x==15:
        break
    print('el valor del bucle es de ', x)

print('Se rompió la ejecución del bucle cuando x valía ' + str(x))
