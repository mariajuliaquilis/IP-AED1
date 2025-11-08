from queue import Queue as Cola

"""
Ejercicio 1 [2.25 puntos]
problema maximas_cantidades_consecutivos (in v: seq⟨Z⟩) : Diccionario⟨Z,Z⟩ { 
    requiere: { True }  
    asegura: { Las claves de res son exactamente los números que aparecen al menos una vez en v }  
    asegura: { Para cada clave k de res, su valor es igual a la máxima cantidad de apariciones consecutivas de k en v, }
    donde dicha cantidad de apariciones es mayor o igual 1. }}
"""
def cant_apariciones(lista: list[int], elemento: int) -> int:
    cantidad: int = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            cantidad+=1
    return cantidad

def apariciones_consecutivas(lista: list[int], elemento: int) -> int:
    subsecuencia_actual: list[int] = []
    max_subsecuencia: list[int] = []
    cantidad_actual: int = 0
    cantidad_maxima: int = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            subsecuencia_actual.append(lista[i])
            cantidad_actual+=1
        else:
            if len(subsecuencia_actual) > len(max_subsecuencia):
                max_subsecuencia = subsecuencia_actual
                subsecuencia_actual = []
                cantidad_maxima = cantidad_actual
                cantidad_actual = 0

    if len(subsecuencia_actual) > len(max_subsecuencia):
        max_subsecuencia = subsecuencia_actual
        cantidad_maxima = cantidad_actual
    return cantidad_maxima

def maximas_cantidades_consecutivos(v: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}
    for i in range(len(v)):
        if cant_apariciones(v, v[i]) == 1:
            res[v[i]] = cant_apariciones(v, v[i])
        else:
            res[v[i]] = apariciones_consecutivas(v, v[i])
    return res

lista_1: list[int] = []
print(maximas_cantidades_consecutivos(lista_1)) #debe dar {}
lista_2: list[int] = [1]
print(maximas_cantidades_consecutivos(lista_2)) #debe dar {1:1}
lista_3: list[int] = [1,2]
print(maximas_cantidades_consecutivos(lista_3)) #debe dar {1:1, 2:1}
lista_4: list[int] = [1,1,2,1]
print(maximas_cantidades_consecutivos(lista_4)) #debe dar {1:2, 2:1}
lista_5: list[int] = [1,2,2,2,1,2,2]
print(maximas_cantidades_consecutivos(lista_5)) #debe dar {1:1, 2:3}
lista_6: list[int] = [1,2,2,2]
print(maximas_cantidades_consecutivos(lista_6)) #debe dar {1:1, 2:3}

"""
Ejercicio 2 [2.25 puntos]
problema maxima_cantidad_primos(in A: seq⟨seq⟨Z⟩⟩) : Z {  
    requiere: { Todas las filas de A tienen la misma longitud } 
    asegura: { Existe alguna columna c en A para la cual res de sus elementos son números primos }  
    asegura: { Todas las columnas de A tienen a lo sumo res elementos que son números primos }}
"""
def lista_numeros(numero: int) -> list[int]:
    res: list[int] = []
    indice: int = 1
    while indice <= numero:
        res.append(indice)
        indice+=1
    return res 

def lista_divisores(lista: list[int], numero: int) -> list[int]:
    res: list[int] = []
    for elemento in lista:
        if numero % elemento == 0:
            res.append(elemento)
    return res

def es_primo(numero: int) -> bool:
    return lista_divisores(lista_numeros(numero), numero) == [1, numero]

def maxima_cantidad_primos(A: list[list[int]]) -> int:
    cantidad_maxima = 0
    for j in range(len(A[0])):
        cantidad_actual = 0
        for i in range(len(A)):
            if es_primo(A[i][j]):
                cantidad_actual+=1
        if cantidad_actual > cantidad_maxima:
            cantidad_maxima = cantidad_actual
    return cantidad_maxima

matriz_1: list[list[int]] = [[1,2,3,4],
                             [2,0,10,8],
                             [2,3,6,0],
                             [5,4,1,9]
                          ]
print(maxima_cantidad_primos(matriz_1)) #debe dar 3

matriz_2: list[list[int]] = [[]]
print(maxima_cantidad_primos(matriz_2)) #debe dar 0

matriz_3: list[list[int]] = [[1,4,9,12],
                             [4,8,10,12],
                             [6,8,20,25],
                             [10,15,20,30]
                          ]
print(maxima_cantidad_primos(matriz_3)) #debe dar 0

matriz_4: list[list[int]] = [[2,3,5,7],
                             [3,4,11,10],
                             [13,8,19,15],
                             [29,30,107,20]
]
print(maxima_cantidad_primos(matriz_4)) #debe dar 4

matriz_5: list[list[int]] = [[3]]
print(maxima_cantidad_primos(matriz_5)) #debe dar 1

"""
Ejercicio 3 [2.25 puntos]
Dadas las siguientes definiciones:
Tupla positiva: par de números enteros en el cual el producto de ambos números es positivo. Ejemplo: (2,3)
Tupla negativa: par de números enteros en el cual el producto de ambos números es negativo. Ejemplo: (3,-2)
Tupla nula: par de números enteros en el cual el producto de ambos números es igual a cero. Ejemplo: (0,0)
Se pide resolver:
problema tuplas_positivas_y_negativas(inout c: Cola⟨ZxZ⟩ ) {  
    requiere: { c no tiene tuplas repetidas } 
    modifica: { c } 
    asegura: { c contiene todas las tuplas positivas y todas las tuplas negativas de c@pre y además no contiene ninguna otra tupla } 
    asegura: { No hay niguna tupla negativa en c que aparezca antes que alguna tupla positiva }
    asegura: { Para todas las tuplas positivas t1 y t2 en c, con t1 != t2, si t1 aparece antes que t2 en c@pre, entonces t1 aparece antes que t2 en c }  
    asegura: { Para todas las tuplas negativas t1 y t2 en c, con t1 != t2, si t1 aparece antes que t2 en c@pre, entonces t1 aparece antes que t2 en c }}
"""

