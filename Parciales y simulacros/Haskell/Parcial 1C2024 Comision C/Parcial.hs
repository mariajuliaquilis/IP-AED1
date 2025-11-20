module Parcial where
{-
La Unidad de Tecnologías de la Información (UTI) de nuestra Facultad nos ha encargado que desarrollemos un nuevo sistema para el registro 
de alumnos. En este sistema se guarda la información de cada alumno, que está representada como una tupla de dos elementos: el primero es 
el nombre completo del alumno y el segundo una lista con las notas de los finales que rindió.
Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo enteramente en Haskell,
utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras 
de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1 (2 puntos)
problema aproboMasDeNMaterias (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, alumno:seq⟨Char⟩, n: Z) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {n > 0}
  requiere: {El alumno se encuentra en el registro }
  asegura: {res = true <=> el alumno tiene más de n notas de finales mayores o iguales a 4 en el registro}
}
-}
longitud :: (Eq t) => [t] -> Int
longitud lista | lista == [] = 0
               | otherwise = 1 + longitud(tail lista) 

finalesRendidosPorElAlumno :: String -> [(String, [Int])] -> [Int]
finalesRendidosPorElAlumno alumno registro | longitud(registro) == 0 = []
                                           | fst(head registro) == alumno = snd(head registro) 
                                           | otherwise = finalesRendidosPorElAlumno alumno (tail registro) 

cantFinalesAprobados :: [Int] -> Int
cantFinalesAprobados finales | longitud(finales) == 0 = 0
                             | (head finales) >= 4 = 1 + cantFinalesAprobados(tail finales)
                             | otherwise = cantFinalesAprobados (tail finales)

aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias registro alumno n = cantFinalesAprobados(finalesRendidosPorElAlumno alumno registro) > n

{-Ejercicio 2 (2 puntos)
problema buenosAlumnos (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨seq⟨Char⟩⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  asegura: {res es la lista de los nombres de los alumnos que están en registro cuyo promedio de notas es mayor o igual a 8 y no tiene 
            aplazos (notas menores que 4)}
}
Para resolver el promedio pueden utilizar la función del Preludio de Haskell fromIntegral que dado un valor de tipo Int devuelve su 
equivalente de tipo Float.
-}
noTieneAplazos :: [Int] -> Bool
noTieneAplazos finales | longitud(finales) == 0 = True 
                       | otherwise = (head finales) >= 4 && noTieneAplazos(tail finales)

sumoNotas :: [Int] -> Int
sumoNotas finales | longitud(finales) == 0 = 0
                  | otherwise = (head finales) + sumoNotas(tail finales)

promedio :: [Int] -> Float
promedio finales = fromIntegral(sumoNotas finales)/fromIntegral(longitud finales)

buenosAlumnos :: [(String, [Int])] -> [String]
buenosAlumnos registro | longitud(registro) == 0 = []
                       | promedio(snd(head registro)) >= 8 && noTieneAplazos(snd(head registro)) = fst(head registro):buenosAlumnos(tail registro)
                       | otherwise = buenosAlumnos(tail registro)

{-Ejercicio 3 (2 puntos)
problema mejorPromedio (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩) : seq⟨Char⟩ {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {|registro| > 0 }
  asegura: {res es el nombre del alumno cuyo promedio de notas es el más alto; si hay más de un alumno con el mismo promedio de notas, 
            devuelve el nombre de alumno que aparece primero en registro}
}
-}
promedioMasAlto :: [(String, [Int])] -> (String, [Int]) -> String
promedioMasAlto registro alumno | longitud(registro) == 0 = fst(alumno)
                                | promedio(snd(head registro)) > promedio(snd(alumno)) = promedioMasAlto (tail registro) (head registro)
                                | otherwise = promedioMasAlto (tail registro) alumno

mejorPromedio :: [(String, [Int])] -> String
mejorPromedio registro = promedioMasAlto registro (head registro)

{-Ejercicio 4 (3 puntos)
problema seGraduoConHonores (registro: seq⟨seq⟨Char⟩ x seq⟨Z⟩⟩, cantidadDeMateriasDeLaCarrera: Z, alumno: seq⟨Char⟩ ) : Bool {
  requiere: {No hay nombres de alumnos repetidos en registro}
  requiere: {Las notas de registro son todas iguales o mayores a cero y menores o iguales a 10}
  requiere: {cantidadDeMateriasDeLaCarrera > 0}
  requiere: {El alumno se encuentra en el registro }
  requiere: {|buenosAlumnos(registro)| > 0}
  asegura: {res <=> true si aproboMasDeNMaterias(registro, alumno, cantidadDeMateriasDeLaCarrera-1) = true y alumno pertenece 
            al conjunto de buenosAlumnos(registro) y el promedio de notas de finales de alumno está a menos (estrictamente) de
            1 punto del mejorPromedio(registro)}
}
-}
pertenece :: [String] -> String -> Bool
pertenece alumnos alumno | longitud(alumnos) == 0 = False 
                         | otherwise = (head alumnos) == alumno || pertenece (tail alumnos) alumno

halloElMejorPromedio :: [(String, [Int])] -> Float
halloElMejorPromedio registro = promedio(finalesRendidosPorElAlumno (mejorPromedio registro) registro)

seGraduoConHonores :: [(String, [Int])] -> Int -> String -> Bool
seGraduoConHonores registro cantidadDeMateriasDeLaCarrera alumno = (aproboMasDeNMaterias registro alumno (cantidadDeMateriasDeLaCarrera-1)) &&
                                                                   (pertenece (buenosAlumnos(registro)) alumno) &&
                                                                   (halloElMejorPromedio(registro) - promedio(finalesRendidosPorElAlumno alumno registro)) < 1

{-Ejercicio 5 (1 punto)
Conteste marcando la opción correcta. El Testing es una técnica de verificación que sirve para:

1) Demostrar que un programa es correcto.
2) Probar propiedades de un programa.
3) Encontrar fallas en un programa.
-}

--Ejercicio 5) Encontrar fallas en un programa.