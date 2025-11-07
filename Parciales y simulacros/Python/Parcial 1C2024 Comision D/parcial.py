"""
Ejercicio 1) Análisis de Stock [2 puntos]

En la veterinaria "Exactas's pets", al finalizar cada día, el personal registra en papeles los nombres y la cantidad actual de los 
productos cuyo stock ha cambiado. Para mejorar la gestión, desde la dirección de la veterinaria han pedido desarrollar una solución 
en Python que les permita analizar las fluctuaciones del stock.

Se pide implementar una función, que reciba una lista de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento.
La función debe procesar esta lista y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su mínimo
y máximo stock histórico registrado.

problema stock_productos (in stock_cambios: seq⟨(String x Z)) : dict⟨String, (Z x Z)⟩ {
  requiere:{Todos los elementos de stock_cambios están formados por un String no vacío y un entero ≥ 0}
  asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un producto)}
  asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock_cambios}
  asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese 
            producto en stock_cambios y como segundo valor el mayor}
}
"""
def minimo_stock(producto: str, stock_cambios: list[tuple[str, int]]) -> int:
  lista_stock: list[int] = []
  for i in range(len(stock_cambios)):
    if producto == stock_cambios[i][0]:
      lista_stock.append(stock_cambios[i][1])
  minimo: int = lista_stock[0]
  for j in range(len(lista_stock)):
    if lista_stock[j] < minimo:
      minimo = lista_stock[j]
  return minimo

def maximo_stock(producto: str, stock_cambios: list[tuple[str, int]]) -> int:
  lista_stock: list[int] = []
  for i in range(len(stock_cambios)):
    if producto == stock_cambios[i][0]:
      lista_stock.append(stock_cambios[i][1])
  maximo: int = lista_stock[0]
  for j in range(len(lista_stock)):
    if lista_stock[j] > maximo:
      maximo = lista_stock[j]
  return maximo  

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
  res: dict[str, tuple[int, int]] = {}
  for i in range(len(stock_cambios)):
    stock: str = stock_cambios[i][0]
    minimoStock = minimo_stock(stock, stock_cambios)
    maximoStock = maximo_stock(stock, stock_cambios)    
    tupla: tuple[int, int] = (minimoStock, maximoStock)
    res[stock] = tupla  
  return res

"""
Ejercicio 2) Filtrar códigos de barra [2 puntos]

El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos códigos de barras terminan 
en números primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre de esta idea, 
solicita una función en Python que facilite esta gestión.

Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código de barras de un producto, 
cree y devuelva una nueva lista que contenga únicamente aquellos números de la lista original cuyos últimos tres dígitos formen 
un número primo (por ejemplo, 101, 002 y 011).
Nota: Un número primo es aquel que solo es divisible por sí mismo y por 1. Algunos ejemplos de números primos de hasta tres dígitos 
son: 2, 3, 5, 101, 103, 107, etc.

problema filtrar_codigos_primos (in codigos_barra: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere:{Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos}
  requiere:{No hay elementos repetidos en codigos_barra}
  asegura: {los últimos 3 dígitos de cada uno de los elementos de res forman un número primo}
  asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo están en res}
  asegura: {Todos los elementos de res están en codigos_barra }
}
"""
def lista_numeros(numero: int) -> list[int]:
  lista: list[int] = []
  indice = 1
  while indice <= numero:
    lista.append(indice)
    indice+=1
  return lista

def divisores_numero(numero: int) -> list[int]:
  lista: list[int] = lista_numeros(numero)
  res: list[int] = []
  for i in range(len(lista)):
    if numero % lista[i] == 0:
      res.append(lista[i])
  return res

def es_primo(numero: int) -> bool:
  return divisores_numero(numero) == [1, numero]

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
  lista_primos: list[int] = []
  for i in range(len(codigos_barra)):
    if es_primo(codigos_barra[i] % 1000):
      lista_primos.append(codigos_barra[i])
  return lista_primos

"""
Ejercicio 3) Flujo de pacientes [2 puntos]

Con el objetivo de organizar el flujo de pacientes, en la veterinaria se anotan los tipos de mascotas que van ingresando al local.
Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una función en Python que 
encuentre la secuencia más larga de consultas consecutivas que solo contenga los tipos de mascota "perro" o "gato".

Se pide implementar una función que, dada una secuencia de Strings, que representan los tipos de animales atendidos, devuelva el índice
donde comienza la subsecuencia más larga que cumpla con estas condiciones.

problema subsecuencia_mas_larga(in tipos_pacientes_atendidos: seq⟨String⟩) : Z{
  requiere: {tipos_pacientes_atendidos tiene, por lo menos, un elemento "perro" o "gato"}
  asegura: {res es el índice donde empieza la subsecuencia más larga de tipos_pacientes_atendidos que contenga solo elementos "perro" o "gato"}
  asegura: {Si hay más de una subsecuencia de tamaño máximo, res tiene el índice de la primera)}
}
"""
def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
  cant_elementos_subsecuencia_actual: int = 0
  cant_elementos_subsecuencia_mas_grande: int = 0
  indice_subsecuencia_mas_grande: int = 0
  indice_subsecuencia_actual: int = -1 #esto es válido en el parcial?

  for i in range(len(tipos_pacientes_atendidos)):
    if tipos_pacientes_atendidos[i] == "perro" or tipos_pacientes_atendidos[i] == "gato":
      cant_elementos_subsecuencia_actual+=1
      if indice_subsecuencia_actual == -1:
        indice_subsecuencia_actual = i
    else:
      if cant_elementos_subsecuencia_actual > cant_elementos_subsecuencia_mas_grande:
        cant_elementos_subsecuencia_mas_grande = cant_elementos_subsecuencia_actual
        cant_elementos_subsecuencia_actual = 0
        indice_subsecuencia_mas_grande = indice_subsecuencia_actual
        indice_subsecuencia_actual = -1
      else:
        cant_elementos_subsecuencia_actual = 0
        indice_subsecuencia_actual = -1


  if cant_elementos_subsecuencia_actual > cant_elementos_subsecuencia_mas_grande:
      cant_elementos_subsecuencia_mas_grande = cant_elementos_subsecuencia_actual
      indice_subsecuencia_mas_grande = indice_subsecuencia_actual

  return indice_subsecuencia_mas_grande

