from queue import LifoQueue as Pila

"""
Ejercicio 1 [2 puntos]

Implementar la función subsecuencias_que_suman:

problema subsecuencias_que_suman (in s: seq⟨Z⟩, in n: Z) : seq⟨seq⟨Z⟩⟩ {
  requiere: { n es positivo}
  requiere: { Todos los elementos de s son positivos }
  asegura: { res contiene exactamente todas las subsecuencias consecutivas de s cuya suma es n }
  asegura: { Las subsecuencias en res aparecen en el mismo orden en que ocurren en s }
}

  Ejemplo: subsecuencias_que_suman([1,3,2,1,5,4,8], 5) debe devolver [[3,2], [5]]
      
"""
def subsecuencias_que_suman(s: list[int], n: int) -> list[list[int]]:
    res: list[list[int]] = []
    subsecuencia_actual: list[int] = []
    suma_actual: int = 0
    guardo_indice: int = 0

    for i in range(len(s)):
        subsecuencia_actual.append(s[i])
        suma_actual+= s[i]

        if suma_actual >= n:
            if suma_actual == n:
                res.append(subsecuencia_actual)
                subsecuencia_actual = [] 
                suma_actual = 0
                i = guardo_indice+1
            else:
                subsecuencia_actual = []
                suma_actual = 0
                i = guardo_indice+1
    return res
"""
Ejercicio 2 [2 puntos]

Implementar la función buscar_cliente_prioritario:

problema buscar_cliente_prioritario (inout clientes: Pila⟨String x String x Z⟩) : String {
  requiere: { Existe al menos un elemento (nombre, medio, cant) en clientes tal que medio = "bitcoin" ∧ cant > 100 }
  modifica: { clientes }
  asegura: { res es el nombre del elemento más antiguo (en el orden de clientes@pre) que cumple medio = "bitcoin" ∧ cant > 100 }
  asegura: { clientes contiene exactamente los elementos de clientes@pre excepto ese último elemento seleccionado, preservando el orden relativo }
}

  Ejemplo: Si clientes es la siguiente pila (el elemento ("Ana","bitcoin",3) es el tope de la pila):

  ("Ana","bitcoin",3)
  ("Beto","debito",150)
  ("Caro","bitcoin",120)

  entonces 

  res = "Caro" y clientes es:
  
  ("Ana","bitcoin",3)
  ("Beto","debito",150)        
"""

def buscar_cliente_prioritario (clientes: Pila[tuple[str, str, int]]) -> str:
    res: str = ""
    pila_auxiliar: Pila[tuple[str, str, int]] = Pila()

    #invierto la pila
    while not clientes.empty():
        elemento: tuple[str, str, int] = clientes.get()
        pila_auxiliar.put(elemento)    

    while not pila_auxiliar.empty():
        otro_elemento: tuple[str, str, int] = pila_auxiliar.get()
        if (otro_elemento[1] == "bitcoin" and otro_elemento[2] > 100) and res == "":
            res = otro_elemento[0]
        else:
            clientes.put(otro_elemento)
    return res

"""
Ejercicio 3 [2 puntos]

Implementar la función eliminar_fila_que_mas_suma:

problema eliminar_fila_que_mas_suma (in A: seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
  requiere: { |A| > 0}
  requiere: { Todos los elementos de A tienen la misma longitud, y la misma es mayor a 0}
  asegura: { res contiene todas las filas de A (con los mismos elementos y en el mismo orden) excepto aquellas cuya suma es la máxima entre las filas de A }
}

  Ejemplo: eliminar_fila_que_mas_suma ([[1,-2,3],[8,8,8],[4,5,6],[7,8,9]]) 

  debe devolver [[1,-2,3],[4,5,6]]
      
"""
def suma_filas(fila: list[int]) -> int:
    res: int = 0
    for i in range(len(fila)):
        res+=fila[i]
    return res

def lista_sumas_filas(mat: list[list[int]]) -> list[int]:
    res: list[int] = []
    for i in range(len(mat)):
        suma: int = suma_filas(mat[i])
        res.append(suma)
    return res

def maximo(lista: list[int]) -> int:
    numero_mas_grande: int = 0
    numero_actual: int = 0
    for i in range(len(lista)):
        numero_actual: int = lista[i]
        if numero_actual > numero_mas_grande:
            numero_mas_grande = numero_actual
    return numero_mas_grande

def eliminar_fila_que_mas_suma(A: list[list[int]]) -> list[list[int]]:    
    res: list[list[int]] = []
    for i in range(len(A)):
        suma_actual: int = suma_filas(A[i])
        if suma_actual < maximo(lista_sumas_filas(A)):
            res.append(A[i])               
    return res

"""
Ejercicio 4 [2 puntos]
Una plataforma de streaming quiere saber cuáles son las películas favoritas. Contamos con un diccionario donde la clave representa a un cliente y el 
valor es el nombre de su película favorita. 
A dicha plataforma le interesa conocer aquellas películas favoritas que fueron vistas por más de un cierto número de clientes.

Implementar la función peliculas_mas_vistas:

problema peliculas_mas_vistas (in favoritas_por_cliente: dict⟨String, String⟩, in n: Z) : dict⟨String, Z⟩ {
  requiere: { favoritas_por_cliente tiene al menos una película que fue elegida como favorita por al menos n clientes}
  requiere: { n > 0 }
  asegura: { Una película P está en res si y solo si al menos n clientes la eligieron como favorita.}
  asegura: { Para cada clave c de res, res[c] es la cantidad de clientes que tienen como favorita la película c.}
}

  Ejemplo: peliculas_mas_vistas({"Beto":"Endgame","Ana":"Avatar","Caro":"Endgame","Diego":"Endgame"}, 3) devuelve {"Endgame":3}
      
"""
def pertenece(lista: list[str], elemento: str) -> bool:
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

def cuantas_veces_vieron_la_pelicula(peli: str, peliculas: list[str]) -> int:
    cantidad: int = 0
    for i in range(len(peliculas)):
        if peliculas[i] == peli:
            cantidad+=1
    return cantidad

def lista_pelis(diccionario: dict[str, str]) -> list[str]:
    res: list[str] = []
    for pelicula in diccionario.values():
        res.append(pelicula)
    return res

def peliculas_mas_vistas(favoritas_por_cliente: dict[str, str], n: int) -> dict[str, int]:
    res: dict[str, int] = {}
    lista_peliculas: list[str] = []
    for pelicula in favoritas_por_cliente.values():
        if not pertenece(lista_peliculas, pelicula) and cuantas_veces_vieron_la_pelicula(pelicula, lista_pelis(favoritas_por_cliente)) >= n:
            res[pelicula] = cuantas_veces_vieron_la_pelicula(pelicula, lista_pelis(favoritas_por_cliente))
    return res