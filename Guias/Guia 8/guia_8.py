from queue import LifoQueue as Pila #importa LifoQueue y le asigna el alias Pila
from random import randint
from copy import copy

#PILAS

#Ejercicio 1:
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int)->Pila[int]:
    res: Pila[int] = Pila()
    for i in range(cantidad):
        numero: int = randint(desde, hasta)
        res.put(numero)
    return res

#Ejercicio 2:
def cantidad_elementos(p: Pila) -> int: #cuando paso como parámetro de entrada una pila y uso get() para recorrerla, voy a tener que restaurarla
    pila_auxiliar: Pila[int] = copy(p)  #genero una copia para no modificar la pila original
    res: int = 0
    while pila_auxiliar.empty() != True:
        pila_auxiliar.get()
        res+=1
    return res
"""
p = Pila()
p.put(5)
p.put(4)
p.put(9)
p.put(1)
print(cantidad_elementos(p))
"""

#Ejercicio 3:
def buscar_el_maximo(p: Pila[int])->int:
    pila_auxiliar: Pila[int] = copy(p)
    res: int = pila_auxiliar.get()     #tomo como máximo el último elemento insertado
    while pila_auxiliar.empty() != True:
        numero = pila_auxiliar.get()
        if numero > res:
            res = numero 
    return res 
"""
p = Pila()
p.put(4)
p.put(9)
p.put(34)
p.put(5)
print(buscar_el_maximo(p))
"""

#Ejercicio 4:
def buscar_nota_maxima(p: Pila[tuple[str, int]])->tuple[str, int]:
    pila_auxiliar: Pila[tuple[str, int]] = copy(p)
    res: tuple[str, int] = pila_auxiliar.get()
    while pila_auxiliar.empty() != True:
        tupla = pila_auxiliar.get()
        if tupla[1] > res[1]:
            res = tupla 
        
    return res

"""
p = Pila()
p.put(("Ana", 8))
p.put(("Sergio", 7))
p.put(("Sofia", 10))
p.put(("Ramiro", 6))
print(buscar_nota_maxima(p))
"""

