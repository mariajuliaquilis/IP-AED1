--Ejercicio 1.
--a)
f :: Integer -> Integer
f x | x == 1 = 8
    | x == 4 = 131
    | otherwise = 16

--b)
--Especifico g:
{--
problema g (n: Z) : Z {
    requiere {n = 8 ∨ n = 16 ∨ n = 1}
    asegura {(n = 8 → res = 16) ∧ (n = 16 → res = 4) ∧ (n = 131 → res = 1)}
}
--}
g :: Integer -> Integer
g x | x == 8 = 16
    | x == 16 = 4
    |otherwise = 1

--c)
h :: Integer -> Integer
h x = f(g(x))

k :: Integer -> Integer
k x = g(f(x))

--Ejercicio 2.
--a)
absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
           | otherwise = (-1)*n

--b)
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | absoluto x >= absoluto y = absoluto x
                   | otherwise = absoluto y

--c)
--reutilizo la función máximo vista en clase
maximo x y | x >= y = x
           | otherwise = y

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | maximo x y >= z = maximo x y
              | otherwise = z

--d)
algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y = (x == 0.0) || (y == 0.0)

algunoEsCero_pm :: Float -> Float -> Bool
algunoEsCero_pm 0 _ = True
algunoEsCero_pm _ 0 = True
algunoEsCero_pm x y = False

--e)
ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y = (x == 0.0) && (y == 0.0)

ambosSonCero_pm :: Float -> Float -> Bool
ambosSonCero_pm 0 0 = True
ambosSonCero_pm x y = False

--f)
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y = (x <= 3 && y <= 3) || ((x > 3 && x <= 7) && (y > 3 && y <= 7)) || (x > 7 && y > 7)

--g)
--primero me armo una función que me diga si dos números son iguales
sonIguales :: Integer -> Integer -> Bool
sonIguales x y = x == y

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | (sonIguales x y) && (sonIguales x z) && (sonIguales y z) = x 
                    | ((sonIguales x y) || (sonIguales x z)) && not(sonIguales y z) = y+z
                    | (sonIguales y z) && not(sonIguales x z) = x+z
                    | otherwise = x+y+z

--h)
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0

--i)
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

--j)
digitoDecenas :: Integer -> Integer
digitoDecenas x = mod(div x 10) 10

--Ejercicio 3.
cumpleLaEcuacion :: Integer -> Integer -> Integer -> Bool
cumpleLaEcuacion a b k = ((a*a + a*b*k) == 0) && (k /= 0)

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = (mod (-a) b == 0) && cumpleLaEcuacion a b (div (-a) (b))

--Ejercicio 4.

--a)
productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (x, y) (v, w) = x*v + y*w

--b)
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (x, y) (v, w) = (x < v) && (y < w)

--c)
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x, y) (v, w) = sqrt(((v - x)^2) + ((w - y)^2)) 

--d)
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z

--e)
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) w | (mod x w == 0) && (mod y w == 0) && (mod z w == 0) = x+y+z
                               | (mod x w == 0) && (mod y w == 0) = x + y
                               | (mod x w == 0) && (mod z w == 0) = x + z
                               | (mod y w == 0) && (mod z w == 0) = y + z
                               | (mod x w == 0) = x
                               | (mod y w == 0) = y
                               | (mod z w == 0) = z
                               | otherwise = 0

--f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | mod x 2 == 0 = 0
                       | mod y 2 == 0 = 1
                       | mod z 2 == 0 = 2
                       | otherwise = 4

--g)
crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

--h)
invertir :: (a, b) -> (b, a)
invertir (x, y) = (y, x)

--i)
type Punto2D = (Float, Float)

prodInterno :: Punto2D -> Punto2D -> Float
prodInterno (x, y) (v, w) = x*v + y*w

parMenor :: Punto2D -> Punto2D -> Bool
parMenor (x, y) (v, w) = (x < v) && (y < w)

dist :: Punto2D -> Punto2D -> Float
dist (x, y) (v, w) = sqrt(((v - x)^2) + ((w - y)^2))

--Ejercicio 5.
f_ej5 :: Integer -> Integer
f_ej5 x | x <= 7 = x*x 
        | otherwise = (2*x) - 1

g_ej5 :: Integer -> Integer
g_ej5 x | mod x 2 == 0 = div x 2
        | otherwise = (3*x) + 1

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (a, b, c) = (f_ej5(a) > g_ej5(a)) && (f_ej5(b) > g_ej5(b)) && (f_ej5(c) > g_ej5(c))

--Ejercicio 6.
type Anio = Integer
type EsBisiesto = Bool
bisiesto :: Anio -> EsBisiesto
bisiesto x | not(esMultiploDe x 4) = False
           | (esMultiploDe x 100) && not(esMultiploDe x 400) = False
           | otherwise = True

--Ejercicio 7.
--a)
--Implemento de nuevo la función absoluto, solo que esta vez recibe un número de punto flotante.
abs_float :: Float -> Float
abs_float n | n >= 0 = n
            | otherwise = (-1)*n

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a, b, c) (x, y, z) = abs_float(a-x) + abs_float(b-y) + abs_float(c-z)

--b)
type Punto3D = (Float, Float, Float)
distManhattan :: Punto3D -> Punto3D -> Float
distManhattan (a, b, c) (x, y, z) = abs_float(a-x) + abs_float(b-y) + abs_float(c-z)

--Ejercicio 8.
comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
             | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
             | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod (absoluto(x)) 10 + mod ((div(absoluto(x))10)) 10


--Ejercicio 9
--a)
--Dado un número real, si es 0 devuelve 1, y si no lo es devuelve 0
{--
problema f1 (n: R) : R {
    requiere {True}
    asegura {(n = 0 -> res = 1) ∧ (n ̸= 0 -> res = 0)}
}
--}

--b)
--Defino por extensión la función f2 de la siguiente manera:
--          f2(1) = 15
--          f2(-1) = -15
{--
problema f2 (n: R) : R {
    requiere {(n = 1 ∨ n = -1)}
    asegura {(n = 1 -> res = 15) ∧ (n = -1 -> res = -15)}
}    
--}

--c)
--Dado un número real, si este es menor o igual a 9, devuelve el número 7; y si es mayor o igual a 3 devuelve el 5
{--
problema f3 (n: R) : R {
    requiere {True}
    asegura {(n <= 9 -> res = 7) ∧ (n >= 3 -> res = 5) }
}
--}

--d)
--Dados dos números reales, calcula el promedio entre ambos.
{--
problema f4 (x: R, y: R) : R {
    requiere {True}
    asegura {res = (x+y)/2}
}
--}

--e)
--Dada una tupla de R, calcula el promedio de las coordenadas de la tupla.
{--
problema f5 (v: R × R) : R {
    requiere {True}
    asegura {res = (v0 + v1)/2}
}
--}

--f) 
--Dado un número real y un número entero, redondea para abajo el número real y decide si este número es igual al entero pasado por parámetro
{--
problema f6 (x: R, y: Z) : Bool {
    requiere {True}
    asegura {(res = true) <-> (el resultado de redondear para abajox tiene que ser igual a y)}
}
--}