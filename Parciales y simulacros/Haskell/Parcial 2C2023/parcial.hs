{-
2023 Segundo Cuatrimestre

¡Vamos Campeones!
En exactas se está jugando un torneo de fútbol y la facultad le pidió a los alumnos de IP programar algunas funcionalidades en Haskell. 
Los datos con los que contamos para esto son los nombres de los equipos que participan del torneo, los nombres de los arqueros titulares
de cada uno de dichos equipos, y la cantidad de goles recibidos por esos arqueros. 
Los nombres de los equipos y sus respectivos arqueros serán modelados mediante tuplas de tipo (String, String), donde la primera 
componente representa el nombre del equipo, y la segunda representa el nombre del arquero titular de dicho equipo.
En los problemas en los cuales se reciben como parámetros secuencias arquerosPorEquipo y goles, cada posición de la lista goles representará 
la cantidad de goles recibidos por el arquero del equipo que se encuentra en esa misma posicion de arquerosPorEquipo. 
Por ejemplo, si la lista arquerosPorEquipo es [("Sacachispas", "Neyder Aragon"), ("Fenix", "Nahuel Galardi")]  y la lista de goles [3, 5], 
eso indicaría que Neyder Aragon recibió 3 goles, y Nahuel Galardi 5.

Se pueden usar las siguientes funciones del preludio:
	- Listas: head, tail, last, init, length, elem, ++
	- Tuplas: fst, snd
	- Operaciones Lógicas: &&, ||, not
	- Constructores de listas: (x:xs), []
	- Constructores de tuplas: (x, y)
-}

{-
1) Atajaron Suplentes
problema atajaronSuplentes (arquerosPorEquipo: seq<String X String>, goles: seq<Z>, totalGolesTorneo: Z): Z {
	requiere: {equiposValidos(arquerosPorEquipo)
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {La suma de todos los elementos de goles es menor o igual a totalGolesTorneo}
	asegura: {res es la cantidad de goles recibidos en el torneo por arqueros que no son titulares en sus equipos}
}
-}
longitud :: (Eq t) => [t] -> Int
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista)

sumoGoles :: [Int] -> Int
sumoGoles goles | longitud(goles) == 0 = 0
                | otherwise = (head goles) + sumoGoles(tail goles)

atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes arquerosPorEquipo goles totalGolesTorneo = totalGolesTorneo - sumoGoles(goles)

{-
2) Equipos Válidos
problema equiposValidos (arquerosPorEquipo: seq<String X String>): Bool {
	requiere: {True}
	asegura: {
	(res = True) <=> arquerosPorEquipo no contiene nombres de clubes repetidos, ni arqueros repetidos, ni jugadores con nombre del club
	}
}
-}
extraigoClubes :: [(String, String)] -> [String]
extraigoClubes arquerosPorEquipo | longitud(arquerosPorEquipo) == 0 = []
                                 | otherwise = fst(head arquerosPorEquipo):(extraigoClubes (tail arquerosPorEquipo))  

extraigoNombres :: [(String, String)] -> [String]
extraigoNombres arquerosPorEquipo | longitud(arquerosPorEquipo) == 0 = []
                                  | otherwise = snd(head arquerosPorEquipo):(extraigoNombres(tail arquerosPorEquipo))

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = head(lista) == elemento || pertenece (tail lista) elemento

noContieneNombresClubesRepetidos :: [String] -> Bool
noContieneNombresClubesRepetidos clubes | longitud(clubes) == 0 = True
                                        | otherwise = not(pertenece (tail clubes) (head clubes)) && noContieneNombresClubesRepetidos (tail clubes) 

noContieneNombresArquerosRepetidos :: [String] -> Bool
noContieneNombresArquerosRepetidos arqueros | longitud(arqueros) == 0 = True
                                            | otherwise = not(pertenece (tail arqueros) (head arqueros)) && noContieneNombresArquerosRepetidos (tail arqueros) 

noHayJugadoresConNombreDelClub :: [String] -> [String] -> Bool
noHayJugadoresConNombreDelClub clubes arqueros | longitud(clubes) == 0 = True
                                               | otherwise = not(pertenece arqueros (head clubes)) && noHayJugadoresConNombreDelClub (tail clubes) arqueros

equiposValidos :: [(String, String)] -> Bool
equiposValidos arquerosPorEquipo = noContieneNombresClubesRepetidos(extraigoClubes(arquerosPorEquipo)) &&
                                   noContieneNombresArquerosRepetidos(extraigoNombres(arquerosPorEquipo)) &&
                                   noHayJugadoresConNombreDelClub (extraigoClubes(arquerosPorEquipo)) (extraigoNombres(arquerosPorEquipo)) 

{-
3) Porcentaje de goles
problema porcentajeDeGoles (arquero: String, arquerosPorEquipo: seq<String X String>, goles: seq<Z>): R {
	requiere: {La segunda componente de algún elemento de arquerosPorEquipo es arquero}
	requiere: {equiposValidos(arquerosPorEquipo)}
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {Hay al menos un elemento de goles mayores estricto a 0}
	asegura: {res es el porcentaje de goles que recibió arquero sobre el total de goles recibidos por arqueros titulares}
}
Para resolver este ejercicio pueden utilizar la siguiente función que devuelve como float la división entre dos
numeros de tipo Int.

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b
-}
golesQueRecibioElArquero :: String -> [(String, String)] -> [Int] -> Int
golesQueRecibioElArquero arquero arquerosPorEquipo goles | snd(head(arquerosPorEquipo)) == arquero = head(goles)
                                                         | otherwise = golesQueRecibioElArquero arquero (tail(arquerosPorEquipo)) (tail(goles))

porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles arquero arquerosPorEquipo goles = fromIntegral(golesQueRecibioElArquero arquero arquerosPorEquipo goles)/fromIntegral(sumoGoles(goles))

{-
4) Valla Menos Vencida
problema vallaMenosVencida (arquerosPorEquipo: seq<String X String>, goles: seq<Z>): String {
	requiere: {equiposValidos(arquerosPorEquipo)}
	requiere: {|arquerosPorEquipo| = |goles|}
	requiere: {Todos los elementos de goles son mayores o iguales a 0}
	requiere: {|goles| > 0}
	asegura: {res es alguno de los arqueros de arquerosPorEquipo que menor goles recibió de acuerdo a goles}
}
-}
menorCantGoles :: [Int] -> Int -> Int
menorCantGoles goles minimaCant | longitud(goles) == 0 = minimaCant
                                | head(goles) < minimaCant = menorCantGoles (tail goles) (head(goles))
                                | otherwise = menorCantGoles (tail goles) minimaCant

arqueroQueRecibioMenosGoles :: [(String, String)] -> [Int] -> String -> String
arqueroQueRecibioMenosGoles arquerosPorEquipo goles arquero | menorCantGoles goles (head goles) == (head goles) = (snd(head(arquerosPorEquipo)))
                                                            | otherwise = arqueroQueRecibioMenosGoles (tail(arquerosPorEquipo)) (tail(goles)) arquero

vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida arquerosPorEquipo goles = arqueroQueRecibioMenosGoles arquerosPorEquipo goles arquero
                                          where arquero = snd(head(arquerosPorEquipo))