module Parcial where
{- Ejercicio 1 (2,5 puntos)
Se dice que n es un número abundante si la suma de sus divisores propios es mayor que n. Los divisores propios de un número son todos los 
divisores sin contar al número mismo. Por ejemplo, los divisores propios de 12 son 1, 2, 3, 4 y 6. La suma de los divisores propios de 12 
es 1 + 2 + 3 + 4 + 6 = 16, que es mayor que 12. Por lo tanto, 12 es un número abundante.
Se pide implementar cantidadNumerosAbundantes:
problema cantidadNumerosAbundantes (d: Z,h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números abundantes en el rango [d..h]}
}  Ejemplo: cantidadNumerosAbundantes 12 24 debe devolver 4  
-}

longitud :: (Eq t) => [t] -> Integer
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista)

divisoresHastaN :: Integer -> Integer -> [Integer]
divisoresHastaN d n | d == n = []
                    | mod n d == 0 = [d]++divisoresHastaN (d+1) n
                    | otherwise = divisoresHastaN (d+1) n

divisoresPropios :: Integer -> [Integer]
divisoresPropios n = divisoresHastaN 1 n

sumaDivisoresPropios :: [Integer] -> Integer
sumaDivisoresPropios lista | longitud(lista) == 0 = 0
                           | otherwise = head(lista) + sumaDivisoresPropios(tail lista)

esNumeroAbundante :: Integer -> Bool
esNumeroAbundante n = sumaDivisoresPropios(divisoresPropios n) > n

cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes d h | d > h = 0
                              | esNumeroAbundante d = 1 + cantidadNumerosAbundantes (d+1) h 
                              | otherwise = cantidadNumerosAbundantes (d+1) h  

{- Ejercicio 2 (2 puntos)
Representaremos una cursada aprobada con una tupla String x Z x Z, donde:
La primera componente de la tupla contiene el nombre de una materia
La segunda componente de la tupla contiene el año de aprobación de la cursada
La tercera componente de la tupla contiene el cuatrimestre de aprobación de la cursada (el valor 0 representa un curso de verano)
Se pide implementar cursadasVencidas, que dada una lista de cursadas devuelva aquellas materias cuya aprobación de la cursada ya venció, 
y por lo tanto ya no se puede rendir el final

problema cursadasVencidas (s: seq⟨String x Z x Z⟩) :seq⟨String⟩ {
  requiere: { s[i]1 ≥ 1993 para todo i tal que 0 ≤ i < |s|}
  requiere: { 0 ≤ s[i]2 ≤ 2 para todo i tal que 0 ≤ i < |s|}
  asegura: { res no tiene elementos repetidos}
  asegura: { res contiene los nombres de todas las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer
            cuatrimestre de 2021, inclusive}
  asegura: { res contiene solamente los nombres de las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer 
             cuatrimestre de 2021, inclusive}
}
Ejemplo: cursadasVencidas [("Algoritmos y Estructuras de Datos I", 2020, 2), ("Algoritmos y Estructuras de Datos II", 2022, 1)] debe 
         devolver ["Algoritmos y Estructuras de Datos I"]    
-}
primerElemento :: (String, Integer, Integer) -> String
primerElemento (x,y,z) = x

segundoElemento :: (String, Integer, Integer) -> Integer
segundoElemento (x,y,z) = y

tercerElemento :: (String, Integer, Integer) -> Integer
tercerElemento (x,y,z) = z

vencioElFinal :: [(String, Integer, Integer)] -> [String] -> [String]
vencioElFinal cursada lista | longitud(cursada) == 0 = lista
                            | (segundoElemento(head cursada) <= 2020) || (segundoElemento(head cursada) == 2021 && tercerElemento(head cursada) == 1) = (primerElemento(head cursada)):vencioElFinal (tail cursada) lista
                            | otherwise = vencioElFinal (tail cursada) lista

pertenece :: String -> [String] -> Bool
pertenece elemento lista | longitud(lista) == 0 = False
                         | otherwise = (elemento == (head lista)) || (pertenece elemento (tail lista))

eliminoDuplicados :: [String] -> [String] -> [String]
eliminoDuplicados cursada lista | longitud(cursada) == 0 = lista
                                | not(pertenece (head cursada) lista) = eliminoDuplicados (tail cursada) ([head (cursada)]++lista)
                                | otherwise = eliminoDuplicados (tail cursada) lista

cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas cursada = eliminoDuplicados (vencioElFinal cursada []) []

