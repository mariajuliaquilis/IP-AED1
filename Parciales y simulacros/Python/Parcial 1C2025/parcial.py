from queue import Queue as Cola

"""
Ejercicio 1 [2 puntos]
Implementar la función cantidad_parejas_que_suman:
problema cantidad_parejas_que_suman (in s: seq⟨Z⟩, in n: Z) : Z {
    requiere: { - }
    asegura: { res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j) }
}
Ejemplo: cantidad_parejas_que_suman([1,3,2,5,4,8], 5) debe devolver 2
"""
def pertenece(s: list[int], elemento: int) -> bool:
    for i in range(len(s)):
        if s[i] == elemento:
            return True
    return False

def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    cantidad: int = 0
    lista: list[int] = []
    for i in range(len(s)):
        if not pertenece(lista, s[i]):
            for j in range(i+1, len(s)):
                if s[i] + s[j] == n:
                    cantidad+=1
    return cantidad

lista_1: list[int] = [1,3,2,5,4,8]
elemento_1: int = 5
print(cantidad_parejas_que_suman(lista_1, elemento_1)) #debe dar 2
lista_2: list[int] = []
elemento_2: int = 3
print(cantidad_parejas_que_suman(lista_2, elemento_2)) #debe dar 0
lista_3: list[int] = [1,4,7,0,11]
elemento_3: int = 11
print(cantidad_parejas_que_suman(lista_3, elemento_3)) #debe dar 2

"""
Ejercicio 2 [2,5 puntos]
En un supermercado tenemos una fila de clientes esperando para ser atendidos por algún cajero. Cada cliente tiene un nombre, 
un método de pago y una cantidad de productos. La fila de clientes se representa como una Cola de String x String x Z, donde 
el primer elemento es el nombre del cliente, el segundo es el método de pago y el tercero es la cantidad de productos. 
Implementar la función pasar_por_autoservicio:

Nota: los métodos de pago son strings conformados por letras minúsculas.

problema pasar_por_autoservicio (inout clientes: Cola⟨ String x String x Z ⟩) : String {
    requiere:{ Las primeras componentes de clientes son strings no vacíos y todos distintos entre sí }
    requiere:{ Las terceras componentes de clientes son números positivos }
    requiere:{ Existe al menos un elemento c dentro de la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15 }
    modifica: { clientes }
    asegura: { Sea c el primer elemento insertado en la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15, entonces res = c0 }
    asegura: { clientes contiene todos los elementos de clientes@pre excepto la tupla que contiene a res en su primera posición, 
               en el mismo orden que en clientes@pre. }
}

Ejemplo: pasar_por_autoservicio(clientes) debe devolver "Bruno" (y quitar su tupla de la cola) si clientes es una cola en la 
cual se insertaron (en orden) los siguientes elementos:
1. ("Ana", "efectivo", 13)
2. ("Juan", "qr", 22)
3. ("Bruno", "tarjeta", 14)
"""
def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    res: str = ""
    cola_auxiliar: Cola[tuple[str, str, int]] = Cola()

    while not clientes.empty():
        elemento: tuple[str, str, int] = clientes.get()
        cola_auxiliar.put(elemento)
    while not cola_auxiliar.empty():
        otroElemento: tuple[str, str, int] = cola_auxiliar.get()
        if otroElemento[1] != "efectivo" and otroElemento[2] <= 15 and res == "":
            res+= otroElemento[0]
        else:
            clientes.put(otroElemento)
    return res

cola_1: Cola[tuple[str, str, int]] = Cola()
cola_1.put(("Ana", "efectivo", 13))
cola_1.put(("Juan", "qr", 22))
cola_1.put(("Bruno", "tarjeta", 14))
print(cola_1.queue)
print(pasar_por_autoservicio(cola_1))
print(cola_1.queue)

cola_2: Cola[tuple[str, str, int]] = Cola()
cola_2.put(("Ana", "efectivo", 13))
cola_2.put(("Juan", "qr", 22))
cola_2.put(("Bruno", "tarjeta", 14))
cola_2.put(("Agustina", "qr", 20))
cola_2.put(("Martín", "qr", 11))
print(cola_2.queue)
print(pasar_por_autoservicio(cola_2))
print(cola_2.queue)

