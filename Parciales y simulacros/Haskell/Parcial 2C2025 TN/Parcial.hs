module Parcial where

{-Enunciado
Resolver los siguientes ejercicios cuyas especificaciones en lenguaje semiformal figuran a continuación. Deben ser implementadas en
Haskell utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos 
y Estructuras de Datos I (FCEyN-UBA)
-}

{-Ejercicio 1 (2 puntos)
problema mayorNumeroConNDivisores (d: Z, h: Z, n: Z) : Z {
  requiere: {0 < d ∧ d ≤ h ∧ 0 < n}
  requiere: {Existe al menos un número, en el rango [d, h], con exactamente n divisores positivos}
  asegura: {d ≤ res ∧ res ≤ h}
  asegura: {res tiene exactamente n divisores positivos}
  asegura: {No existe un número con exactamente n divisores positivos en el rango [res + 1, h]}
}
Ejemplo 1: mayorNumeroConNDivisores 2 5 3 debe devolver 4
Ejemplo 2: mayorNumeroConNDivisores 2 5 2 debe devolver 5 
-}
longitud :: (Eq t) => [t] -> Integer 
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista)

listaNumeros :: Integer -> Integer -> [Integer]
listaNumeros desde hasta | desde > hasta = []
                         | otherwise = desde:listaNumeros (desde+1) hasta 

listaDivisoresNumero :: Integer -> Integer -> [Integer]
listaDivisoresNumero desde numero | desde > numero = []
                                  | mod numero desde == 0 = desde:listaDivisoresNumero (desde+1) numero
                                  | otherwise = listaDivisoresNumero (desde+1) numero

cantDivisores :: [Integer] -> Integer
cantDivisores lista | longitud(lista) == 0 = 0
                    | otherwise = 1 + cantDivisores(tail lista)

numeroConNDivPos :: [Integer] -> Integer -> Integer -> Integer
numeroConNDivPos lista numero n | longitud(lista) == 0 = numero
                                | cantDivisores(listaDivisoresNumero 1 (head lista)) == n && (head lista) > numero = numeroConNDivPos (tail lista) (head lista) n
                                | otherwise = numeroConNDivPos (tail lista) numero n

mayorNumeroConNDivisores :: Integer -> Integer -> Integer -> Integer
mayorNumeroConNDivisores d h n = numeroConNDivPos (listaNumeros d h) d n 

{-Ejercicio 2 (2 puntos)
problema sanguchitoDeCerosMasGrande (lista: seq⟨Z⟩) : Z {
  requiere: {|lista| ≥ 3}
  asegura: {Si existe al menos un i en el rango de lista tal que esSanguchitoDeCeros(lista, i) es verdadero, entonces res
            es el mayor valor lista[i] que cumple que esSanguchitoDeCeros(lista, i) es verdadero}
  asegura: {Si no existe ningún i en el rango de lista tal que esSanguchitoDeCeros(lista, i) es verdadero, entonces res = 0}
}

problema esSanguchitoDeCeros (lista: seq⟨Z⟩, i: Z) : Bool {
  asegura: {|lista| ≥ 3 ∧ i > 0 ∧ i < |lista|-1 ∧ lista[i-1] = 0 ∧ lista[i+1] = 0}
}

Ejemplo 1: sanguchitoDeCerosMasGrande [0,5,0,2,0,1] debe devolver 5
Ejemplo 2: sanguchitoDeCerosMasGrande [1,0,3,1,0] debe devolver 0 
-}

indice :: [Integer] -> Integer -> Integer
indice lista elemento | longitud(lista) == 0 = -1
                      | head lista == elemento = 0
                      | otherwise = 1 + indice (tail lista) elemento

extraigoElemento :: [Integer] -> Integer -> Integer
extraigoElemento lista posicion | longitud(lista) == 0 = -1
                                | indice lista (head lista) == posicion = head lista
                                | otherwise = extraigoElemento (tail lista) (posicion-1)

