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
                 | mod (head s) n == 0 = (head s):(multiplosDeN n (tail s))
                 | otherwise = multiplosDeN n (quitarTodos (head s) s)

--item 9)
ordenar :: [Integer] -> [Integer]
ordenar s | longitud(s) == 0 = s 
          | otherwise = (ordenar(quitarTodos(maximo s) s))++[maximo s]

--Ejercicio 5:

--item 1)
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada s | longitud(s) == 1 = s 
                | otherwise = (head s):sumaAcumulada((head s + (head(tail s))):(tail(tail s)))

--item 2)
--Utilizo las funciones de la práctica 4
minimoDivisorDeN :: Integer -> Integer -> Integer
minimoDivisorDeN n i | mod n i == 0 = i --me quedo con el primer numero natural que divide
                     | otherwise = minimoDivisorDeN n (i+1) --pruebo con el siguiente natural

menorDivisor :: Integer -> Integer
menorDivisor 1 = 1
menorDivisor n = minimoDivisorDeN n 2

esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = (n == menorDivisor n)

listaDePrimosHasta :: Integer -> Integer -> [Integer] --asumo que d >= 2
listaDePrimosHasta d h | d > h = []
                       | esPrimo(d) = d:(listaDePrimosHasta (d+1) h) 
                       | otherwise = listaDePrimosHasta (d+1) h

listaDeDivisoresPrimosDeN :: Integer -> [Integer] -> [Integer]
listaDeDivisoresPrimosDeN n s | longitud(s) == 0 = s 
                              | mod n (head s) == 0 = (head s):(listaDeDivisoresPrimosDeN (div n (head s)) s)
                              | otherwise = listaDeDivisoresPrimosDeN n (tail s)

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos s | longitud(s) == 1 = [listaDeDivisoresPrimosDeN (head s) (listaDePrimosHasta (menorDivisor (head s)) (head s))]
                      | otherwise = [listaDeDivisoresPrimosDeN (head s) (listaDePrimosHasta (menorDivisor (head s)) (head s))]++(descomponerEnPrimos (tail s))

--Ejercicio 6:
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

--implemento la sugerencia:
elNombre :: Contacto -> Nombre
elNombre c = fst(c)

elTelefono :: Contacto -> Telefono
elTelefono c = snd(c)

--item a)
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos n c | c == [] = False
                   | otherwise = n == elNombre(head(c)) || enLosContactos n (tail c)

--item b)
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto t c | not(enLosContactos (elNombre t) c) = t:c 
                    | elNombre t == elNombre(head c) = (elNombre t, elTelefono t):(eliminarContacto (elNombre t) c)  
                    | otherwise = (head c):(agregarContacto t (tail c))  
--item c)
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto n c | not(enLosContactos n c) = c 
                     | n == elNombre(head c) = (tail c)
                     | otherwise = (head c):(eliminarContacto n (tail c))

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
           