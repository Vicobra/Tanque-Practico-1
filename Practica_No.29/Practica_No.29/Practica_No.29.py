#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-
#Victor Alberto Rivera Cantero 19310429 6E2

#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categor�a' y 'Precio'. Muestra la �ltima clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categor�a': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categor�a': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 
 
teclado2.pop("Categor�a")
teclado2.pop("Precio")


print(teclado2["Modelo"])