from queue import LifoQueue as Pila #importa LifoQueue y le asigna el alias Pila
from queue import Queue as Cola #importa Queue y le asigna el alias Cola
from random import randint
from copy import copy

#PILAS

"""
p = Pila()         #crea una pila
p.put(1)           #apila un 1
elemento = p.get() #desapila
p.empty ()         #devuelve true si y solo si la pila está vacía
"""

#Ejercicio 1:
def generar_nros_al_azar_pila(cantidad: int, desde: int, hasta: int)->Pila[int]:
    res: Pila[int] = Pila()
    for i in range(cantidad):
        numero: int = randint(desde, hasta)
        res.put(numero)
    return res

#Ejercicio 2:
def cantidad_elementos(p: Pila) -> int: #cuando paso como parámetro de entrada una pila y uso get() para recorrerla, voy a tener que restaurarla
    pila_auxiliar: Pila[int] = copy(p)  #genero una copia para no modificar la pila original
    res: int = 0
    while not(pila_auxiliar.empty()):
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
    while not(pila_auxiliar.empty()):
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
    while not(pila_auxiliar.empty()):
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
#Ejercicio 7:
def intercalar_pilas(p1: Pila, p2: Pila) -> Pila:
    p1_aux: Pila = copy(p1)
    p2_aux: Pila = copy(p2)
    res: Pila = Pila()
    while not(p1_aux.empty()) and not(p2_aux.empty()):
        res.put(p1_aux.get())
        res.put(p2_aux.get())
    return res

#COLAS

"""
c = Cola()         #creo una cola
c.put(1)           #encolo el 1
elemento = c.get() #desencolo
c.empty ()         #devuelve true si y solo si la cola está vacía
"""

#Ejercicio 8
def generar_nros_al_azar_cola(cantidad: int, desde: int, hasta: int)-> Cola[int]:
    res: Cola[int] = Cola()
    for i in range(cantidad):
        numero: int = randint(desde, hasta)
        res.put(numero)
    return res

#Ejercicio 9
def cantidad_elementos_cola(c: Cola)->int:
    cantidad: int = 0
    colaAuxiliar: Cola = copy(c)
    while not(colaAuxiliar.empty()):
        colaAuxiliar.get()
        cantidad+=1
    return cantidad

#Ejercicio 10
def buscar_el_maximo(c: Cola[int])->int:
    cola_auxiliar: Cola[int] = copy(c)
    res: int = cola_auxiliar.get()
    while not(cola_auxiliar.empty()):
        numero = cola_auxiliar.get()
        if numero > res:
            res = numero
    return res 

#Ejercicio 11
def buscar_nota_minima(c:Cola[tuple[str, int]])->tuple[str, int]:
    cola_auxiliar: Cola[tuple[str, int]] = copy(c)
    nota_minima: tuple[str, int] = cola_auxiliar.get()
    while not(cola_auxiliar.empty()):
        tupla = cola_auxiliar.get()
        if tupla[1] < nota_minima[1]:
            nota_minima = tupla
    return nota_minima

#Ejercicio 12:
def intercalar(c1: Cola, c2: Cola)->Cola:
    c1_aux: Cola = copy(c1)
    c2_aux: Cola = copy(c2)
    res: Cola = Cola()
    while not(c1_aux.empty()) and not(c2_aux.empty()):
        res.put(c1_aux.get())
        res.put(c2_aux.get())
    return res