module Solucion where

-- Ejercicio 1
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes d h | d > h = 0
                              | otherwise = unoSiCeroSiNo (esNumeroAbundante d) + cantidadNumerosAbundantes (d + 1) h

unoSiCeroSiNo :: Bool -> Integer
unoSiCeroSiNo True = 1
unoSiCeroSiNo False = 0

esNumeroAbundante :: Integer -> Bool
esNumeroAbundante n = sumaDivisoresPropios n > n

sumaDivisoresPropios :: Integer -> Integer
sumaDivisoresPropios n = sumaDivisoresPropiosDesde 1 n

sumaDivisoresPropiosDesde :: Integer -> Integer -> Integer
sumaDivisoresPropiosDesde d n | d == n = 0
                              | otherwise = d * (unoSiCeroSiNo (esDivisible n d)) + sumaDivisoresPropiosDesde (d+1) n

esDivisible :: Integer -> Integer -> Bool
esDivisible n d = mod n d == 0

-- Ejercicio 2
cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas xs = sinRepetidos (cursadasVencidasConRepetidos xs)

cursadasVencidasConRepetidos :: [(String, Integer, Integer)] -> [String]
cursadasVencidasConRepetidos [] = []
cursadasVencidasConRepetidos ((materia, año, cuatrimestre):cursadas) | esCursadaVencida = materia : cursadasVencidasConRepetidos cursadas
                                                                     | otherwise = cursadasVencidasConRepetidos cursadas
                                                                      where esCursadaVencida = año < 2021 || (año == 2021 && cuatrimestre <= 1)
                                         
sinRepetidos :: [String] -> [String]
sinRepetidos [] = []
sinRepetidos (x:xs) | pertenece x xs = sinRepetidos xs
                    | otherwise  = x : sinRepetidos xs
                    
pertenece :: Eq a => a -> [a] -> Bool
pertenece _ [] = False
pertenece elem (x:xs) | elem == x = True
                      | otherwise = pertenece elem xs

-- Ejercicio 3
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] _ = []
saturarEnUmbralHastaNegativo (x:xs) u | x > u = u:saturarEnUmbralHastaNegativo xs u
                                      | x < 0 = []
                                      | otherwise = x:saturarEnUmbralHastaNegativo xs u

-- Ejercicio 4
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] _ = 0
cantidadParesColumna (fila:subMatriz) col = unoSiCeroSiNo (esPar (obtenerElemento fila (col - 1))) + cantidadParesColumna subMatriz col

obtenerElemento :: [Integer] -> Integer -> Integer
obtenerElemento (x:xs) 0 = x
obtenerElemento (x:xs) pos = obtenerElemento xs (pos - 1)

esPar :: Integer -> Bool
esPar n = esDivisible n 2
