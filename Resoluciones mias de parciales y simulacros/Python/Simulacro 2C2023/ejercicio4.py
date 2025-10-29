"""
Ejercicio 4:
Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
y sus valores la cantidad de veces que cada uno de esos números aparece en s

problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
  requiere: -
  asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
}
Por ejemplo, dada la lista
 lista = [-1,0,4,100,100,-1,-1]
se debería devolver res={-1:3, 0:1, 4:1, 100:2}
  
RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO
"""
def pertenece(diccionario: dict[int, int], elemento: int) -> bool:
  for clave in diccionario.keys():
    if clave == elemento:
      return True
  return False

def cant_apariciones(lista: list[int], elemento: int) -> int:
  cantidad: int = 0
  for i in range(len(lista)):
    if lista[i] == elemento:
      cantidad+=1
  return cantidad

def convertir_a_diccionario(lista: list[int]) -> dict[int, int]:
  res: dict[int, int] = {}
  for i in range(len(lista)):
    if not pertenece(res, lista[i]):
      res[lista[i]] = cant_apariciones(lista, lista[i])
  return res