esSanguchitoDeCeros :: [Integer] -> Integer -> Bool
esSanguchitoDeCeros lista posicion = extraigoElemento lista (posicion-1) == 0 && extraigoElemento lista (posicion+1) == 0

listaIndiceElementoNoEsCero :: [Integer] -> Integer -> [Integer]
listaIndiceElementoNoEsCero lista i | longitud(lista) == 0 = []
                                    | (head lista) /= 0 = i:listaIndiceElementoNoEsCero(tail lista) (i+1)
                                    | otherwise = listaIndiceElementoNoEsCero (tail lista) (i+1)

indicesDondeSeCumpleSanguchito :: [Integer] -> [Integer] -> [Integer]
indicesDondeSeCumpleSanguchito listaPos listaElem | longitud(listaPos) == 0 = []
                                                  | not(esSanguchitoDeCeros listaElem (head listaPos)) = indicesDondeSeCumpleSanguchito (tail listaPos) listaElem 
                                                  | otherwise = (head listaPos):indicesDondeSeCumpleSanguchito (tail listaPos) listaElem

elementosDondeSeCumpleSanguchito :: [Integer] -> [Integer] -> [Integer]
elementosDondeSeCumpleSanguchito listaElem [] = []
elementosDondeSeCumpleSanguchito listaElem listaPos = extraigoElemento listaElem (head listaPos):elementosDondeSeCumpleSanguchito listaElem (tail listaPos)

mayorElemento :: [Integer] -> Integer -> Integer
mayorElemento lista maximo | longitud(lista) == 0 = maximo
                           | head(lista) > maximo = mayorElemento (tail lista) (head lista)
                           | otherwise = mayorElemento (tail lista) maximo

sanguchitoDeCerosMasGrande :: [Integer] -> Integer
sanguchitoDeCerosMasGrande lista | listaSinCeros == [] = 0
                                 | otherwise = mayorElemento listaSinCeros (head(listaSinCeros))
                                 where listaSinCeros = (elementosDondeSeCumpleSanguchito lista (indicesDondeSeCumpleSanguchito (listaIndiceElementoNoEsCero (lista) 0) (lista)))

{-Ejercicio 3 (2 puntos)
Una famosa plataforma de streaming nos envía un listado de series de TV con sus respectivas temporadas. Se desea armar una estadística de
la cantidad de temporadas de las series. Para ello nos piden armar una lista que agrupe todas las series que poseen la misma cantidad de 
temporadas.
problema agruparPorCantidadDeTemporadas (lista: seq⟨String x Z⟩) : seq⟨Z x seq⟨String⟩⟩ {
  requiere: {Las primeras componentes de lista tienen longitud mayor estricta a cero}
  requiere: {Las segundas componentes de lista son mayores estrictas a cero}
  requiere: {Las primeras componentes de lista no están repetidas en otras tuplas de la lista}
  asegura: {Las primeras componentes de res son todas distintas}
  asegura: {Si en lista hay una o más series con una cantidad de temporadas t, habrá un elemento e ∈ res tal que e0 = t}
  asegura: {Todos los elementos de res son tuplas donde la primera componente corresponde a la cantidad de temporadas de alguna serie de 
            lista, y la segunda componente son todas las series de lista que tienen esa cantidad de temporadas}
}
Ejemplo 1: agruparPorCantidadDeTemporadas [("Lost",6),("Friends", 10),("Bojack",6)] puede devolver [(6,["Lost","Bojack"]),(10,["Friends"])]  
-}
pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = (head lista) == elemento || pertenece (tail lista) elemento

mismaCantDeTemporadas :: [(String, Integer)] -> Integer -> [String]
mismaCantDeTemporadas lista cantidad | longitud(lista) == 0 = []
                                     | snd(head lista) == cantidad = (fst(head lista)):mismaCantDeTemporadas (tail lista) cantidad
                                     | otherwise = mismaCantDeTemporadas (tail lista) cantidad

