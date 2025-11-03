from queue import Queue as Cola

"""
Ejercicio 1) Juego del gallina (3 puntos)

El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario; 
si alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un "gallina". 
Se hizo un torneo para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. 
Si dos jugadores juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado. 
Si ambos jugadores se desvían, pierde cada uno 10 puntos por gallinas. 
Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos! 
En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se desvía, o nunca lo hace. 
Se debe programar la función 'torneo_de_gallinas' que recibe un diccionario (donde las claves representan los nombres de los 
participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y devuelve un diccionario con los puntajes 
obtendidos por cada jugador.

problema torneo_de_gallinas (in estrategias: dict⟨String,String⟩) : dict⟨String,Z⟩ {
  requiere: {estrategias tiene por lo menos 2 elementos (jugadores)}
  requiere: {Las claves de estrategias tienen longitud mayor a 0}
  requiere: {Los valores de estrategias sólo pueden ser los strings "me desvio siempre" ó "me la banco y no me desvio"}
  asegura: {Las claves de res y las claves de estrategias son iguales}
  asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al finalizar 
            el torneo, dado que jugó una vez contra cada otro jugador}
}
"""

def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}
    return res


"""
Ejercicio 2) Cola en el Banco (1 puntos)

En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por las
tuplas (nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser "comun" o "vip".
Se nos pide implementar una función en python que dada una cola de clientes del banco, devuelva una nueva cola con los mismos 
clientes pero en donde los clientes vip estan primero que los clientes comunes manteniendo el orden original de los clientes vips 
y los comunes entre sí.

problema reordenar_cola_priorizando_vips (in filaClientes: Cola⟨String x String⟩) : Cola⟨String⟩ {
  requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0}
  requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son "comun" o "vip" }
  requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí }
  asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes}
  asegura: {|res| = |filaCliente|}
  asegura: {res no tiene elementos repetidos}
  asegura: {No hay ningun cliente "comun" antes que un "vip" en res}
  asegura: {Para todo cliente c1 y cliente c2 de tipo "comun" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes 
            entonces el nombre de c1 aparece antes que el nombre de c2 en res}
  asegura: {Para todo cliente c1 y cliente c2 de tipo "vip" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes
            entonces el nombre de c1 aparece antes que el nombre de c2 en res}
}
"""
def copia_cola(cola: Cola[tuple[str, str]]) -> Cola[tuple[str, str]]:
  cola_auxiliar: Cola[tuple[str, str]] = Cola()
  cola_copiada: Cola[tuple[str, str]] = Cola()
  #Invertimos la cola pasada como parámetro
  while not cola.empty():
    elemento: tuple[str, str] = cola.get()
    cola_auxiliar.put(elemento)
  #Restauro la cola original
  while not cola_auxiliar.empty():
     otro_elemento: tuple[str, str] = cola_auxiliar.get()
     cola.put(otro_elemento)
     cola_copiada.put(otro_elemento)
  return cola_copiada

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str, str]]) -> Cola[str]:
  copia_filaClientes: Cola[tuple[str, str]] = copia_cola(filaClientes)
  afiliados_de_tipo_comun: Cola[str] = Cola()
  afiliados_de_tipo_vip: Cola[str] = Cola()
  res: Cola[str] = Cola()

  while not copia_filaClientes.empty():
    elemento: tuple[str, str] = copia_filaClientes.get()
    if elemento[1] == "comun":
      afiliados_de_tipo_comun.put(elemento[0])
    else:
      afiliados_de_tipo_vip.put(elemento[0])

  while not afiliados_de_tipo_vip.empty():
    cliente_vip: str = afiliados_de_tipo_vip.get()
    res.put(cliente_vip)
  while not afiliados_de_tipo_comun.empty():
    cliente_comun: str = afiliados_de_tipo_comun.get()
    res.put(cliente_comun)   
    
  return res

