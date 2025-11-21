module Parcial where
{-Enunciado:
Resolver los siguientes ejercicios cuyas especificaciones en lenguaje semiformal figuran a continuación. Deben ser 
implementadas en Haskell utilizando los tipos requeridos y solamente las funciones que se ven en la materia 
Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1 (2 puntos)
problema mayorFibonacciEnRango (d: Z, h: Z) : Z {
    requiere: {d ≥ 0}
    requiere: {h ≥ d}
    requiere: {El rango [d, h] contiene al menos un número de Fibonacci}
    asegura: {res es el mayor número de Fibonacci que pertenece al rango [d, h]}
}
Aclaración: Un número es de Fibonacci es aquel que pertenece a la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... definida por la 
fórmula: F(0) = 0, F(1) = 1, y para n ≥ 2: F(n) = F(n-1) + F(n-2).
Ejemplo 1: mayorFibonacciEnRango 4 10 debe devolver 8
Ejemplo 2: mayorFibonacciEnRango 5 8 debe devolver 8
Ejemplo 3: mayorFibonacciEnRango 13 13 debe devolver 13
-}

numeroDeFibonacci :: Int -> Int
numeroDeFibonacci 0 = 0
numeroDeFibonacci 1 = 1
numeroDeFibonacci n = numeroDeFibonacci(n-1) + numeroDeFibonacci(n-2)

listaDeNumeros :: Int -> Int -> [Int]
listaDeNumeros desde hasta | desde > hasta = []
                           | otherwise = desde:listaDeNumeros (desde+1) hasta         

listaDeNumerosDeFibonacci :: Int -> Int -> [Int]
listaDeNumerosDeFibonacci desde hasta | (numeroDeFibonacci desde) > hasta = []
                                      | otherwise = (numeroDeFibonacci desde):listaDeNumerosDeFibonacci (desde+1) hasta
longitud :: (Eq t) => [t] -> Int
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista)

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = head(lista) == elemento || pertenece (tail lista) elemento

sacoNumerosDeFiboDelRango :: [Int] -> [Int] -> [Int]
sacoNumerosDeFiboDelRango lista listaFibo | longitud(lista) == 0 = []
                                          | pertenece listaFibo (head lista) = (head lista):sacoNumerosDeFiboDelRango (tail lista) listaFibo
                                          | otherwise = sacoNumerosDeFiboDelRango (tail lista) listaFibo

mayorNumeroDeFibonacci :: [Int] -> Int -> Int
mayorNumeroDeFibonacci lista mayorNumero | longitud(lista) == 0 = mayorNumero
                                         | (head lista) > mayorNumero = mayorNumeroDeFibonacci (tail lista) (head lista)
                                         | otherwise = mayorNumeroDeFibonacci (tail lista) mayorNumero   

mayorFibonacciEnRango :: Int -> Int -> Int
mayorFibonacciEnRango desde hasta = mayorNumeroDeFibonacci (listaFiboEnRango) (head listaFiboEnRango)
                                  where listaFiboEnRango = sacoNumerosDeFiboDelRango (listaDeNumeros desde hasta) (listaDeNumerosDeFibonacci 0 hasta) 

{-Ejercicio 2 (2 puntos)
problema esMontaniaRusa (l: seq⟨Z⟩) : Bool {
  requiere: {True}
  asegura: {res = true <=> l es una secuencia montaña rusa}
}
Aclaración: Una secuencia montaña rusa es aquella donde las diferencias entre elementos consecutivos se alternan entre positivas y 
negativas (estrictos). Si la primera diferencia es positiva, la siguiente será negativa, y así sucesivamente 
(también puede ser que la primera diferencia sea negativa, la siguiente positiva, etc.).
Ejemplo 1: esMontaniaRusa [1,2,4] debe devolver False
Ejemplo 2: esMontaniaRusa [3,1,4,0] debe devolver True        
-}
--esMontaniaRusa [1,3,2,0]
diferenciaSeAlternaPositivamente :: Int -> [Int] -> Bool
diferenciaSeAlternaPositivamente elemento lista | (longitud(lista) == 1) = (((head lista) - elemento) >= 0)
                                                | otherwise = ((head lista) - elemento) >= 0 && diferenciaSeAlternaNegativamente (head  lista) (tail lista)

diferenciaSeAlternaNegativamente :: Int -> [Int] -> Bool
diferenciaSeAlternaNegativamente elemento lista | (longitud(lista) == 1) = (((head lista) - elemento) < 0)
                                                | otherwise = ((head lista) - elemento) < 0 && diferenciaSeAlternaPositivamente (head lista) (tail lista)

esMontaniaRusa :: [Int] -> Bool
esMontaniaRusa lista | longitud(lista) <= 1 = True 
                     | head(tail lista) - head(lista) < 0 = diferenciaSeAlternaPositivamente (head(tail lista)) (tail(tail lista))
                     | otherwise = diferenciaSeAlternaNegativamente (head(tail lista)) (tail(tail lista))

