module Parcial where
{-Ejercicio 1)
problema hayPrimosGemelos (d: Z,h: Z) : Bool {
  requiere: {0 < d <= h}
  asegura: {res = true <=> existen dos números p1 y p2 contenidos en el rango [d..h] tales que p1 y p2 son primos gemelos}
}
Aclaración: Se dice que p1 y p2 son primos gemelos si ambos son primos y además |p2-p1| = 2
-}
longitud :: (Eq t) => [t] -> Int
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista)

listaHastaN :: Int -> Int -> [Int]
listaHastaN desde hasta | desde > hasta = []
                        | otherwise = desde:listaHastaN (desde+1) hasta 

listaDivisoresN :: Int -> [Int] -> [Int]
listaDivisoresN n lista | longitud(lista) == 0 = []
                        | mod n (head lista) == 0 = (head lista):listaDivisoresN n (tail lista)
                        | otherwise = listaDivisoresN n (tail lista)
                    
esPrimo :: Int -> Bool
esPrimo n = listaDivisoresN n (listaHastaN 1 n) == [1, n]

listaDePrimos :: Int -> Int -> [Int]
listaDePrimos desde hasta | desde > hasta = []
                          | esPrimo desde = desde:listaDePrimos (desde+1) hasta
                          | otherwise = listaDePrimos (desde+1) hasta

diferenciaAbsoluta :: Int -> Int -> Int
diferenciaAbsoluta a b | a - b < 0 = -(a-b)
                       | otherwise = a-b 

existeParDePrimosGemelos :: Int -> [Int] -> Bool
existeParDePrimosGemelos numero lista | longitud(lista) == 0 = False
                                      | otherwise = (diferenciaAbsoluta numero (head lista) == 2) || existeParDePrimosGemelos numero (tail lista)

hayParesDePrimosGemelos :: [Int] -> [Int] -> Bool
hayParesDePrimosGemelos lista mismaLista | longitud(lista) == 0 = False
                                         | existeParDePrimosGemelos (head lista) mismaLista = True 
                                         | otherwise = hayParesDePrimosGemelos (tail lista) mismaLista

hayPrimosGemelos :: Int -> Int -> Bool
hayPrimosGemelos d h = hayParesDePrimosGemelos (listaDePrimos d h) (listaDePrimos d h)

{-Ejercicio 2)
Representaremos un di­a de cursada de cierta materia con una tupla String x String x Z x Z, donde:
-)La primera componente de la tupla contiene el nombre de una materia
-)La segunda componente de la tupla contiene el día de cursada (lunes, martes, etc)
-)La tercera componente de la tupla contiene el horario de inicio de la cursada de ese día
-)La cuarta componente de la tupla contiene el horario de fin de la cursada de ese día
Se pide implementar materiasTurnoTarde, que dada una lista de cursadas devuelva aquellas materias que se cursan en el turno tarde (14 a 17hs)

problema materiasTurnoTarde (s: seq<String x String x Z x Z>) :seq<String> {
  requiere: { s[i]_1 es alguno de los siguientes valores: "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"}
  requiere: { s[i]_2 >= 8 para todo i tal que 0 <= i < |s|}
  requiere: { s[i]3 <= 22 para todo i tal que 0 <= i < |s|}
  requiere: { s[i]_2 < s[i]_3 para todo i tal que 0 <= i < |s|}
  asegura: {res no tiene elementos repetidos}
  asegura: {res contiene los nombre de todas las materias incluí­das en s tales que el horario de cursada de dichas materias 
            se superpone (total o parcialmente) con el rango (14..17)}
  asegura: {res contiene solamente los nombre las materias incluí­das en s tales el horario de cursada de dichas materias 
            se superpone (total o parcialmente) con el rango (14..17)}
}
-}
primeraComponente :: (String, String, Int, Int) -> String
primeraComponente (x,y,z,w) = x

terceraComponente :: (String, String, Int, Int) -> Int
terceraComponente (x,y,z,w) = z 

cuartaComponente :: (String, String, Int, Int) -> Int
cuartaComponente (x,y,z,w) = w

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = (head lista) == elemento || pertenece (tail lista) elemento

sinRepeticiones :: [String] -> [String] -> [String]
sinRepeticiones materias lista | longitud(materias) == 0 = []
                               | not(pertenece lista (head materias)) = (head materias):sinRepeticiones (tail materias) ((head materias):lista)
                               | otherwise = sinRepeticiones (tail materias) lista

