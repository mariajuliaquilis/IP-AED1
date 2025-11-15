{-Perfectos amigos
El Departamento de Matemática (DM) de la FCEyN-UBA nos ha encargado que desarrollemos un sistema para el tratamiento de números naturales.
Específicamente les interesa conocer cuándo un número es perfecto y cuándo dos números son amigos. Aunque por ahí no lo sabías, estos 
conceptos existen y se definen como:
Un número natural es perfecto cuando la suma de sus divisores propios (números que lo dividen menores a ́el) es igual al mismo número.
Por ejemplo, 6 es un número perfecto porque la suma de sus divisores propios (1,2 y 3) es igual a 6.
Dos números naturales distintos son amigos si cada uno de ellos se obtiene sumando los divisores propios del otro.
Por ejemplo, 220 y 284 son amigos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110 que sumados dan 284 y
los divisores propios de 284 son 1, 2 , 4, 71, 142 que sumados dan 220.
Para implementar este sistema nos enviaron las siguientes especificaciones en lenguaje semiformal y nos pidieron que hagamos el desarrollo
enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia
Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
-}

{-Ejercicio 9. 
Implementar la función divisoresPropios :: Int -> [Int]
problema divisoresPropios (n: Z) : seq⟨Z⟩ {
    requiere: {n > 0}
    asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
    asegura: {res no tiene elementos repetidos}
    asegura: {res no contiene a ningún elemento que no sea un divisor propio de n}
}
-}
divisoresMenoresAN :: Integer -> Integer -> [Integer]
divisoresMenoresAN n numero | numero >= n = []
                            | mod n numero == 0 = (numero):divisoresMenoresAN n (numero+1)
                            | otherwise = divisoresMenoresAN n (numero+1)

divisoresPropios :: Integer -> [Integer]
divisoresPropios n = divisoresMenoresAN n 1

{-Ejercicio 10. 
Implementar la función sonAmigos :: Int -> Int ->Bool
problema sonAmigos (n,m: Z) : Bool{
    requiere: {n > 0}
    requiere: {m > 0}
    requiere: {m /= n}
    asegura: {res = True ⇔ n y m son números amigos}
}
-}
longitud :: [Integer] -> Integer
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista) 

sumaDivisoresPropios :: [Integer] -> Integer
sumaDivisoresPropios lista | longitud(lista) == 0 = 0
                           | otherwise = (head lista) + sumaDivisoresPropios(tail lista)

sonAmigos :: Integer -> Integer -> Bool
sonAmigos n m = (sumaDivisoresPropios(divisoresPropios n) == m) && (sumaDivisoresPropios(divisoresPropios m) == n)

{-Ejercicio 11. 
Implementar la función losPrimerosNPerfectos :: Int ->[Int]
problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
    requiere: {n > 0}
    asegura: {|res| = n}
    asegura: {res es la lista de los primeros n n´umeros perfectos, de menor a mayor}
}
Por cuestiones de tiempos de ejecución, no les recomendamos que prueben este ejercicio con un n > 4.
-}

{-Un número natural es perfecto cuando la suma de sus divisores propios (números que lo dividen menores a ́el) es igual al mismo número.
Por ejemplo, 6 es un número perfecto porque la suma de sus divisores propios (1,2 y 3) es igual a 6.
-}
numerosPerfectos :: Integer -> Integer -> Integer -> [Integer]
numerosPerfectos n desde cantidad | cantidad == n = []
                                  | (sumaDivisoresPropios(divisoresPropios desde) == desde) = (desde):numerosPerfectos n (desde+1) (cantidad+1)
                                  | otherwise = numerosPerfectos n (desde+1) cantidad

losPrimerosNPerfectos :: Integer -> [Integer]
losPrimerosNPerfectos n = numerosPerfectos n 1 0

{-Ejercicio 12. 
Implementar la función listaDeAmigos :: [Int] -> [(Int,Int)]
problema listaDeAmigos (lista: seq⟨Z⟩) : seq⟨Z × Z⟩ {
    requiere: {Todos los números de lista son mayores a 0}
    requiere: {Todos los números de lista son distintos}
    asegura: {res es una lista de tuplas sin repetidos, que contiene a todos los pares de números que pertenecen a lista y son amigos entre sí}
    asegura: {|res| es igual a la cantidad de pares de números amigos que hay en lista.}
}
-}
listaDeAmigos :: [Integer] -> [(Integer, Integer)]
