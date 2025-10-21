from typing import List, Tuple, Dict

#Ejercicio 2
"""
2) Seguidilla [2 puntos]

Implementar la función seguidilla() que dada una secuencia de enteros calificaciones, y un entero nota_minima,
devuelva la cantidad de elementos de la subsecuencia más larga que cumplen que son mayores o iguales a la nota_minima.
En caso de que esta seguidilla no exista, devolver 0.

problema seguidilla (in calificaciones: seq⟨Z⟩, in nota_minima: Z): Z {
  requiere: {todos los elementos de calificaciones son mayores o iguales a 0 y menores o iguales a 100}
  requiere: {nota_minima es mayor o igual a 0 y menor o igual a 100}
  asegura: {res = |subsec| si solo si existe una subsecuencia de calificaciones (subsec), y todos los elementos de subsec son mayores o iguales a la nota_minima}
  asegura: {No existe otra subsecuencia de calificaciones que tenga longitud mayor a res}
  asegura: {res = 0 si y solo si no hay ningún elemento de calificaciones que sea mayor a nota_minima}
}

Ejemplo 1: dada los siguientes inputs:

calificaciones = [10,55,60,87,54,98,87,65,55,45,57]; nota_minima = 60
se debería devolver res = 3, que es la longitud de la subsecuencia [98,87,65]

Ejemplo 2: dada los siguientes inputs:

calificaciones = [10,55,60,65,54,64,65,55,45,57]; nota_minima = 70
se debería devolver res = 0, ya que no hay ninguna subsecuencia de calificaciones con elementos mayores o iguales a nota_minima 
"""


def seguidilla (calificaciones: List[int], nota_minima: int)-> int:
    return 0.0
