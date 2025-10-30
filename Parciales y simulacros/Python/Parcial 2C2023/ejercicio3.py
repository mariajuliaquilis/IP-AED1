"""
Ejercicio 3) A los pingos: resultado carreras [3 puntos]
Además de recitales de artistas de renombre internacional (ej: Bizarrap), en el hipódromo de Palermo se realizan cotidianamente 
carreras de caballos. 
Por ejemplo, durante el mes de Octubre se corrieron 10 carreras. En cada una de ellas participaron alrededor de 10 caballos.
Implementar la función frecuencia_posiciones_por_caballo que dada la lista de caballos que corrieron las carreras, 
y el diccionario que tiene los resultados del hipódromo en el formato carreras:posiciones_caballos, donde carreras es un String 
y posiciones_caballos es una lista de strings con los nombres de los caballos, genere un diccionario de caballos:#posiciones, 
que para cada caballo devuelva la lista de cuántas veces salió en esa posición.

Tip: para crear una lista con tantos ceros como caballos se puede utilizar la siguiente 
sintaxis lista_ceros = [0]*len(caballos)

problema frecuencia_posiciones_por_caballo(in caballos: seq⟨String⟩, in carreras: 
dict⟨String,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
  requiere: {caballos no tiene repetidos}
  requiere: {Los valores del diccionario carreras son permutaciones de la lista 
  caballos (es decir, tienen exactamente los mismos elementos que caballos, en 
  cualquier orden posible)}
  asegura: {res tiene como claves los elementos de caballos}
  asegura: {El valor en res de un caballo es una lista que indica en la posición i 
  cuántas veces salió ese caballo en la i-ésima posición.}
}
Por ejemplo, dados
caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
                  "carrera2":["petisa", "mister", "linda", "luck"]}
se debería devolver res = {"petisa": [1,1,0,0],
                                          "mister": [0,1,1,0],
                                          "linda": [1,0,1,0],
                                          "luck": [0,0,0,2]}
"""
def posiciones_por_caballo_en_tal_carrera(caballo: str, posiciones: list[str]) -> int:
  posicion: int = 0
  for i in range(len(posiciones)):
    if posiciones[i] == caballo:
      return i 
  return posicion

def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str, list[str]]) -> dict[str, list[int]]:
  res: dict[str, list[int]] = {}
  for caballo in caballos:
    lista_caballo: list[int] = [0]*len(caballos) #Crea una lista con tantos ceros como caballos para cada caballo
    for posiciones in carreras.values(): 
      lista_caballo[posiciones_por_caballo_en_tal_carrera(caballo, posiciones)]+=1
    res[caballo] = lista_caballo
  return res


  