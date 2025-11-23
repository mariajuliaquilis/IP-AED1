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

{-Ejercicio 3)
problema maximaSumaDeTresConsecutivos (s: seq <Z>) : Z {
  requiere: { |s| >= 3}
  asegura: { res es la suma de tres elementos que se encuentran en posiciones consecutivas de s }
  asegura: {Para cualquier i en el rango 1 <= i < |s|-1, se cumple que s[i-1] + s[i] + s[i+1] <= res}
-}

{-Ejercicio 4)
problema sumaIesimaColumna (matriz: seq<seq<Integer>>, col: Integer) : Integer{
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {1 <= col <= |matriz[0]| }
  asegura: {res es la sumatoria de los elementos matriz[i][col-1] para todo i tal que 0 <= i < |matriz|}
}
-}