{-Ejercicio 3 (2 puntos)
problema saturarEnUmbralHastaNegativo (s: seq⟨Z⟩, u: Z) : seq⟨Z⟩ {
  requiere: {u > 0}
  asegura: {La longitud de res es igual a la cantidad de elementos no negativos consecutivos desde el inicio de s}
  asegura: {Para cualquier i en el rango 0 ≤ i < |res| tal que 0 ≤ s[i] ≤ u, se cumple que res[i] = s[i]}
  asegura: {Para cualquier i en el rango 0 ≤ i < |res| tal que s[i] > u, se cumple que res[i] = u}
}
Ejemplo: saturarEnUmbralHastaNegativo [3,8,5,0,7,-2,4] 5 debe devolver [3,5,5,0,5]    
-}

guardoConsecutivos :: [Integer] -> [Integer] -> [Integer]
guardoConsecutivos lista guardoElementos | longitud(lista) == 0 || head(lista) < 0 = guardoElementos
                                         | otherwise = (head(lista)):(guardoConsecutivos (tail lista) guardoElementos)

saturo :: [Integer] -> Integer -> [Integer] -> [Integer]
saturo s u guardoElemento | longitud(s) == 0 = guardoElemento
                          | head(s) > u = (u):(saturo (tail s) u guardoElemento)
                          | otherwise = (head s):(saturo (tail s) u guardoElemento)

saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo s u = saturo (guardoConsecutivos s []) u []

{-Ejercicio 4 (2 puntos)
problema cantidadParesColumna (matriz: seq⟨seq⟨Z⟩⟩, col: Z) : Z{
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {1 ≤ col ≤ |matriz[0]| }
  asegura: {res es la cantidad de números pares de los elementos matriz[i][col-1] para todo i tal que 0 ≤ i < |matriz| }
}
Ejemplo: cantidadParesColumna [[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 2 debe devolver 2
-}

--columnas: 1) [-9, 2, -1] 2) [8, 7, 0] 3) [2,-5,5] 4) [3,3,6]
-- columna 2: [8,7,0] = 2

primerElementoDeCadaFila :: [[Integer]] -> [Integer]
primerElementoDeCadaFila matriz | longitud(matriz) == 0 = []
                                | otherwise = [head (head matriz)] ++ primerElementoDeCadaFila (tail matriz)  

eliminoPrimerElementoDeCadaFila :: [[Integer]] -> [[Integer]]
eliminoPrimerElementoDeCadaFila matriz | longitud(matriz) == 0 = []
                                       | otherwise = tail(head matriz):eliminoPrimerElementoDeCadaFila (tail matriz)

matrizTraspuesta :: [[Integer]] -> [[Integer]] --intercambio las filas y las columnas de mi matriz
matrizTraspuesta matriz | longitud(matriz) == 0 || longitud(head matriz) == 0 = [] --chequeo que si la matriz o la fila de la matriz esté vacía, retorne []
                        | otherwise = (primerElementoDeCadaFila matriz):matrizTraspuesta(eliminoPrimerElementoDeCadaFila matriz)

cantidadDePares :: [Integer] -> Integer
cantidadDePares lista | longitud(lista) == 0 = 0
                      | mod (head lista) 2 == 0 = 1 + cantidadDePares(tail lista)
                      | otherwise = cantidadDePares(tail lista)

cuentoCantidadDePares :: [[Integer]] -> Integer -> Integer -> Integer
cuentoCantidadDePares matriz col indice | indice < col = cuentoCantidadDePares (tail matriz) col (indice + 1)
                                        | otherwise = cantidadDePares (head matriz) 

cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna matriz col = cuentoCantidadDePares (matrizTraspuesta(matriz)) (col-1) 0

{- Ejercicio 5 (0,75 puntos)
Conteste marcando la opción correcta.

¿Qué ocurre si una definición por pattern matching no contempla todos los casos posibles?
1) El programa no compila.
2) Haskell elige un valor por defecto automáticamente.
3) El programa puede lanzar un error en tiempo de ejecución si se invoca con un patrón no contemplado.
-}

--Ejercicio 5: El programa puede lanzar un error en tiempo de ejecución si se invoca con un patrón no contemplado.

{- Ejercicio 6 (0,75 puntos)
Conteste marcando la opción correcta.

Dado un problema con parámetros c (de tipo Char) y s (de tipo String), cuya única precondición es (esVocal(c) ∨ longitud(s) > 3):

1) La precondición garantiza que siempre se trabajará con strings no vacíos.
2) Si c es una consonante y s tiene longitud igual a 2, no se garantiza el comportamiento correcto del programa.
3) Cualquier combinación de valores de c y s es válida, porque la precondición es una disyunción en vez de una conjunción.
-}

--Ejercicio 6: Si c es una consonante y s tiene longitud igual a 2, no se garantiza el comportamiento correcto del programa.