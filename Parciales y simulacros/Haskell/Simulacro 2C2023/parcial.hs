module Parcial where
{-
Para empezar a dise nar la novedosa y rupturista red social Y el famoso Elio Mark nos ha pedido que desarrollemos algunas
funciones básicas, que tendrán como objetido representar algunas relaciones e interacciones entre los usuarios. 
Para esto nos envió las siguientes especificaciones en lenguaje semiformal y nos pidió que hagamos el desarrollo enteramente 
en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en Introducción a la Programación de Exactas-UBA
-}

{-Ejercicio 1:

problema relacionesValidas (relaciones: seq〈StringxString〉) : Bool {
    requiere: { True }
    asegura: { res = True ←→ relaciones no contiene ni tuplas repetidas (1), ni tuplas con ambas componentes iguales}
}
(1) A los fines de este problema consideraremos que dos tuplas son iguales si el par de elementos que las componen 
(sin importar el orden) son iguales.
-}
longitud :: [(String, String)] -> Integer
longitud l | l == [] = 0
           | otherwise = 1 + longitud(tail l)

tuplasIguales :: (String, String) -> Bool
tuplasIguales (a, b) = a == b

tuplasRepetidas :: [(String, String)] -> Bool
tuplasRepetidas t | longitud(t) == 0 = True
                  | otherwise = longitud((tail t)) /= 0 && (head(t) /= head(tail t)) && tuplasRepetidas(tail t)

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas relaciones | longitud(relaciones) == 0 = True
                             | otherwise = not(tuplasRepetidas(relaciones)) && not(tuplasIguales(head(relaciones))) && relacionesValidas(tail(relaciones))

{-Ejercicio 2:
problema personas (relaciones: seq〈StringxString〉) : seq〈String〉 {
    requiere: { relacionesValidas(relaciones) }
    asegura: { res no tiene elementos repetidos }
    asegura: { res tiene exactamente los elementos que figuran en alguna tupla de relaciones, en cualquiera de sus posiciones}
}
-}
personas :: [(String, String)] -> [String]
personas relaciones | longitud(relaciones) == 0 = []
                    | otherwise = [fst(head relaciones)]++[snd(head(relaciones))]++personas(tail(relaciones))

{-Ejercicio 3:
problema amigosDe (persona: String, relaciones: seq〈StringxString〉) : seq〈String〉 {
    requiere: {relacionesValidas(relaciones)}
    asegura: {res tiene exactamente los elementos que figuran en las tuplas de relaciones en las que una de sus componentes es persona}
}
-}
pertenece :: String -> (String, String) -> Bool
pertenece persona tupla = (persona == fst(tupla) || persona == snd(tupla))

amigosDe :: String -> [(String, String)] -> [String]
amigosDe persona relaciones | longitud(relaciones) == 0 = []
                            | (pertenece persona amigo) && (fst(amigo) == persona) = [snd(amigo)]++amigosDe persona (tail relaciones)
                            | (pertenece persona amigo) && (snd(amigo) == persona) = [fst(amigo)]++amigosDe persona (tail relaciones)
                            | otherwise = amigosDe persona (tail relaciones)
                            where amigo = head relaciones

{-Ejercicio 4:
problema personaConMasAmigos (relaciones: seq〈StringxString〉) : String {
    requiere: {relaciones no vacía}
    requiere: {relacionesValidas(relaciones)}
    asegura: {res es el Strings que aparece más veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}
-}

elMasAmiguero :: [(String, String)] -> (String, String) -> Integer -> String
elMasAmiguero relaciones amistad cantAmigos | longitud(amigosDe amistad relaciones) > cantAmigos =  

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos relaciones = elMasAmiguero relaciones head(relaciones) 0 