{-Sistema de stock
Una reconocida empresa de comercio electrónico nos pide desarrollar un sistema de stock de mercadería. La mercadería de
la empresa va a ser representada como una secuencia de nombres de los productos, donde puede haber productos repetidos.
El stock va a ser representado como una secuencia de tuplas de dos elementos, donde el primero es el nombre del producto y
el segundo es la cantidad que hay en stock (en este caso no hay nombre de productos repetidos). También se cuenta con una
lista de precios de productos representada como una secuencia de tuplas de dos elementos, donde el primero es el nombre
del producto y el segundo es el precio.
Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo
enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la
Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1. Implementar la función generarStock :: [String] -> [(String, Int)]
problema generarStock (mercadería: seq⟨String⟩) : seq⟨String ×Z⟩ {
    requiere: {True}
    asegura: {La longitud de res es igual a la cantidad de productos distintos que hay en mercadería}
    asegura: {Para cada producto que pertenece a mercadería, existe un i tal que 0 ≤ i < |res| y res[i]_0 = producto y
              res[i]_1 es igual a la cantidad de veces que aparece producto en mercadería}
}
-}
longitud :: (Eq t) => [t] -> Int
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista) 

cantidadProductos :: [String] -> String -> Int
cantidadProductos mercaderia producto | longitud(mercaderia) == 0 = 0
                                      | head(mercaderia) == producto = 1 + cantidadProductos (tail mercaderia) producto
                                      | otherwise = cantidadProductos (tail mercaderia) producto  

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = (head lista == elemento) || pertenece (tail lista) elemento

generoElStock :: [String] -> [(String, Int)]
generoElStock mercaderia | longitud(mercaderia) == 0 = []
                         | otherwise = ((head mercaderia), cantidadProductos mercaderia (head mercaderia)):generoElStock (tail mercaderia) 

eliminoDuplicados :: [(String, Int)] -> [String] -> [(String, Int)]
eliminoDuplicados stock lista | longitud(stock) == 0 = stock
                              | not(pertenece lista (fst(head stock))) = (head stock):eliminoDuplicados (tail stock) ((fst(head stock)):lista) 
                              | otherwise = eliminoDuplicados (tail stock) (lista)

generarStock :: [String] -> [(String, Int)]
generarStock mercaderia = eliminoDuplicados (generoElStock mercaderia) []

{-Ejercicio 2. Implementar la función stockDeProducto :: [(String, Int))] -> String -> Int
problema stockDeProducto (stock: seq⟨String × Z⟩, producto: String) : Z{
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
    requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
    asegura: {si no existe un i tal que 0 ≤i < |stock| y producto = stock[i]_0 entonces res es igual a 0 }
    asegura: {si existe un i tal que 0 ≤i < |stock| y producto = stock[i]_0 entonces res es igual a stock[i]_1}
}
-}
listaDeProductos :: [(String, Int)] -> [String]
listaDeProductos stock | longitud(stock) == 0 = []
                       | otherwise = (fst(head stock)):listaDeProductos (tail stock)             

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto stock producto | not(pertenece (listaDeProductos stock) producto) = 0
                               | fst(head stock) == producto = snd(head stock)
                               | otherwise = stockDeProducto (tail stock) producto                 


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
divisoresMenoresAN :: Int -> Int -> [Int]
divisoresMenoresAN n numero | numero >= n = []
                            | mod n numero == 0 = (numero):divisoresMenoresAN n (numero+1)
                            | otherwise = divisoresMenoresAN n (numero+1)

divisoresPropios :: Int -> [Int]
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
sumaDivisoresPropios :: [Int] -> Int
sumaDivisoresPropios lista | longitud(lista) == 0 = 0
                           | otherwise = (head lista) + sumaDivisoresPropios(tail lista)

sonAmigos :: Int -> Int -> Bool
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
numerosPerfectos :: Int -> Int -> Int -> [Int]
numerosPerfectos n desde cantidad | cantidad == n = []
                                  | (sumaDivisoresPropios(divisoresPropios desde) == desde) = (desde):numerosPerfectos n (desde+1) (cantidad+1)
                                  | otherwise = numerosPerfectos n (desde+1) cantidad

losPrimerosNPerfectos :: Int -> [Int]
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