horasDeCursada :: Int -> Int -> [Int]
horasDeCursada inicio fin | inicio == fin = []  --fin no forma parte del horario de cursada, está excluido dentro del intervalo (inicio, fin)
                          | otherwise = inicio:horasDeCursada (inicio+1) fin

estaEnElRango :: [Int] -> [Int] -> Bool
estaEnElRango horarios horariosTarde | longitud(horarios) == 0 = False
                                     | otherwise = pertenece horariosTarde (head horarios) || estaEnElRango (tail horarios) (horariosTarde)

materiasEnElRango :: [(String, String, Int, Int)] -> [String]
materiasEnElRango materias  | longitud(materias) == 0 = []
                            | estaEnElRango (horasDeCursada (terceraComponente(head materias)) (cuartaComponente(head materias))) (horasDeCursada 14 17) = primeraComponente(head materias):materiasEnElRango(tail materias)
                            | otherwise = materiasEnElRango(tail materias)

materiasTurnoTarde :: [(String, String, Int, Int)] -> [String]
materiasTurnoTarde materias = sinRepeticiones (materiasEnElRango(materias)) []

{-Ejercicio 3)
problema maximaSumaDeTresConsecutivos (s: seq <Z>) : Z {
  requiere: {|s| >= 3}
  asegura: {res es la suma de tres elementos que se encuentran en posiciones consecutivas de s}
  asegura: {Para cualquier i en el rango 1 <= i < |s|-1, se cumple que s[i-1] + s[i] + s[i+1] <= res}
-}
sumaMaxima :: [Integer] -> Integer -> Integer
sumaMaxima lista maximo | longitud(lista) == 3 && (sumoLosElementos > maximo) = sumoLosElementos
                        | longitud(lista) == 3 && (sumoLosElementos <= maximo) = maximo
                        | sumoLosElementos > maximo = sumaMaxima (tail lista) (sumoLosElementos)
                        | otherwise = sumaMaxima (tail lista) maximo
                        where primerElemento = (head lista)
                              segundoElemento = (head(tail lista))
                              tercerElemento = (head(tail(tail lista))) 
                              sumoLosElementos = primerElemento + segundoElemento + tercerElemento

maximaSumaDeTresConsecutivos :: [Integer] -> Integer
maximaSumaDeTresConsecutivos lista = sumaMaxima lista (primerElemento+segundoElemento+tercerElemento)
                                   where primerElemento = (head lista)
                                         segundoElemento = (head(tail lista))
                                         tercerElemento = (head(tail(tail lista)))
                                         
{-Ejercicio 4)
problema sumaIesimaColumna (matriz: seq<seq<Integer>>, col: Integer) : Integer{
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {1 <= col <= |matriz[0]| }
  asegura: {res es la sumatoria de los elementos matriz[i][col-1] para todo i tal que 0 <= i < |matriz|}
}
-}
extraigoPrimerElementoDeFilas :: [[Integer]] -> [Integer]
extraigoPrimerElementoDeFilas matriz | longitud(matriz) == 0 = []
                                     | otherwise = (head(head matriz)):extraigoPrimerElementoDeFilas(tail matriz)

eliminoPrimerElementoDeFilas :: [[Integer]] -> [[Integer]]
eliminoPrimerElementoDeFilas matriz | longitud(matriz) == 0 = []
                                    | otherwise = tail(head matriz):eliminoPrimerElementoDeFilas (tail matriz) 

matrizTraspuesta :: [[Integer]] -> [[Integer]]
matrizTraspuesta matriz | longitud(matriz) == 0 || longitud(head matriz) == 0 = []
                        | otherwise = extraigoPrimerElementoDeFilas(matriz):matrizTraspuesta(eliminoPrimerElementoDeFilas(matriz))

sumoColumna :: [Integer] -> Integer
sumoColumna columna | longitud(columna) == 0 = 0
                    | otherwise = (head columna) + sumoColumna(tail columna)

numeroDeColumna :: [[Integer]] -> [Integer] -> Integer
numeroDeColumna matriz fila | (head matriz) == fila = 1
                            | otherwise = 1 + numeroDeColumna(tail matriz) fila

extraigoColumna :: [[Integer]] -> [[Integer]] -> Integer -> [Integer]
extraigoColumna matriz mismaMatriz col | (numeroDeColumna mismaMatriz (head matriz)) == col = (head matriz)
                                       | otherwise = extraigoColumna (tail matriz) mismaMatriz col

sumaIesimaColumna :: [[Integer]] -> Integer -> Integer
sumaIesimaColumna matriz columna = sumoColumna(extraigoColumna (matrizTraspuesta(matriz)) (matrizTraspuesta(matriz)) columna)