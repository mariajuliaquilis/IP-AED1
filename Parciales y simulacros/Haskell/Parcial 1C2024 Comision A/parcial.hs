module Parcial where
{-Enunciado
La codificación por sustitución es una de las técnicas de cifrado más simples, en el que un caracter en el texto original es 
reemplazado por otro caracter dependiendo de un mapeo. Este mapeo puede representarse con una secuencia de tuplas de dos caracteres,
donde la primera componente de la tupla representa el caracter original y la segunda componente el caracter por el cual se lo va a 
sustituir. Por simplicidad, en este problema codificaremos solo los caracteres que aparecen en el mapeo dado. 
Todos los restantes caracteres quedan inalterados en el mensaje codificado.
Para implementar este sistema de codificación nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo
enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia 
Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1 (2 puntos)
problema hayQueCodificar (c: Char, mapeo: seq⟨Char x Char⟩ ) : Bool {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  asegura: {res = true <=> c es igual a la primera componente de alguna tupla de mapeo}
}
-}
longitud :: (Eq t) => [t] -> Int 
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista)

-- pertenece :: (Eq t) => [t] -> t -> Bool
-- pertenece lista elemento | longitud(lista) == 0 = False
--                          | otherwise = (head lista) == elemento || pertenece (tail lista) elemento

hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar caracter mapeo | longitud(mapeo) == 0 = False
                               | otherwise = caracter == (fst(head mapeo)) || hayQueCodificar caracter (tail mapeo)

{-Ejercicio 2 (2 puntos)
problema cuantasVecesHayQueCodificar (c: Char, frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Z {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0}
  requiere: {c pertenece a frase}
  asegura: {(res = 0 y hayQueCodificar (c, mapeo) = false) o 
            (res = cantidad de veces que c aparece en frase y hayQueCodificar (c, mapeo) = true)}
}
-}
cantApariciones :: [Char] -> Char -> Int
cantApariciones lista elemento | longitud(lista) == 0 = 0
                               | elemento == (head lista) = 1 + cantApariciones (tail lista) elemento
                               | otherwise = cantApariciones (tail lista) elemento

cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar c frase mapeo | not(hayQueCodificar c mapeo) = 0
                                          | otherwise = cantApariciones frase c

{-Ejercicio 3 (2 puntos)
problema laQueMasHayQueCodificar (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Char {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0}
  requiere: {Existe al menos un c que pertenece a frase y hayQueCodificar(c, mapeo) = true}
  asegura: {res = c donde c es el caracter tal que cuantasVecesHayQueCodificar(c, frase, mapeo) es mayor a cualquier otro caracter
            perteneciente a frase}
  asegura: {Si existen más de un caracter c que cumple la condición anterior, devuelve el que aparece primero en frase}
}
-}
caracterQueMasHayQueCodificar :: [Char] -> [Char] -> [(Char, Char)] -> Char -> Char
caracterQueMasHayQueCodificar frase mismaFrase mapeo mayor | longitud(frase) == 0 = mayor
                                                           | cuantasVecesHayQueCodificar (head frase) mismaFrase mapeo > cuantasVecesHayQueCodificar mayor mismaFrase mapeo = caracterQueMasHayQueCodificar (tail frase) mismaFrase mapeo (head frase)
                                                           | otherwise = caracterQueMasHayQueCodificar (tail frase) mismaFrase mapeo mayor

laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar frase mapeo = caracterQueMasHayQueCodificar frase frase mapeo (head frase)

{-Ejercicio 4 (3 puntos)
problema codificarFrase (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : seq ⟨Char⟩ {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  asegura: {|res| = |frase|}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = true entonces
             res[i] = mapeo[j]_1, para un j tal que 0 <= j < |mapeo| y mapeo[j]_0 = frase[i]}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = false entonces res[i] = frase[i]}
}
-}
buscoElMapeo :: Char -> [(Char, Char)] -> Char
buscoElMapeo caracter mapeo | fst(head mapeo) == caracter = snd(head mapeo)
                            | otherwise = buscoElMapeo caracter (tail mapeo)
                            
codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase frase mapeo | longitud(frase) == 0 = []
                           | hayQueCodificar (head frase) mapeo = (buscoElMapeo (head frase) mapeo):codificarFrase (tail frase) mapeo
                           | otherwise = (head frase):codificarFrase (tail frase) mapeo

{-Ejercicio 5 (1 punto) 
Conteste marcando la opción correcta.
Si un usuario no cumple con la precondición de la especificación de un programa y el programa no termina (se cuelga):
1) El usuario tiene derecho a quejarse porque el programador debería haber contemplado ese caso.
2) El usuario no tiene derecho a quejarse, pero el programa es incorrecto porque no debería colgarse.
3) El usuario no tiene derecho a quejarse y no importa que el programa se cuelgue para este caso.
-}
--Ejercicio 5: El usuario no tiene derecho a quejarse y no importa que el programa se cuelgue para este caso.