agrupoPorTemporada :: [(String, Integer)] -> [(String, Integer)] -> [Integer] -> [(Integer, [String])]
agrupoPorTemporada lista mismaLista listaTemp | longitud(lista) == 0 = []
                                              | not(pertenece listaTemp (snd(head lista))) = (snd(head lista), mismaCantDeTemporadas mismaLista (snd(head lista))):agrupoPorTemporada (tail lista) (mismaLista) ((snd(head lista)):listaTemp)
                                              | otherwise = agrupoPorTemporada (tail lista) mismaLista listaTemp

agruparPorCantidadDeTemporadas :: [(String, Integer)] -> [(Integer, [String])]
agruparPorCantidadDeTemporadas lista = agrupoPorTemporada lista lista [] 

{-Ejercicio 4 (2 puntos)
problema reemplazarMinimoDeCadaFila (mat: seq⟨seq⟨Z⟩⟩, valor: Z) : seq⟨seq⟨Z⟩⟩ {
  requiere: {|mat| > 0}
  requiere: {Todos los elementos de mat tienen la misma longitud (y dicha longitud es estrictamente mayor a 0)}
  asegura: {|res| = |mat| ∧ para todo i tal que 0 ≤ i < |mat| se cumple que |res[i]| = |mat[i]|}
  asegura: {Cada secuencia res[i] es igual a mat[i] en todos sus elementos excepto en el/los mínimo/s, que son reemplazados por valor}
}
Ejemplo 1: reemplazarMinimoDeCadaFila [[3,1],[2,2],[7,0]] 0 debe devolver [[3,0],[0,0],[7,0]]
-}
minimoValor :: [Integer] -> Integer -> Integer
minimoValor fila minimo | longitud(fila) == 0 = minimo
                        | (head fila) < minimo = minimoValor (tail fila) (head fila)
                        | otherwise = minimoValor (tail fila) minimo

reemplazoElMinimo :: [Integer] -> [Integer] -> Integer -> [Integer]
reemplazoElMinimo fila mismaFila valor | longitud(fila) == 0 = []
                                       | (head fila) == minimoValor mismaFila (head mismaFila) = valor:reemplazoElMinimo (tail fila) mismaFila valor
                                       | otherwise = (head fila): reemplazoElMinimo (tail fila) mismaFila valor 

reemplazarMinimoDeCadaFila :: [[Integer]] -> Integer -> [[Integer]]
reemplazarMinimoDeCadaFila matriz valor | longitud(matriz) == 0 = []
                                        | otherwise = (reemplazoElMinimo (head matriz) (head matriz) valor):reemplazarMinimoDeCadaFila (tail matriz) valor

{-Ejercicio 5 (1 punto)
Conteste marcando la opción correcta asumiendo que α y β son dos fórmulas de la lógica proposicional tales que α es más fuerte que β,
y que se tiene las siguientes especificaciones:
problema1 (...) {
  requiere: {True}
  asegura: {α}
}

problema2 (...) {
  requiere: {True}
  asegura: {β}
}
1) El conjunto de soluciones de problema1 está contenido dentro del conjunto de soluciones de problema2.
2) El conjunto de soluciones de problema2 está contenido dentro del conjunto de soluciones de problema1.
3) No es posible afirmar ninguna de las opciones sin conocer en detalle ambas especificaciones. 
-}

--Ejercicio 5: El conjunto de soluciones de problema1 está contenido dentro del conjunto de soluciones de problema2.

{-Ejercicio 6 (1 punto)
Respecto al testing de caja negra, conteste marcando la opción correcta asumiendo que se cuenta con la siguiente especificación:
problema unaFuncionQueHaceAlgo (n: Z) : Z {
  requiere: {Existe algún número entero x tal que x*x = n}
  asegura: {res*res = n}
}
1) n = 10, res = √10 es un caso de test válido.
2) n = 4, res = 2 es un caso de test válido.
3) Para testear el caso n=9, se debe considerar que el resultado podría ser -3 o 3.
-}

--Ejercicio 6: Para testear el caso n=9, se debe considerar que el resultado podría ser -3 o 3.