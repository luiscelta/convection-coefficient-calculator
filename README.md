# Convection Coefficient Calculator

Calculadora de coeficientes de convección en Python, ejecutada por consola.

## Objetivo

Este programa calcula el coeficiente de convección (**h**) —o, en el caso de algunas cavidades, la conductividad térmica aparente (**k**)— para un amplio catálogo de problemas de transferencia de calor. Este proyecto tiene como objetivo facilitar y agilizar el cálculo del coeficiente de convección, que en los problemas de transferencia de calor, puede resultar tedioso de calcular a mano. El código es abierto, para que la comunidad pueda editarlo con el objetivo de crear una herramienta poderosa e intuitiva de utilizar de forma gratuita.

## Inspección rápida del programa

El usuario recorre un menú interactivo para definir:

- El **tipo de flujo** (convección natural/forzada, condensación natural/forzada).
- El **dominio** (interno/externo, cuando aplica).
- La **geometría** (y subtipo, cuando aplica): placas, cilindros, esferas, conductos, cavidades, haces de tubos, etc.
- El **fluido de trabajo** (aire, agua, refrigerantes, etc.)

A partir de esa selección, el programa:

1. Pide los datos numéricos necesarios para el caso elegido (temperaturas, dimensiones características, velocidades, etc.)
2. Calcula las propiedades del fluido a la(s) temperatura(s) correspondiente(s) mediante correlaciones propias por fluido.
3. Calcula los números adimensionales que correspondan (Reynolds, Prandtl, Grashof, Rayleigh).
4. Selecciona y aplica la correlación empírica adecuada para la geometría/régimen elegido, validando que los datos y los números adimensionales estén dentro del rango de aplicabilidad de la correlación.
5. Muestra un resumen de los datos introducidos, el resultado de la validación y el coeficiente de convección (o la conductividad, según el caso) obtenido.

## Cómo se usa

Requisitos: Python 3, sin dependencias externas (solo librería estándar).

Ejecutar desde la raíz del proyecto:

```
python src/main.py
```

El programa guía al usuario paso a paso:

1. Seleccionar el tipo de problema mediante los menús numerados (tipo de flujo → dominio → geometría → subtipo, según corresponda).
2. Seleccionar el fluido de trabajo.
3. Introducir los datos numéricos solicitados (en unidades del Sistema Internacional: °C para temperaturas, m para longitudes, m/s para velocidades, etc.)
4. El programa muestra los datos introducidos, valida su rango de aplicabilidad y presenta el resultado final: h [W/m²·K] o k [W/m·K].

## Bibliografía

Las correlaciones de convección y las propiedades de los fluidos implementadas en este proyecto están basadas la siguiente referencia: 

> Fernández Seara, J.; Rodríguez Alonso, C.; Uhía Vizoso, F. J.; Sieres Atienza, J. *Coeficientes de convección en casos prácticos. Correlaciones y programa de cálculo.* Editorial Ciencia 3, Madrid.

Que recopila las correlaciones originales de la literatura científica de transferencia de calor:

Para las referencias originales de cada correlación, consulta la bibliografía citada en dicha obra.

## Author

Developed by Luis Fernández Sotelo.

## Copyright

Copyright (C) 2026 Luis Fernández Sotelo

## License

This project is licensed under the GNU General Public License v3.0.
See the LICENSE file for details.
