#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-

#Crea un bucle while con las siguientes caracter�sticas:
#El valor inicial de la variable x ser� de 0.
#El valor de incremento ser� 1.
#La condici�n de salida del bucle ser� mayor o igual a 30.
#La ejecuci�n se deber� romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecuci�n, deber�s mostrar los valores saltado con este mensaje: 'Se salt� el valor ' + x ' de x'.
#Cuando se rompa la ejecuci�n del bucle deber�s mostrar un mensaje indic�ndolo: 'Se rompi� la ejecuci�n del bucle cuando x val�a ' + x.

x = 0
while x < 30:
    x+=1
    if x == 4 or x == 6 or x == 10:
        print('se salto el valor ' + str(x) + " " + 'de x')
        continue 
     
    if x==15:
        break
    print('el valor del bucle es de ', x)

print('Se rompi� la ejecuci�n del bucle cuando x val�a ' + str(x))
