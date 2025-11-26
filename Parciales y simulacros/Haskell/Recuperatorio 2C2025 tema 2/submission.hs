module SolucionT2 where

-- Ejercicio 1
longitud :: (Eq t) => [t] -> Int
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista) 

listaDeNumeros :: Int -> Int -> [Int]
listaDeNumeros desde hasta | desde == hasta = []
                           | otherwise = desde:listaDeNumeros (desde+1) hasta 

listaDeDivisores :: Int -> [Int] -> [Int]
listaDeDivisores numero lista | longitud(lista) == 0 = []
                              | mod numero (head lista) == 0 = (head lista):listaDeDivisores numero (tail lista)
                              | otherwise = listaDeDivisores numero (tail lista)  

divisoresPropios :: Int -> [Int]
divisoresPropios numero = listaDeDivisores numero (listaDeNumeros 1 numero)

-- Ejercicio 2
primeraCoordenada :: (String,String,Int,Int) -> String
primeraCoordenada (x,y,z,w) = x

terceraCoordenada :: (String,String,Int,Int) -> Int
terceraCoordenada (x,y,z,w) = z 

cuartaCoordenada :: (String,String,Int,Int) -> Int 
cuartaCoordenada (x,y,z,w) = w

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = (head lista) == elemento || pertenece (tail lista) elemento

listaHorarios :: Int -> Int -> [Int]
listaHorarios desde hasta | desde > hasta = []
                          | otherwise = desde:listaHorarios (desde+1) hasta  

horarioEstaEnListaHorarios :: (String,String,Int,Int) -> Int -> Int -> Bool
horarioEstaEnListaHorarios materia inicio fin = (pertenece (listaHorarios inicio fin) (terceraCoordenada(materia)) && pertenece (listaHorarios inicio fin) (cuartaCoordenada(materia))) ||
                                                (pertenece (listaHorarios (terceraCoordenada(materia)) (cuartaCoordenada(materia))) inicio && pertenece (listaHorarios (terceraCoordenada(materia)) (cuartaCoordenada(materia))) fin)

listaMateriasQueSeCursanEnUnTurno :: [(String,String,Int,Int)] -> Int -> Int -> [String]
listaMateriasQueSeCursanEnUnTurno lista desde hasta | longitud(lista) == 0 = []
                                                    | horarioEstaEnListaHorarios (head(lista)) desde hasta = (primeraCoordenada(head lista)):(listaMateriasQueSeCursanEnUnTurno (tail lista) desde hasta) 
                                                    | otherwise = listaMateriasQueSeCursanEnUnTurno (tail lista) desde hasta

materiasComisionN :: [(String,String,Int,Int)] -> Int -> Int -> [String]
materiasComisionN lista inicio fin = listaMateriasQueSeCursanEnUnTurno lista inicio fin

-- Ejercicio 3
sumoNotas :: [Int] -> Int
sumoNotas lista | longitud(lista) == 0 = 0
                | otherwise = (head lista) + sumoNotas(tail lista)

cantidadDeNotas :: [Int] -> Int
cantidadDeNotas lista | longitud(lista) == 0 = 0
                      | otherwise = 1 + cantidadDeNotas(tail lista)

promedioPorAlumno :: [Int] -> Float
promedioPorAlumno lista = (fromIntegral(sumoNotas(lista)))/(fromIntegral(cantidadDeNotas(lista)))

promedioMasAlto :: [(String, [Int])] -> String -> Float -> String
promedioMasAlto lista alumno promedio | longitud(lista) == 0 = alumno
                                      | promedioPorAlumno(snd(head lista)) > promedio = promedioMasAlto (tail lista) (fst(head lista)) (promedioPorAlumno(snd(head lista)))
                                      | otherwise = promedioMasAlto (tail lista) alumno promedio

mejorPromedio :: [(String, [Int])] -> String
mejorPromedio lista = promedioMasAlto lista (fst(head lista)) (promedioPorAlumno (snd(head lista)))

-- Ejercicio 4
listaCaracteresQueAparecenEnS1 :: String -> String -> String
listaCaracteresQueAparecenEnS1 s1 s2 | longitud(s2) == 0 = ""
                                     | pertenece s1 (head(s2)) = (head s2):listaCaracteresQueAparecenEnS1 s1 (tail s2)
                                     | otherwise = listaCaracteresQueAparecenEnS1 s1 (tail s2)

listaCaracteresQueAparecenEnS2 :: String -> String -> String
listaCaracteresQueAparecenEnS2 s1 s2 | longitud(s1) == 0 = ""
                                     | pertenece s2 (head(s1)) = (head s1):listaCaracteresQueAparecenEnS2 (tail s1) s2
                                     | otherwise = listaCaracteresQueAparecenEnS2 (tail s1) s2

palabrasEnComun :: String -> String -> String
palabrasEnComun palabra1 palabra2 | longitud(palabra1) == 0 = ""
                                  | pertenece (palabra2) (head(palabra1)) = (head(palabra1)):palabrasEnComun (tail palabra1) palabra2
                                  | otherwise = palabrasEnComun (tail palabra1) palabra2  

sinRepetidos :: String -> String -> String
sinRepetidos palabra lista | longitud(palabra) == 0 = ""
                           | not(pertenece (lista) (head palabra)) = (head palabra):(sinRepetidos (tail palabra) ((head palabra):lista))
                           | otherwise = sinRepetidos (tail palabra) (lista)

caracteresEnComun :: String -> String -> String
caracteresEnComun s1 s2 = sinRepetidos (palabrasEnComun (listaCaracteresQueAparecenEnS1 s1 s2) (listaCaracteresQueAparecenEnS2 s1 s2)) ""