{-Ejercicio 3 (2 puntos)

Recibimos un listado con todos los libros disponibles en una biblioteca. Cada libro tiene un autor y un título 
(primera y segunda componente del par respectivamente). El objetivo es crear un catálogo, es decir una lista de tuplas 
cuya primera componente es el autor y la segunda es la lista de todos sus títulos.

problema catalogoPorAutores (libros: seq⟨⟨String x String⟩⟩) : seq⟨⟨String x seq⟨String⟩⟩⟩ {
  requiere: {libros no contiene elementos repetidos}
  asegura: {Los autores que aparecen en res son los mismos que aparecen en libros}
  asegura: {res es un catálogo donde cada autor aparece una sola vez junto con la lista de todos sus títulos}
}
Ejemplo 1: catalogoPorAutores [("García Márquez","Cien años de soledad"),("Borges","Ficciones"),("García Márquez","El amor en los tiempos del cólera")] puede devolver 
[("García Márquez",["Cien años de soledad","El amor en los tiempos del cólera"]),("Borges",["Ficciones"])]

Ejemplo 2: catalogoPorAutores [("Poe","El cuervo")] debe devolver [("Poe",["El cuervo"])]
-}
titulosPorAutor :: String -> [(String, String)] -> [String]
titulosPorAutor autor libros | longitud(libros) == 0 = []
                             | fst(head libros) == autor = snd(head libros):titulosPorAutor autor (tail libros)
                             | otherwise = titulosPorAutor autor (tail libros)

creoCatalogo :: [(String, String)] -> [String] -> [(String, [String])]
creoCatalogo libros lista | longitud(libros) == 0 = []
                          | not(pertenece lista autor) = (autor, titulosPorAutor autor libros):creoCatalogo (tail libros) (autor:lista)
                          | otherwise = creoCatalogo (tail libros) (lista) 
                          where autor = fst(head libros)

catalogoPorAutores :: [(String, String)] -> [(String, [String])]
catalogoPorAutores libros = creoCatalogo libros []

{-Ejercicio 4 (2 puntos)
problema filaDelMaximo (matriz: seq⟨seq⟨Z⟩⟩) : Z {
  requiere: {matriz no está vacía y todas sus filas tienen al menos un elemento}
  requiere: {Todos los elementos de matriz tienen la misma longitud}
  requiere: {No hay elementos repetidos en matriz}
  asegura: {res es el número de fila (indexando desde 1) que contiene el valor máximo de toda la matriz}
}
Ejemplo 1: filaDelMaximo [[1,2,3],[4,5,6],[7,8,9]] debe devolver 3
-}

valorMaximo :: [Int] -> Int -> Int
valorMaximo fila maxValor | longitud(fila) == 0 = maxValor
                          | (head fila) > maxValor = valorMaximo (tail fila) (head fila)
                          | otherwise = valorMaximo (tail fila) maxValor

halloElValorMaximo :: [[Int]] -> Int -> Int
halloElValorMaximo matriz maximo | longitud(matriz) == 0 = maximo
                                 | valorMaximo (head matriz) (head(head matriz)) > maximo = halloElValorMaximo (tail matriz) (valorMaximo (head matriz) (head(head matriz)))
                                 | otherwise = halloElValorMaximo (tail matriz) maximo

halloElNumeroDeFila :: [[Int]] -> Int -> Int
halloElNumeroDeFila matriz indice | (valorMaximo (head matriz) (head(head matriz))) == (halloElValorMaximo matriz (valorMaximo (head matriz) (head(head matriz)))) = indice
                                  | otherwise = halloElNumeroDeFila (tail matriz) (indice+1) 

filaDelMaximo :: [[Int]] -> Int
filaDelMaximo matriz = halloElNumeroDeFila matriz 1

{-Ejercicio 5 (1 punto)
Conteste marcando la opción correcta asumiendo que α y β son dos fórmulas de la lógica proposicional tales que α es más fuerte que β:

1) β → α es necesariamente una tautología
2) β → α podría ser una tautología (y también podría no serlo)
3) α → β podría ser una tautología (y también podría no serlo)
-}

--Ejercicio 5: β → α podría ser una tautología (y también podría no serlo)

{-Ejercicio 6 (1 punto)
Respecto al testing de caja negra, conteste marcando la opción correcta asumiendo que se cuenta con la siguiente especificación:

problema unaFuncionQueHaceAlgo (n: Z) : Z {
  requiere: {n > 0}
  asegura: {res = n+1 ∨ res = n-1}
}

1) No es posible armar un caso de test para n = 0 porque no sabemos cuál es exactamente el resultado esperado
2) No es necesario testear el caso n = 0
3) Debo armar dos casos de test para n = 0, en uno el resultado esperado debe ser 1, y en el otro -1
-}

--Ejercicio 6: No es necesario testear el caso n = 0