"""
Ejercicio 3) Sufijos que son palíndromos (2 puntos)

Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. 
Se nos pide programar en python la siguiente función:

problema cuantos_sufijos_son_palindromos(in texto:String) : Z {
  requiere: -
  asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
}
Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el final de la palabra. 
Ej: "Diego", el conjunto de sufijos es: "Diego", "iego","ego","go", "o". 
Para este ejercicio no consideraremos a "" como sufijo de ningun texto.
"""
def es_palindromo(texto: str) -> bool:
  for i in range(0, len(texto)):
    if i <= len(texto)-i-1:
      if texto[i] != texto[len(texto)-i-1]:
        return False
  return True

def cant_palindromos(subsecuencias: list[str]) -> int:
  cantidad: int = 0
  for i in range(len(subsecuencias)):
    if es_palindromo(subsecuencias[i]):
      cantidad+=1
  return cantidad

def cuantos_sufijos_son_palindromos(texto: str) -> int:
  sufijos: list[str] = []
  for i in range(len(texto)):
    sufijo: str = ""
    for j in range(i, len(texto)):
      sufijo = sufijo+texto[j]
    sufijos.append(sufijo)
  return cant_palindromos(sufijos)

"""
Ejercicio 4) Ta-Te-Ti-Facilito (2 puntos)

Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su ficha en cada turno.
Juegan intercaladamente y comienza Ana. Ana pone siempre una 'X' en su turno y Beto pone una 'O' en el suyo. 
Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero está completo y no ganó nadie, 
entonces se declara un empate. El tablero comienza vacío, representado por ' ' en cada posición.
Notar que dado que juegan por turnos y comienza Ana poniendo una 'X' se cumple que la cantidad de 'X' es igual a la cantidad de 'O' o bien
la cantidad de 'X' son uno más que la cantidad de 'O'.
Se nos pide implementar una función en python 'problema quien_gano_el_tateti_facilito' que determine si ganó alguno, o si Beto hizo trampa 
(puso una 'O' cuando Ana ya había ganado).

problema quien_gano_el_tateti_facilito(in tablero:seq⟨seq⟨Char⟩) : Z {
  requiere: {tablero es una matriz cuadrada}
  requiere: {5<=|tablero[0]|<= 10}
  requiere: {tablero sólo tiene 'X', 'O' y ' ' (espacio vacío) como elementos}
  requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'}
  asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical(misma columna) y no hay tres 'O' consecutivas en forma 
            vertical (misma columna) }
  asegura: {res = 2 <==> hay tres 'O' consecutivas en forma vertical (misma columna) y no hay tres 'X' consecutivas en forma 
            vertical (misma columna) }
  asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
  asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
}
"""
def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
  for i in range(len(tablero[0])):
    contador_X: int = 0
    contador_O: int = 0
    for j in range(len(tablero)):
      if tablero[j][i] == "X":
        contador_X+=1
      elif tablero[j][i] == "O":
        contador_O+=1
      if contador_X == 3 and contador_O == 3:
        return 3
      elif contador_X == 3:
        return 1
      elif contador_O == 3:
        return 2
  return 0


"""
Ejercicio 5) Preguntas teóricas (2 puntos)
Conteste marcando la opción correcta.

A) ¿Qué es una variable en Python? (0.75 punto)

1) Una función que devuelve valores aleatorios.
2) Un contenedor para almacenar datos que puede cambiar durante la ejecución del programa.
3) Un tipo de dato que solo puede contener números enteros.

B) ¿Cuál es la función de un ciclo en Python? (0.75 punto)

1) Ejecutar un conjunto de instrucciones una sola vez.
2) Ejecutar repetidamente un conjunto de instrucciones hasta que una condición se evalúe como falsa.
3) Definir una constante que no puede ser cambiada.

C) ¿Cuál es la finalidad de un Control Flow Graph en testing? (0.5 punto)

1) Identificar todas las posibles salidas de un programa.
2) Visualizar todos los posibles caminos de ejecución para asegurar la cobertura completa del código.
3) Determinar los puntos de entrada y salida del programa.
"""

#Ejercicio 5 A) Un contenedor para almacenar datos que puede cambiar durante la ejecución del programa.
#Ejercicio 5 B) Ejecutar repetidamente un conjunto de instrucciones hasta que una condición se evalúe como falsa.
#Ejercicio 5 C) Visualizar todos los posibles caminos de ejecución para asegurar la cobertura completa del código.