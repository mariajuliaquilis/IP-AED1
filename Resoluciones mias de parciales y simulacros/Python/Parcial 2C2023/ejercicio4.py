"""
Ejercicio 4) Matriz capicúa [3 puntos]
Implementar la función matriz_capicua que dada una matriz devuelve True si cada una de sus filas es capicúa. Es decir,
si cada fila es igual leída de izquierda a derecha o de derecha a izquierda. Definimos a una secuencia de secuencias como 
matriz si todos los elemento de la primera secuencia tienen la misma longitud.

problema matriz_capicua(in m:seq⟨seq⟨Z⟩⟩ ) : Bool {
  requiere: {todos los elementos de m tienen igual longitud (los elementos de m son secuencias)}
  asegura: {(res = true) <=> todos los elementos de m son capicúa}
}

Por ejemplo, dada la matriz m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]] se debería devolver res = true
"""
def lista_capicua(lista: list[int]) -> bool:
  res: bool = True
  for i in range(len(lista)):
    primerElemento: int = lista[i]
    ultimoElemento: int = lista[len(lista)-1-i]
    if i <= len(lista)-1-i:
      if primerElemento != ultimoElemento:
        return False
  return res
        
def matriz_capicua(m: list[list[int]]) -> bool:
  res: bool = True
  for i in range(len(m)):
    if not lista_capicua(m[i]):
      return False
  return res