# def copia_cola(c: Cola[tuple[int, int]]) -> Cola[tuple[int, int]]:
#     cola_auxiliar: Cola[tuple[int, int]] = Cola()
#     cola_copia: Cola[tuple[int, int]] = Cola()
#     #Invertimos c
#     while not c.empty():
#         elemento: tuple[int, int] = c.get()
#         cola_auxiliar.put(elemento)
#     #Restauro la cola original y hago la copia
#     while not cola_auxiliar.empty():
#         otro_elemento: tuple[int, int] = cola_auxiliar.get()
#         c.put(otro_elemento)
#         cola_copia.put(otro_elemento)
#     return cola_copia

def tuplas_positivas_y_negativas(c: Cola[tuple[int, int]]):
    cola_auxiliar: Cola[tuple[int, int]] = Cola()

    while not c.empty():
        elemento: tuple[int, int] = c.get()
        cola_auxiliar.put(elemento)

    cola_tuplas_positivas: Cola[tuple[int, int]] = Cola()
    cola_tuplas_negativas: Cola[tuple[int, int]] = Cola()
    cola_tuplas_nulas: Cola[tuple[int, int]] = Cola()

    while not cola_auxiliar.empty():
        elemento: tuple[int, int] = cola_auxiliar.get()
        multiplicacion: int = elemento[0]*elemento[1]
        if multiplicacion > 0:
            cola_tuplas_positivas.put(elemento)
        elif multiplicacion < 0:
            cola_tuplas_negativas.put(elemento)
        else:
            cola_tuplas_nulas.put(elemento)


    while not cola_tuplas_positivas.empty():
        elemento_tuplas_positivas: tuple[int, int] = cola_tuplas_positivas.get()
        c.put(elemento_tuplas_positivas)

    while not cola_tuplas_negativas.empty():
        elemento_tuplas_negativas: tuple[int, int] = cola_tuplas_negativas.get()
        c.put(elemento_tuplas_negativas)

c: Cola = Cola()
c.put([1,0])
c.put([2, 4])
c.put([3,-9])
c.put([0,0])
c.put([9,8])
print(c.queue)
print(tuplas_positivas_y_negativas(c))
print(c.queue)
    

"""
Ejercicio 4 [2.25 puntos]
problema resolver_cuenta(in s: string): R { 
     requiere: { Cada caracter de s es '+', '-', '.' (separador decimal) o es un dígito}
     requiere: { No hay dos operadores consecutivos en s (los operadores son '+' y '-') } 
     requiere: { El último caracter de s es un dígito }  
     requiere: { El primer caracter de s es un dígito o un operador }  
     requiere: { En las posiciones adyacentes a cada aparición de '.' en s, hay un dígito } 
     requiere: { Entre un operador y el operador inmediato siguiente hay a lo sumo un separador decimal }  
     requiere: { Antes del primer operador hay a lo sumo un separador decimal }  
     requiere: { Después del último operador hay a lo sumo un separador decimal }  
     asegura: { res es igual al resultado de la operación aritmética representada por s }}
Hint: las funciones int o float permiten convertir strings en números enteros o flotantes respectivamente.
Ejemplo: Para el input "+10" se debe devolver 10
"""
def resolver_cuenta(s: str) -> float:
    resultado: float = 0.0
    guardo_numero: str = '0'
    guardo_operando: str = ''

    for i in range(len(s)):
        if s[i] != '+' and s[i] != '-':
            guardo_numero += s[i]
        else:
            if s[i] == '+':
                if guardo_operando == '':
                    guardo_operando = s[i]
                    resultado = float(guardo_numero)  
                    guardo_numero = ''
                elif guardo_operando == '-':
                    resultado-=float(guardo_numero)
                    guardo_operando = s[i]
                    guardo_numero = ''
                else:
                    resultado+=float(guardo_numero)
                    guardo_numero = ''
            else:
                if guardo_operando == '':
                    guardo_operando = s[i]
                    resultado = float(guardo_numero)  
                    guardo_numero = ''
                elif guardo_operando == '+':
                    resultado+=float(guardo_numero)
                    guardo_operando = s[i]
                    guardo_numero = ''
                else:
                    resultado-=float(guardo_numero)
                    guardo_numero = ''

    if guardo_operando == '+':
        resultado+=float(guardo_numero)
    elif guardo_operando == '-':
        resultado-=float(guardo_numero)
    else:
        resultado = float(guardo_numero)
    return resultado 

ecuacion: str = '12+13-25'
print(resolver_cuenta(ecuacion))
ec: str = '+8'
print(resolver_cuenta(ec))
otra_ecuacion: str = '12.5 + 3'
print(resolver_cuenta(otra_ecuacion))
aaa: str = '1'
print(resolver_cuenta(aaa))


"""
Ejercicio 5) Pregunta teórica (1 punto)
Conteste marcando la opción correcta.

La principal diferencia entre testing de caja blanca y de caja negra es que en testing de caja blanca tenemos acceso a:
1) Al código fuente del programa que queremos testear
2) A la documentación del programa que queremos testear
3) Al Control Flow Graph (CFG) del programa que queremos testear
"""
#Ejercicio 5) Al Control Flow Graph (CFG) del programa que queremos testear
