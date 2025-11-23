{-
Sistema de stock
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

cantApariciones :: [String] -> String -> Int
cantApariciones productos producto | longitud(productos) == 0 = 0
                                   | (head productos) == producto = 1 + cantApariciones (tail productos) producto
                                   | otherwise = cantApariciones (tail productos) producto

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = (head lista) == elemento || pertenece (tail lista) elemento

generoStock :: [String] -> [String] -> [(String, Int)]
generoStock productos lista | longitud(productos) == 0 = []
                            | not(pertenece lista (head productos)) = ((head productos), cantApariciones productos (head productos)):generoStock (tail productos) ((head productos):lista)
                            | otherwise = generoStock (tail productos) lista

generarStock :: [String] -> [(String, Int)]
generarStock productos = generoStock productos []

{-Ejercicio 2. Implementar la función stockDeProducto :: [(String, Int))] -> String -> Int
problema stockDeProducto (stock: seq⟨String × Z⟩, producto: String) : Z{
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
    requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
    asegura: {si no existe un i tal que 0 ≤i < |stock| y producto = stock[i]_0 entonces res es igual a 0 }
    asegura: {si existe un i tal que 0 ≤i < |stock| y producto = stock[i]_0 entonces res es igual a stock[i]_1}
}
-}
listaDeProductosStock :: [(String, Int)] -> [String]
listaDeProductosStock stock | longitud(stock) == 0 = []
                            | otherwise = fst(head stock):listaDeProductosStock (tail stock)

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto stock producto | not(pertenece (listaDeProductosStock(stock)) producto) = 0
                               | fst(head stock) == producto = snd(head stock)
                               | otherwise = stockDeProducto (tail stock) producto             

{-Ejercicio 3. Implementar la función dineroEnStock :: [(String, Int))] -> [(String, Float)] -> Float
problema dineroEnStock (stock: seq⟨String ×Z⟩, precios: seq⟨String ×R⟩ ) : R {
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
    requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
    requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
    requiere: {Todo producto de stock aparece en la lista de precios}
    asegura: {res es igual a la suma de los precios de todos los productos que están en stock multiplicado por la cantidad
    de cada producto que hay en stock}
}
Para resolver este ejercicio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo
Int devuelve su equivalente de tipo Float.
-}
listaDeProductosPrecios :: [(String, Float)] -> [String]
listaDeProductosPrecios precios | longitud(precios) == 0 = []
                                | otherwise = fst(head precios):listaDeProductosPrecios (tail precios)

precioDeProducto :: [(String, Float)] -> String -> Float
precioDeProducto precios producto | not(pertenece (listaDeProductosPrecios precios) producto) = 0
                                  | fst(head precios) == producto = snd(head precios)
                                  | otherwise = precioDeProducto (tail precios) producto

multiplicoCantConPrecio :: Int -> Float -> Float
multiplicoCantConPrecio cantidad precio = (fromIntegral cantidad)*precio

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock stock precios | longitud(stock) == 0 = 0.0
                            | otherwise = (multiplicoCantConPrecio (stockDeProducto stock (fst(head stock))) (precioDeProducto precios (fst(head stock)))) + dineroEnStock (tail stock) (tail precios)

{-Ejercicio 4. 
Implementar la función aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String,Float)]
problema aplicarOferta (stock: seq⟨String ×Z⟩, precios: seq⟨String ×R⟩ ) : seq⟨String × R⟩ {
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
    requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
    requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
    requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
    requiere: {Todo producto de stock aparece en la lista de precios}
    asegura: {|res|= |precios|}
    asegura: {Para todo 0 ≤i < |precios|, si stockDeProducto(stock, precios[i]_0) > 10, entonces res[i]_0 = precios[i]_0 y
              res[i]_1 = precios[i]_1∗ 0,80}
    asegura: {Para todo 0 ≤i < |precios|, si stockDeProducto(stock, precios[i]_0) ≤ 10, entonces res[i]_0 = precios[i]_0 y
              res[i]_1 = precios[i]_1}
}
-}
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta stock precios | longitud(precios) == 0 = []
                            |(stockDeProducto (stock) (fst(head precios))) > 10 = ((fst(head precios)), (snd(head precios))*0.80):aplicarOferta (stock) (tail precios)
                            | otherwise = ((fst(head precios)), (snd(head precios))):aplicarOferta (stock) (tail precios)

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
perteneceElAmigo :: [Int] -> Int -> Bool
perteneceElAmigo lista numero | longitud(lista) == 0 = False
                              | otherwise = sonAmigos (head lista) numero || perteneceElAmigo (tail lista) numero  

encuentroAlAmigo :: [Int] -> Int -> Int
encuentroAlAmigo lista numero | sonAmigos (head lista) numero = head lista
                              | otherwise = encuentroAlAmigo (tail lista) numero

numerosAmigos :: [Int] -> [Int] -> [(Int, Int)]
numerosAmigos lista guardoElementos | longitud(lista) == 0 = []
                                    | not(perteneceElAmigo lista (head lista)) = numerosAmigos (tail lista) (guardoElementos)
                                    | otherwise = ((head lista), encuentroAlAmigo lista (head lista)):numerosAmigos (tail lista) (primerElemento:segundoElemento:guardoElementos)
                                    where primerElemento = (head lista)
                                          segundoElemento = (encuentroAlAmigo lista (head lista))
listaDeAmigos :: [Int] -> [(Int, Int)]
listaDeAmigos lista = numerosAmigos lista []