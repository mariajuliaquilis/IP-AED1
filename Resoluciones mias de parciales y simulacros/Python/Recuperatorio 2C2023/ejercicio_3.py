from typing import List, Tuple, Dict

# Ejercicio 3
"""
3) Posiciones pares [3 puntos]

Implementar la función elem_en_pos_pares() que dada una lista de listas matriz y un elemento elem 
devuelva una lista de bool de igual longitud de matriz, que indique en cada posición si elem se encuentra 
en alguna posición par de la sublista de matriz que ocupa esa posición.

problema elem_en_pos_pares(in matriz:seq⟨seq⟨Z⟩⟩, in elem:Z ) : seq⟨Bool⟩ {
  asegura: {(|res| = |matriz|) }
  asegura: {Cada i-ésima posición de res indica si elem pertenece a la lista matriz[i] en una posición par}
}

Por ejemplo, dados:
elem= 1; M = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 1, 0, 0, 6, 0, 0, 1, 0],
]
se debería devolver res = [true, true, true,false,false] 
"""
#Consultar: debo asumir que me pueden pasar cualquier entrada ya que la especificación no tiene un requiere?
#Pensé el ejercicio asumiendo que el usuario me debe pasar n elem, siendo n la longitud de la matriz
def elem_en_pos_pares(matriz: List[List[int]], elem: int) -> List[bool]:
    res: List[bool] = []
    for i in range(len(matriz)):        #Accedo a las filas
        for j in range(len(matriz[i])): #Accedo a los elementos
            if matriz[i][j] == elem:
              if j % 2 == 0:
                  res.append(True)
              else:
                  res.append(False)
    return res