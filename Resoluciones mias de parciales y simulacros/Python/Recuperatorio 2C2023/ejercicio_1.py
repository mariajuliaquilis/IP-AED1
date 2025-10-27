from typing import List, Tuple, Dict

# Ejercicio 1
"""
1) Caminen, chiques, caminen! [2 puntos]
Lita de Lazari fue una conocida ama de casa de la década de los 80's y 90's.
Fue, durante muchos años, la presidenta de la Liga de Amas de Casa.
Su fama se debía, principalmente, a que salía por televisión dando consejos a las amas de casa.
Entre sus frases más famosas está la ya clásica "caminen chicas" (parafraseada y actualizada a los tiempos modernos en el título 
de este ejercicio).
Esta frase representaba la idea de que, dada la situación económica del país en aquella época (no muy diferente a la actual) la mejor 
forma de ahorrar era recorrer diferentes comercios en busca de los mejores precios.

Implementar la función mejores_precios() que dadas dos listas super1 y super2, de igual longitud, donde cada i-ésimo elemento de 
ambas listas representa el precio de un mismo producto en dos supermercados, devuelva una lista de igual longitud con el menor 
precio de cada producto. 


 problema mejores_precios (in super1: seq⟨String x R⟩, in super2: seq⟨String x R⟩): seq⟨String x R ⟩ {
  requiere: {|super1| = |super2|}
  requiere: {Todos los elementos en las segundas posiciones de las tuplas de super1 y de super2 son positivos}
  requiere: {Todos los elementos en las primeras posiciones de las tuplas de super1 y de super2 son iguales}
  asegura: {|res| = |super1| }
  asegura: {Cada posición de |res| contiene una tupla con el nombre del producto correspondiente al de esa posición en super1 
  y el mínimo valor entre los elementos que se encuentran en esa posición en super1 y super2}
}

Por ejemplo, dado
super1 = [("leche", 151.0), ("yerba", 4719.5), ("jabón", 269.2)]
super2 = [("leche", 261.2), ("yerba", 3939.1), ("jabón", 319.2)]
se debería devolver res = [("leche", 151.0), ("yerba", 3939.1), ("jabón", 269.2)] 
"""
def mejores_precios(super1: List[Tuple[str, float]], super2: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
  res: List[Tuple[str, float]] = []
  #No chequeo qué pasa si las longitudes de las listas son distintas pues el usuario no estaría cumpliendo el contrato
  for i in range(len(super1)):
    elementoSuper1: Tuple[str, float] = super1[i] #Accedo a los elementos de la lista de super1
    elementoSuper2: Tuple[str, float] = super2[i] #Puedo hacer esto porque super1 y super2 tienen las mismas longitudes
    if elementoSuper1[1] < elementoSuper2[1]:     #Comparo los precios
      res.append(elementoSuper1)
    else:
      res.append(elementoSuper2)        
  return res