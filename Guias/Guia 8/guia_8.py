from queue import LifoQueue as Pila #importa LifoQueue y le asigna el alias Pila
from queue import Queue as Cola #importa Queue y le asigna el alias Cola
from random import randint

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

#Armo una función que haga la copia de una pila:
#(Sacado de una clase del cuatri pasado)
def copia_pila(pila: Pila) -> Pila:
    pila_auxiliar: Pila = Pila()
    pila_copiada: Pila = Pila()

    #Invertimos la pila.
    while not pila.empty():
        elemento = pila.get()
        pila_auxiliar.put(elemento)

    #Hace la copia y restaura la original
    while not pila_auxiliar.empty():
        otro_elemento = pila_auxiliar.get()
        pila_copiada.put(otro_elemento)
        pila.put(otro_elemento)

    return pila_copiada

#Ejercicio 2:
def cantidad_elementos(p: Pila) -> int: #cuando paso como parámetro de entrada una pila y uso get() para recorrerla, voy a tener que restaurarla
    pila_auxiliar: Pila[int] = copia_pila(p) 
    res: int = 0
    while not pila_auxiliar.empty():
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
def copio_pila_int(p: Pila[int])->Pila[int]:
    pila_auxiliar: Pila[int] = Pila()
    pila_copiada: Pila[int] = Pila()

    #invertimos la pila
    while not p.empty():
        elemento = p.get()
        pila_auxiliar.put(elemento)

    #Hago la copia y restauro la pila original
    while not pila_auxiliar.empty():
        otro_elemento: int = pila_auxiliar.get()
        pila_copiada.put(otro_elemento)
        p.put(otro_elemento)
    return pila_copiada

def buscar_el_maximo(p: Pila[int])->int:
    pila_auxiliar: Pila[int] = copio_pila_int(p)
    res: int = pila_auxiliar.get()             
    while not pila_auxiliar.empty():
        numero: int = pila_auxiliar.get()
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
def copiar_pila_tuplas(p: Pila[tuple[str, int]])->Pila[tuple[str, int]]:
    pila_auxiliar: Pila[tuple[str, int]] = Pila()
    pila_copiada: Pila[tuple[str, int]] = Pila()

    #invertimos la pila
    while not p.empty():
        elemento = p.get()
        pila_auxiliar.put(elemento)

    #Hago la copia y restauro la pila original
    while not pila_auxiliar.empty():
        otro_elemento: tuple[str, int] = pila_auxiliar.get()
        pila_copiada.put(otro_elemento)
        p.put(otro_elemento)
    return pila_copiada

def buscar_nota_maxima(p: Pila[tuple[str, int]])->tuple[str, int]:
    pila_auxiliar: Pila[tuple[str, int]] = copiar_pila_tuplas(p)
    res: tuple[str, int] = pila_auxiliar.get()
    while not pila_auxiliar.empty():
        tupla: tuple[str, int] = pila_auxiliar.get()
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
    p1_aux: Pila = copia_pila(p1)
    p2_aux: Pila = copia_pila(p2)
    res: Pila = Pila()
    while not p1_aux.empty() and not p2_aux.empty():
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
def copiar_cola(c: Cola)->Cola:
    cola_auxiliar: Cola = Cola()
    cola_copiada: Cola = Cola()

    #Invertimos la cola
    while not c.empty():
        elemento = c.get()
        cola_auxiliar.put(elemento)

    #Hago la copia y restauro la cola original
    while not cola_auxiliar.empty():
        otro_elemento = cola_auxiliar.get()
        c.put(otro_elemento)
        cola_copiada.put(otro_elemento)

    return cola_copiada

def cantidad_elementos_cola(c: Cola)->int:
    cantidad: int = 0
    colaAuxiliar: Cola = copiar_cola(c)
    while not colaAuxiliar.empty():
        colaAuxiliar.get()
        cantidad+=1
    return cantidad

#Ejercicio 10
def copiar_cola_int(c: Cola[int])->Cola[int]:
    cola_auxiliar: Cola[int] = Cola()
    cola_copiada: Cola[int] = Cola()

    #Invertimos la cola
    while not c.empty():
        elemento: int = c.get()
        cola_auxiliar.put(elemento)

    #Hago la copia y restauro la cola original
    while not cola_auxiliar.empty():
        otro_elemento: int = cola_auxiliar.get()
        c.put(otro_elemento)
        cola_copiada.put(otro_elemento)

    return cola_copiada

def buscar_el_maximo(c: Cola[int])->int:
    cola_auxiliar: Cola[int] = copiar_cola_int(c)
    res: int = cola_auxiliar.get()
    while not cola_auxiliar.empty():
        numero: int = cola_auxiliar.get()
        if numero > res:
            res = numero
    return res 

#Ejercicio 11
def copiar_cola_tuplas(c: Cola[tuple[str, int]])->Cola[tuple[str, int]]:
    cola_auxiliar: Cola[tuple[str, int]] = Cola()
    cola_copiada: Cola[tuple[str, int]] = Cola()

    #Invertimos la cola
    while not c.empty():
        elemento: tuple[str, int] = c.get()
        cola_auxiliar.put(elemento)

    #Hago la copia y restauro la cola original
    while not cola_auxiliar.empty():
        otro_elemento: tuple[str, int] = cola_auxiliar.get()
        c.put(otro_elemento)
        cola_copiada.put(otro_elemento)
    return cola_copiada

def buscar_nota_minima(c: Cola[tuple[str, int]]) -> tuple[str, int]:
    cola_auxiliar: Cola[tuple[str, int]] = copiar_cola_tuplas(c)
    nota_minima: tuple[str, int] = cola_auxiliar.get()
    while not cola_auxiliar.empty():
        tupla = cola_auxiliar.get()
        if tupla[1] < nota_minima[1]:
            nota_minima = tupla
    return nota_minima

#Ejercicio 12:
def intercalar(c1: Cola, c2: Cola) -> Cola:
    c1_aux: Cola = copiar_cola(c1)
    c2_aux: Cola = copiar_cola(c2)
    res: Cola = Cola()
    while not c1_aux.empty() and not c2_aux.empty():
        res.put(c1_aux.get())
        res.put(c2_aux.get())
    return res