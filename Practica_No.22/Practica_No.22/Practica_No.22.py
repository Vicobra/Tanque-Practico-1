#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-

#Haz una tupla que contenga cuatro colores de tu elecci�n. 
#Tendr�s que poner una condici�n con el condicional if para cada color que le avise al usuario que el color est� en la tupla con un mensaje como este: 
#print('El color rojo est� admitido') y una condici�n False para contemplar cualquier color que no est� en la tupla con un mensaje como este: 
#print('Color no admitido'). 
#No puedes utilizar el operador ==. Adem�s tendr�s que hacer esto con un input() que permita introducir un color al usuario.

colores = ('verde', 'azul', 'naranja', 'rosa')
entrada = input("Introduzca un color:\n")

if entrada in colores[0]:
    print("el color verde esta permitido ")

elif entrada in colores[1]:
    print("el color azul esta permitido")

elif entrada in colores[2]:
    print("el color naranja esta permitido")

elif entrada in colores[3]:
    print("el color rosa esta permitido")

else:
    print("el color no esta permitido")
