#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# -*- coding: utf-8 -*-
#Victor Alberto Rivera Cantero 19310429 6E2

#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
#Categoría = Teclados.
#Modelo = HyperX Alloy FPS Pro.
#Precio = 89,99.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado1:
	print(x + " = " + teclado1[x] + ".")

