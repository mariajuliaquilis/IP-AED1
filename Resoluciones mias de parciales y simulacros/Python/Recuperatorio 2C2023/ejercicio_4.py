from typing import List, Tuple, Dict

# Ejercicio 4
"""
4) Molinete [3 puntos]

La forma de pago del transporte público varía ampliamente entre ciudades.
En muchas ciudades del mundo (Ej. París) existen alternativas de contratación del servicio con una tarifa plana.
Esto implica que pagando un monto fijo por mes (o por otros periodos de tiempo) es posible utilizar libremente 
el transporte, tantas veces como sea requerido.
Para esto, se carga la tarifa en una tarjeta con tecnología NFC (como la SUBE) y al subir a cada transporte se 
pasa la tarjeta por el sensor para verificar que se tenga contratado el servicio.

En el presente ejercicio vamos a trabajar con un diccionario (viajes_diarios) que registrará los usurarios que 
subieron a algún transporte cada día del mes.
El diccionario tendrá como clave el número de cada uno de los días del mes, y como valores, el registro de usuarios 
que pasaron su tarjeta por algún transporte público en el día correspondiente a la clave.

Implementar la función dias_viajados() que dado un diccionario viajes_diarios y una lista usurarios devuelva un nuevo diccionario,
con los elementos de usuarios como claves y como valor la cantidad de días en que el usuario tomó algún transporte. 

 problema viajes_por_dia(in viajes_diarios: dict⟨Z,seq⟨String⟩, in usuarios:⟨String⟩): dict⟨String, Z⟩ {
  requiere: {Las claves de viajes_diarios están entre 1 y 31}
  requiere: {La secuencia de usuarios no tiene elementos repetidos}
  requiere: {Cada valor de viajes_diarios es una secuencia de elementos de usuarios}
  asegura: {res tiene como claves a todos los elementos de usuarios}
  asegura: {Cada valor de res representa en cuántos valores de viajes_diarios aparece el usuario correspondiente}
}

Por ejemplo, dado el siguiente diccionario y lista de usuarios:

viajes_diarios = {1 : ["Juan", "Maria"], 2 : ["Marcela","Juan"]}
usuarios = ["Juan", "Maria", "Marcela"]

resultado_esperado es:
{"Juan" : 2, "Maria" : 1, "Marcela": 1}
"""

def viajes_por_dia(viajes_diarios: dict[int, List[str]],  usuarios:List[str])-> dict[str, int]:
    return {}