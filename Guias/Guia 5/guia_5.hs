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