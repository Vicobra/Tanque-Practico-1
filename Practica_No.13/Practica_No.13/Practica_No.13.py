#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-

#Elimina de la siguiente lista los elementos 'azul' y 'blanco'. Solo puedes eliminarlos utilizando el m�todo pop(). Adem�s, tendr�s que guardar esos dos colores en una nueva lista.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marr�n', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
savethem= colores.pop(1)
savethem2= colores.pop(-2)
colores3 = [savethem, savethem2] 

print(colores) 
print(colores3)

