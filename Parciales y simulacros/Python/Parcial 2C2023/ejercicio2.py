"""
Ejercicio 2) Mezclar [2 puntos]

A la hora de jugar juegos de cartas, como el truco, el tute, o el chinchón, es importante que la distribución de las mismas
en el mano sea aleatoria. Para esto, al comienzo de cada mano, antes de repartir las mismas se realizan mezclas sucesivas.
Una técnica de mezclado es la denominada "mezcla americana" que consiste en separar el mazo en (aproximadamente) dos mitades
e intercalar las cartas de ambas mitades. Implementar la función mezclar que dadas dos listas s1 y s2 con igual cantidad de 
elementos devuelva una lista con los elementos intercalados. Esto es, las posiciones pares de res tendrán los elementos de s1 
y las posiciones impares los elementos de s2, respetando el orden original.

problema mezclar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: {|s1| = |s2| }
  asegura: {|res| = 2 * |s1|}
  asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
}
TIP: realizar la iteración mediante índices y no mediante elementos

Por ejemplo, dadas
s1 = [1, 3, 0, 1]
s2 = [4, 0, 2, 3]
se debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]
"""
def mezclar(s1: list[int], s2: list[int]) -> list[int]:
  res: list[int] = []
  for i in range(len(s1)):
    res.append(s1[i])
    res.append(s2[i])
  return res