"""
Ejercicio 4) Tabla turnos [2 puntos]

Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los días, en orden de lunes a domingo,
y cada fila a un rango de una hora. Hay cuatro filas para los turnos de la mañana (9, 10, 11 y 12 hs) y otras cuatro para la tarde 
(14, 15, 16 y 17).

Para hacer más eficiente el trabajo del personal de la veterinaria, se necesita analizar si quienes quedan de responsables, están asignadas
de manera continuada en los turnos de cada día.

Para ello se pide desarrollar una función en Python que, dada la matriz de turnos, devuelva una lista de tuplas de Bool, una por cada día. 
Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los turnos de la mañana para ese
día son iguales entre sí. El segundo elemento debe ser True si y solo si todos los valores de los turnos de la tarde para ese día son iguales
entre sí. Siempre hay una persona responsable en cualquier horario de la veterinaria.

problema un_responsable_por_turno (in grilla_horaria: seq⟨seq⟨String⟩⟩: seq⟨(Bool x Bool)⟩ {
  requiere: {|grilla_horaria| = 8}
  requiere: {Todos los elementos de grilla_horaria tienen el mismo tamaño (mayor a 0 y menor 8)}
  requiere: {No hay cadenas vacías en las listas de grilla_horaria}
  asegura: {|res| = |grilla_horaria[0]|}
  asegura: {El primer valor de la tupla en res [i], con i:Z, 0 <= i < |res| es igual a True <=> los primeros 4 valores de la columna i de
            grilla_horaria son iguales entre sí}
  asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 <= i < |res| es igual a True <=> los últimos 4 valores de la columna i de 
            grilla_horaria son iguales entre sí}
}
"""
def valores_iguales(lista_turnos: list[str]) -> bool:
  elemento: str = lista_turnos[0]
  for i in range(len(lista_turnos)):
    if lista_turnos[i] != elemento:
      return False
  return True

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool, bool]]:
  res: list[tuple[bool, bool]] = []
  for j in range(len(grilla_horaria[0])):
    lista_dia_turno_mañana: list[str] = []
    lista_dia_turno_tarde: list[str] = []
    for i in range(len(grilla_horaria)):
      if 0 <= i and i <= 3:
        lista_dia_turno_mañana.append(grilla_horaria[i][j])
      else:
        lista_dia_turno_tarde.append(grilla_horaria[i][j])
    res.append((valores_iguales(lista_dia_turno_mañana), valores_iguales(lista_dia_turno_tarde)))
    #res.append(tupla)
  return res

"""
Ejercicio 5) Preguntas teóricas (2 puntos)
Conteste marcando la opción correcta.

A) ¿Qué se entiende por 'estado' en un programa? (0.75 punto)

1) La apariencia visual del código fuente.
2) La configuración de todas las variables en un punto específico durante la ejecución de un programa.
3) El nombre del archivo donde se guarda el código fuente.


B) ¿Cuál es la diferencia entre una variable de 'scope global' y una variable de 'scope local'? (0.75 punto)

1) No hay ninguna diferencia, ambos términos significan lo mismo.
2) Las variables globales son accesibles desde cualquier parte del programa, mientras que las variables locales solo 
   son accesibles dentro del bloque donde fueron definidas.
3) Las variables locales son accesibles desde cualquier parte del programa, mientras que las variables globales solo 
   son accesibles dentro del bloque donde fueron definidas.


C) ¿Qué es un Control Flow Graph (CFG)? (0.5 punto)

1) Un diagrama que representa la estructura jerárquica del código.
2) Un diagrama que muestra los diferentes caminos que puede tomar la ejecución del programa a través de sus instrucciones y decisiones.
3) Un gráfico que representa el rendimiento del software en diferentes entornos.
"""

#Ejercicio 5 A) La configuración de todas las variables en un punto específico durante la ejecución de un programa.
#Ejercicio 5 B) Las variables globales son accesibles desde cualquier parte del programa, mientras que las variables 
#               locales solo son accesibles dentro del bloque donde fueron definidas.
#Ejercicio 5 C) Un diagrama que muestra los diferentes caminos que puede tomar la ejecución del programa a través de 
#               sus instrucciones y decisiones.