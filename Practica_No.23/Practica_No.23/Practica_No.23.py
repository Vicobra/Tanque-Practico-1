#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-

#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
x = 0
while x <= 15:
    print(x)
    x+= 5

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
y = 0
while y >= -100:
    print(y)
    y-= 20
#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecuci�n esta frase con el valor de ejecuci�n correspondiente:
# 'El valor del bucle es 10'...
z=10
while z>=0:
    print("El valor del bucle es de\n" + str(z))
    z-= 1