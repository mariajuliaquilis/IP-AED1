module Parcial where 

type Libro = (String, String, String)
type Genero = String
type Prestamo = (Libro, Int, Int)

{-Enunciado: Sistema de Gestión de Biblioteca
Una biblioteca necesita un sistema para gestionar préstamos de libros. Cada libro se representa como una tupla (Título, Autor, Género), donde:
    Título y Autor son String
    Género es un tipo String: "Novela" | "Ciencia" | "Infantil" | "Historia" | etc
Los préstamos se modelan como una lista de tuplas (Libro, FechaPréstamo, FechaDevolución) donde las fechas son enteros (días desde una fecha
base).
-}

{-
Ejercicio 1 (2 puntos)
problema librosPorGenero (libros: seq⟨Libro⟩, genero: Genero) : seq⟨Libro⟩ {
  requiere: {True}
  asegura: {res contiene exactamente los libros de género especificado}
  asegura: {El orden relativo de los libros se mantiene}
}
Ejemplo
librosPorGenero [("1984", "Orwell", "Novela"), ("Breve historia del tiempo", "Hawking", "Ciencia"), 
                 ("El Principito", "Saint-Exupéry", Infantil)] "Ciencia"
Resultado: [("Breve historia del tiempo", "Hawking", "Ciencia")]
-}

longitud :: (Eq t) => [t] -> Int
longitud libros | libros == [] = 0
                | otherwise = 1 + longitud(tail libros)

terceraCoordenada :: (String, String, String) -> String
terceraCoordenada (x,y,z) = z

librosPorGenero :: [Libro] -> Genero -> [Libro]
librosPorGenero libros genero | longitud(libros) == 0 = []
                              | terceraCoordenada(head libros) == genero = (head libros):librosPorGenero (tail libros) genero
                              | otherwise = librosPorGenero (tail libros) genero

{-Ejercicio 2 (2 puntos)
problema prestamosVencidos (prestamos: seq⟨Prestamo⟩, hoy: Z) : seq⟨Libro⟩ {
  requiere: {hoy ≥ 0}
  requiere: {Para todo préstamo, fechaPréstamo ≤ fechaDevolución}
  asegura: {res contiene los libros con fechaDevolución < hoy}
  asegura: {Sin duplicados}
}
Ejemplo
libro1 = ("1984", "Orwell", "Novela")
libro2 = ("El Principito", "Saint-Exupéry", "Infantil")

prestamos = [(libro1, 10, 20), (libro2, 15, 25), (libro1, 30, 40)]
prestamosVencidos prestamos 35

Resultado: [("1984", "Orwell", "Novela"), ("El Principito", "Saint-Exupéry", "Infantil")]
-}

primeraCoordenadaPrestamo :: (Libro, Int, Int) -> Libro
primeraCoordenadaPrestamo (x,y,z) = x

terceraCoordenadaPrestamo :: (Libro, Int, Int) -> Int
terceraCoordenadaPrestamo (x,y,z) = z 

prestamosVencidos :: [Prestamo] -> Int -> [Libro]
prestamosVencidos prestamos hoy | longitud(prestamos) == 0 = []
                                | terceraCoordenadaPrestamo(head prestamos) < hoy = primeraCoordenadaPrestamo(head prestamos):prestamosVencidos (tail prestamos) hoy 
                                | otherwise = prestamosVencidos (tail prestamos) hoy
{-Ejercicio 3 (3 puntos)
problema generoMasPrestado (prestamos: seq⟨Prestamo⟩) : Genero {
  requiere: {|prestamos| > 0}
  asegura: {res es el género con más préstamos}
  asegura: {En empate, devuelve cualquiera de los géneros con máxima frecuencia}
}
Ejemplo
prestamos = [
  (("1984", "Orwell", "Novela"), 1, 5),
  (("Breve historia del tiempo", "Hawking", "Ciencia"), 2, 6),
  (("El Principito", "Saint-Exupéry", "Infantil"), 3, 7),
  (("1984", "Orwell", "Novela"), 4, 8)
]
generoMasPrestado prestamos
Resultado: "Novela" (porque aparece 2 veces)
-}

--Los préstamos se modelan como una lista de tuplas (Libro, FechaPréstamo, FechaDevolución) donde las fechas son enteros (días desde una fecha
--base).

cantApariciones :: [Genero] -> Genero -> Int
cantApariciones generos genero | longitud(generos) == 0 = 0
                               | head(generos) == genero = 1 + cantApariciones (tail generos) genero
                               | otherwise = cantApariciones (tail generos) genero

listaDeGeneros :: [Prestamo] -> [Genero]
listaDeGeneros prestamos| longitud(prestamos) == 0 = []
                        | otherwise = terceraCoordenada(primeraCoordenadaPrestamo(head prestamos)):listaDeGeneros(tail prestamos)

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece lista elemento | longitud(lista) == 0 = False
                         | otherwise = head(lista) == elemento || pertenece (tail lista) elemento

elMasPrestado :: [Genero] -> Genero -> [Genero] -> Genero
elMasPrestado generos genero lista | longitud(generos) == 0 = genero
                                   | cantApariciones generos (head generos) > cantApariciones generos genero && not(pertenece lista genero) = elMasPrestado (tail generos) (head generos) ((head generos):lista) 
                                   | otherwise = elMasPrestado (tail generos) genero lista 

generoMasPrestado :: [Prestamo] -> Genero
generoMasPrestado prestamos = elMasPrestado (listaDeGeneros prestamos) (terceraCoordenada(primeraCoordenadaPrestamo(head prestamos))) []


{-Ejercicio 4 (3 puntos)
problema consolidarPrestamos (prestamos: seq⟨Prestamo⟩) : seq⟨(Libro, Z)⟩ {
  requiere: {True}
  asegura: {Cada libro aparece una vez en res}
  asegura: {Para cada libro, el número asociado es la cantidad de veces que fue prestado}
}

Ejemplo
prestamos = [
  (("1984", "Orwell", "Novela"), 1, 5),
  (("El Principito", "Saint-Exupéry", "Infantil"), 3, 7),
  (("1984", "Orwell", "Novela"), 4, 8)
]
consolidarPrestamos prestamos
Resultado: [(("1984", "Orwell", "Novela"), 2), (("El Principito", "Saint-Exupéry", "Infantil"), 1)]
-}
cantVecesQueFuePrestado :: [Libro] -> Libro -> Int
cantVecesQueFuePrestado libros libro | longitud(libros) == 0 = 0
                                     | (head libros) == libro = 1 + cantVecesQueFuePrestado (tail libros) libro
                                     | otherwise = cantVecesQueFuePrestado (tail libros) libro

listaDeLibros :: [Prestamo] -> [Libro]
listaDeLibros prestamos | longitud(prestamos) == 0 = []
                        | otherwise = primeraCoordenadaPrestamo(head prestamos):listaDeLibros (tail prestamos)

consolidoPrestamo :: [Libro] -> [Libro] -> [(Libro, Int)]
consolidoPrestamo libros lista | longitud(libros) == 0 = []
                               | not(pertenece lista (head libros)) = ((head libros), cantVecesQueFuePrestado libros (head libros)):consolidoPrestamo (tail libros) ((head libros):lista)
                               | otherwise = consolidoPrestamo (tail libros) lista

consolidarPrestamos :: [Prestamo] -> [(Libro, Int)]
consolidarPrestamos prestamos = consolidoPrestamo (listaDeLibros(prestamos)) [] 