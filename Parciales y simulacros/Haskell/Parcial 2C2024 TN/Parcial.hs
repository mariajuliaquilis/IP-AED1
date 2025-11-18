module Parcial where
{-
Enunciado:
Resolver los siguientes ejercicios cuyas especificaciones en lenguaje semiformal figuran a continuación. Deben ser implementadas en Haskell
utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras
de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1 (2 puntos)

problema maxMovilN (lista: seq⟨Z⟩, n: Z) : Z {
    requiere: {|lista| > 0}
    requiere: {n > 0 y n es menor a la longitud de la lista}
    asegura: {res es el máximo de los últimos n elementos de lista.}
}
-}
longitud :: (Eq t) => [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

maximo :: [Int] -> Int -> Int
maximo lista maxElemento | longitud(lista) == 0 = maxElemento
                         | head(lista) > maxElemento = maximo (tail lista) (head lista)
                         | otherwise = maximo (tail lista) maxElemento

extraigoLista :: [Int] -> Int -> [Int] -> [Int]
extraigoLista lista n nuevaLista | longitud(lista) == n = lista++nuevaLista
                                 | otherwise = extraigoLista (tail lista) n nuevaLista 

maxMovilN :: [Int] -> Int -> Int
maxMovilN lista n = maximo (extraigoLista lista n []) (head(extraigoLista lista n []))

{-Ejercicio 2 (2 puntos)

problema promedioPrimo (n: Z) : Float {
  requiere: {n > 1}
  asegura: {(res es el promedio de todos los factores primos de n (distintos o no).}
}
Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 
-}
listaDivisores :: Int -> Int -> [Int]
listaDivisores n numero | numero > n = []
                        | mod n numero == 0 = (numero):(listaDivisores n (numero+1))
                        | otherwise = listaDivisores n (numero+1)    
esPrimo :: Int -> Bool
esPrimo n = listaDivisores n 1 == [1, n]

factoresPrimos :: Int -> Int -> [Int]
factoresPrimos numero desde | desde > numero = []
                            | (mod numero desde == 0) && (esPrimo desde)  = (desde):factoresPrimos (div numero desde) desde
                            | otherwise = factoresPrimos numero (desde+1)
sumaFactores :: [Int] -> Int
sumaFactores lista | longitud(lista) == 0 = 0
                   | otherwise = (head lista) + sumaFactores(tail lista) 

promedio :: [Int] -> Float
promedio lista = fromIntegral(sumaFactores lista)/fromIntegral(longitud lista)

promedioPrimo :: Int -> Float
promedioPrimo n = promedio (factoresPrimos n 1)

{-Ejercicio 3 (2 puntos)

problema letrasIguales (palabra: seq⟨Char⟩) : Z {
  requiere: {True}
  asegura: {(res es la cantidad de caracteres no blancos repetidos en palabra.}
}
-}
cantRepeticiones :: [Char] -> Char -> Int
cantRepeticiones palabra caracter | longitud(palabra) == 0 = 0
                                  | head(palabra) == caracter = 1 + cantRepeticiones (tail palabra) caracter
                                  | otherwise = cantRepeticiones (tail palabra) caracter
pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = (head lista) == elemento || pertenece (tail lista) elemento

cuentoRepeticiones :: [Char] -> [Char] -> Int
cuentoRepeticiones palabra lista | longitud(palabra) == 0 = 0
                                 | cantRepeticiones palabra (head palabra) > 1 && not(pertenece lista (head palabra)) && (head palabra) /= ' ' = 1 + cuentoRepeticiones (tail palabra) ((head palabra):lista)
                                 | otherwise = cuentoRepeticiones (tail palabra) lista  

letrasIguales :: [Char] -> Int
letrasIguales palabra = cuentoRepeticiones palabra []

{-Ejercicio 4 (3 puntos)
problema cuantosIguales (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Z⟩{
  requiere: {True}
  asegura: {res es igual a la cantidad de caracteres no blancos e iguales que palabra1 y palabra2 tienen en común.}
}
-}
letrasEnComun :: [Char] -> [Char] -> [Char] -> Int
letrasEnComun palabra1 palabra2 lista | longitud(palabra1) == 0 = 0
                                      | (cantRepeticiones palabra2 (head palabra1)) > 0 && not(pertenece lista (head palabra1)) = 1 + letrasEnComun (tail palabra1) palabra2 ((head palabra1):lista)
                                      | otherwise = letrasEnComun (tail palabra1) palabra2 lista

cuantosIguales :: [Char] -> [Char] -> Int
cuantosIguales palabra1 palabra2 = letrasEnComun palabra1 palabra2 []

{-Ejercicio 5 (1 punto)
¿Cuál de las siguientes afirmaciones es correcta sobre el uso de pattern matching en Haskell?

1) Pattern matching en Haskell solo se utiliza con listas y tuplas.
2) Pattern matching en Haskell permite seleccionar qué cláusula de una definición de función ejecutar según la forma de los parámetros.
3) Pattern matching en Haskell siempre debe manejar todas las posibles combinaciones de patrones, de lo contrario, el compilador 
   lanzará un error.
-}
--Ejercicio 5: 2) Pattern matching en Haskell permite seleccionar qué cláusula de una definición de función ejecutar según la forma de los parámetros.