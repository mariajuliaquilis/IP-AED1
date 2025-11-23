module Parcial where

{-Enunciado
Una reconocida empresa de comercio electrónico nos pide desarrollar un sistema de stock de mercadería. 
El conjunto de mercaderías puede representarse con una secuencia de nombres de los productos donde puede haber productos repetidos. 
El stock puede representarse como una secuencia de tuplas de dos elementos, donde el primero es el nombre del producto y el segundo 
es la cantidad que hay en stock (en este caso no hay nombre de productos repetidos). 
También se cuenta con una lista de precios de productos representada como una secuencia de tuplas de dos elementos, donde el primero 
es el nombre del producto y el segundo es el precio.
Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell, 
utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras 
de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1 (2 puntos)
problema generarStock (productos: seq⟨seq⟨Char⟩⟩): seq⟨seq⟨Char⟩ x Z⟩ {
    requiere: {True}
    asegura: {La longitud de res es igual a la cantidad de productos distintos que hay en productos}
    asegura: {Para cada producto que pertenece a productos existe un i tal que 0 <= i < |res| y res[i]_0 = producto y res[i]_1 es igual a la
              cantidad de veces que aparece producto en productos}
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

{-Ejercicio 2 (2 puntos)
problema stockDeProducto (stock:seq⟨seq⟨Char⟩ x Z⟩, producto: seq⟨Char⟩) : Z {
    requiere: {No hay productos repetidos en stock}
    requiere: {Todas las cantidades de los productos que hay en stock son mayores a cero}
    asegura: {(res = 0 y producto no se encuentra en el stock) o (existe un i tal que 0 <= i < |stock| y producto = stock[i]_0 y
               res = stock[i]_1)}
}
-}
listaDeProductosStock :: [(String, Int)] -> [String]
listaDeProductosStock stock | longitud(stock) == 0 = []
                            | otherwise = fst(head stock):listaDeProductosStock (tail stock)

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto stock producto | not(pertenece (listaDeProductosStock(stock)) producto) = 0
                               | fst(head stock) == producto = snd(head stock)
                               | otherwise = stockDeProducto (tail stock) producto

{-Ejercicio 3 (2 puntos)
problema dineroEnStock (stock:seq⟨seq⟨Char⟩ x Z⟩, precios: seq⟨seq⟨Char⟩ x R⟩): R {
    requiere: {No hay productos repetidos en stock}
    requiere: {Todas las cantidades de los productos que hay en stock son mayores a cero}
    requiere: {No hay productos repetidos en precios}
    requiere: {Todos los precios de los productos son mayores a cero}
    requiere: {Todo producto en stock aparece en la lista de precios}
    asegura: {res es igual a la suma de los precios de todos los productos que están en stock multiplicado por 
              la cantidad de cada producto que hay en stock}
}
Para resolver este ejercicio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Int devuelve
su equivalente de tipo Float.
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

{-Ejercicio 4 (3 puntos)
problema aplicarOferta (stock:seq⟨seq⟨Char⟩ x Z⟩, precios: seq⟨seq⟨Char⟩ x R⟩: seq⟨seq⟨Char⟩ x R⟩) {
    requiere: {No hay productos repetidos en stock}
    requiere: {Todas las cantidades de los productos que hay en stock son mayores a cero}
    requiere: {No hay productos repetidos en precios}
    requiere: {Todos los precios de los productos son mayores a cero}
    requiere: {Todo producto en stock aparece en la lista de precios}
    asegura: {|res| = | precios|}
    asegura: {Para todo 0 <= i < |precios| si stockDeProducto(stock, precios[i]_0) > 10 entonces 
              res[i]_0 = precios[i]_0 y res[i]_1 = precios[i]_1 * 0,80}
    asegura: {Para todo 0 <= i < |precios| si stockDeProducto(stock, precios[i]_0) <= 10 entonces 
              res[i]_0 = precios[i]_0 y res[i]_1 = precios[i]_1}
}
-}
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta stock precios | longitud(precios) == 0 = []
                            |(stockDeProducto (stock) (fst(head precios))) > 10 = ((fst(head precios)), (snd(head precios))*0.80):aplicarOferta (stock) (tail precios)
                            | otherwise = ((fst(head precios)), (snd(head precios))):aplicarOferta (stock) (tail precios)
{-Ejercicio 5 (1 punto). 
Conteste marcando la opción correcta.
En el contexto de la programación funcional, se llama polimorfismo:
1) Cuando una función puede invocarse con distintos tipos de datos sin tener que redefinirla.
2) Cuando una función puede invocarse con distintos tipos de datos teniendo que definirla para cada tipo de dato particular.
3) Cuando tengo un tipo de dato que puede ser usado para invocar a muchas funciones.
-}

--Ejercicio 5: Cuando una función puede invocarse con distintos tipos de datos sin tener que redefinirla.