"""
Ejercicio 3 [2,5 puntos]
Implementar la función intercambiar_e_invertir_columnas:
problema intercambiar_e_invertir_columnas(inout A: seq⟨seq⟨Z⟩⟩, in col1: Z, in col2: Z) {
    requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva)}
    requiere: { |A| > 0}
    requiere: { 0 ≤ col1 < |A[0]| }
    requiere: { 0 ≤ col2 < |A[0]| }
    requiere: { col1 ≠ col2 }
    modifica: { A }
    asegura: { A tiene exactamente las mismas dimensiones que A@pre }
    asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que j ≠ col1 y j ≠ col2 }
    asegura: { A[i][col1] = A@pre[|A|-1-i][col2] para todo i tal que 0 ≤ i < |A| }
    asegura: { A[i][col2] = A@pre[|A|-1-i][col1] para todo i tal que 0 ≤ i < |A| }
}

Ejemplo: Si mat = [[1,2,3],[40,50,60], [-7,-8,-9]], luego de ejecutarse intercambiar_e_invertir_columnas(mat,1,2)
debería ocurrir que print(mat) muestre [[1, -9, -8], [40, 60, 50], [-7, 3, 2]]
"""

def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int):
    guardo_columna_col1: list[int] = []
    guardo_columna_col2: list[int] = []

    for i in range(len(A)):
        guardo_columna_col1.append(A[i][col1])
        guardo_columna_col2.append(A[i][col2])

    for j in range(len(A)):
        A[j][col1] = guardo_columna_col2[len(A)-1-j]
        A[j][col2] = guardo_columna_col1[len(A)-1-j]

mat = [[1,2,3],[40,50,60], [-7,-8,-9]]
print(mat)
print(intercambiar_e_invertir_columnas(mat,1,2)) #debe mostrar [[1, -9, -8], [40, 60, 50], [-7, 3, 2]]
print(mat)

"""
Ejercicio 4 [2 puntos]
Se realizaron dos censos en los cuales se le preguntó a cada persona en que localidad vive. Estos datos fueron almacenados en dos 
diccionarios cuyas claves son los nombres de las personas, y sus valores las localidades en las cuales viven. 
Implementar la función mantuvieron_residencia:

problema mantuvieron_residencia (in censo1: Diccionario⟨String,String⟩, in censo2: Diccionario⟨String,String⟩): Diccionario⟨String,Z⟩ {
    requiere: { Las claves de censo1 son las mismas que las claves de censo2 }
    asegura: { k es clave de res si y sólo si existe alguna clave p en censo1 tal que al obtener su valor tanto en 
              censo1 como en censo2, este es igual a k }
    asegura: { El valor de cada clave de res representa la cantidad de personas que en ambos censos vivía en esa localidad, 
               es decir, que mantuvieron su residencia en la misma localidad entre ambos censos }
}

Ejemplo: mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'})
debe devolver {'Merlo': 1}
"""
def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}
    for persona_censo1 in censo1.keys():
        if censo1[persona_censo1] == censo2[persona_censo1]:
            if censo1[persona_censo1] in res:
                res[censo1[persona_censo1]] += 1
            else:
                res[censo1[persona_censo1]] = 1
    return res

censo1 = {'Juan': 'Merlo', 'Ana': 'Merlo'}
censo2 = {'Juan': 'Castelar', 'Ana': 'Morón'}
print(mantuvieron_residencia(censo1, censo2))

censo3 = {'Juan': 'Merlo', 'Ana': 'Merlo'}
censo4 = {'Juan': 'Merlo', 'Ana': 'Merlo'}
print(mantuvieron_residencia(censo3, censo4))

"""
Ejercicio 5 [0,5 puntos]
Dada la siguiente especificación y una posible implementación de la misma, conteste marcando la opción correcta.

problema sumar_elementos (in s: seq⟨Z⟩): Z {
requiere: { - }
asegura: { res es la suma de los elementos de s }
}

def sumar_elementos(s: list[int]) -> int:
res: int = 0
for i in range(1, len(s)):
    res += s[i]
return res

1) El código es correcto, calcula lo pedido en la especificación para cualquier input
2) El código tiene un bug, y si hacemos un test suite que cubra todas las líneas lo detectaremos
3) El código tiene un bug, pero es posible hacer un test suite que cubra todas las líneas y no detectar dicho bug
"""
#Ejercicio 5: El código tiene un bug, pero es posible hacer un test suite que cubra todas las líneas y no detectar dicho bug.

"""
Ejercicio 6 [0,5 puntos]
Supongamos que un programa tiene un ciclo que itera sobre todos los elementos de una lista de tamaño n. 
Si el programa realiza una operación constante dentro de ese ciclo (por ejemplo, incrementa en 1 cada valor de la lista),
¿cómo afecta el tamaño de la lista al número de operaciones?

1) Si la lista tiene más elementos, el número de operaciones aumentará.
2) El número de operaciones no cambia con el tamaño de la lista.
3) El número de operaciones depende del contenido de la lista, no del tamaño
"""
#Ejercicio 6: Si la lista tiene más elementos, el número de operaciones aumentará.