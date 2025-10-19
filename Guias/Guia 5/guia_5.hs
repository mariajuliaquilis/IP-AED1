--Ejercicio 1
--item 1)
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--item 2)
ultimo :: [t] -> t 
ultimo s | (longitud s == 1) = head(s)
         | otherwise =  ultimo(tail s)  

--item 3)
principio :: [t] -> [t]
principio s | (longitud s == 1) = []
            | otherwise = [head s] ++ principio(tail s)

--item 4)
reverso :: [t] -> [t]
reverso s | longitud s == 0 = s 
          | otherwise = [ultimo s] ++ reverso(principio s)

--Ejercicio 2
--item 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e (x:xs) = e == x || pertenece e xs

--item 2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales s | longitud s == 1 = True
               | otherwise = (head s == head(tail s)) && todosIguales (tail s)

--item 3)
cantidadDeApariciones :: (Eq t) => t -> [t] -> Integer 
cantidadDeApariciones e s | longitud s == 0 = 0
                          | (e == (head s)) = 1 + cantidadDeApariciones e (tail s)
                          | otherwise = cantidadDeApariciones e (tail s)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos s | longitud s == 1 = True
                 | otherwise = (cantidadDeApariciones (head s) s == 1) && todosDistintos(tail s)

--item 4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos s | longitud s == 1 = False
               | otherwise = (cantidadDeApariciones (head s) s >= 2) || hayRepetidos (tail s)

--item 5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar e s | ((not(pertenece e s)) || ((cantidadDeApariciones e s) == 1)) = s
           | (e == head(s)) = tail(s)
           | otherwise = [head s] ++ quitar e (tail s)

--item 6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e s | not(pertenece e s) = s
                | (e == head(s)) = quitarTodos e (tail s)
                | otherwise = [head s] ++ quitarTodos e (tail s)

--item 7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos s | longitud s == 0 = s 
                    |(cantidadDeApariciones (head s) s == 1) = [head s] ++ eliminarRepetidos (tail s)
                    | otherwise = [head s] ++ eliminarRepetidos(quitarTodos (head s) s)

--item 8)
elementosIguales :: (Eq t) => [t] -> [t] -> [t] -> Bool
elementosIguales s r l | longitud l == 0 && longitud r /= 0 = False
                       | longitud s == 0 = True
                       | otherwise = (longitud(eliminarRepetidos l) == longitud(eliminarRepetidos r)) && pertenece (head s) (eliminarRepetidos r) && elementosIguales (tail s) r l

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r = elementosIguales s r s 

--item 9)
capicua :: (Eq t) => [t] -> Bool
capicua s = s == reverso(s)

--Ejercicio 3
--item 1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--item 2)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

--item 3)
masGrande :: [Integer] -> Integer -> Integer
masGrande s e | longitud(s) == 1 = e 
              | head(s) > head(tail s) = masGrande(quitarTodos(head(tail s)) s) (head s)
              | otherwise = masGrande (tail s) (head(tail s))
              
maximo :: [Integer] -> Integer
maximo s = masGrande s (head s)

--item 4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n []     = []
sumarN n (x:xs) = (n+x):(sumarN n xs)

--item 5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero s = sumarN (head s) s

--item 6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo s = sumarN (ultimo s) s

--item 7)
pares :: [Integer] -> [Integer]
pares s | longitud(s)    == 0 = s
        | mod (head s) 2 == 1 = pares(quitarTodos (head s) s)
        | otherwise           = (head s):pares(tail s)

--item 8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n s | longitud(s)    == 0 = s
                 | mod (head s) n == 1 = multiplosDeN n (quitarTodos (head s) s)
                 | otherwise = (head s):(multiplosDeN n (tail s))

--item 9)
ordenar :: [Integer] -> [Integer]
ordenar s | longitud(s) == 0 = s 
          | otherwise = (ordenar(quitarTodos(maximo s) s))++[maximo s]

--Ejercicio 6:
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

--Ejercicio 7:
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker] -- [Locker] = [(Identificacion, Estado)] = [(Identificacion, (Disponibilidad, Ubicacion))]
type Disponibilidad = Bool

--item 1)
existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker n m | m == [] = False
                   | otherwise = n == fst(head m) || existeElLocker n (tail m)     

--item 2)
ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker n m | n == fst(head m) = snd(snd(head m))
                       | otherwise = ubicacionDelLocker n (tail m)

--item 3)
estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker n m | n == fst(head m) = fst(snd(head m))
                           | otherwise = estaDisponibleElLocker n (tail m)

--item 4)
ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker n m | not(estaDisponibleElLocker n m) = m 
                 | n == fst(head m) = ocuparLocker n ((n, (False, snd(snd(head m)))):(tail(quitar(head m) m)))
                 | otherwise = (head m):ocuparLocker n (tail m)
   
           