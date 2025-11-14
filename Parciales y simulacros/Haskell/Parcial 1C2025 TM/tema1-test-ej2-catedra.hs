import Parcial
import Test.HUnit
import Data.List(sort)

main = runTestTT allTests

allTests = test[
    "Lista vacía" ~: cursadasVencidas [] ~?= [],
    "Ninguna cursada vencida" ~: cursadasVencidas [("Álgebra", 2022, 1), ("Análisis", 2023, 2)] ~?= [],
    "Una vencida y otra no" ~: cursadasVencidas [("Álgebra", 2020, 2), ("Análisis", 2021, 2)] ~?= ["Álgebra"],
    "Todas las cursadas vencidas" ~: expectPermutacion (cursadasVencidas [("Álgebra", 2020, 2), ("Análisis", 2019, 1)])["Álgebra", "Análisis"],
    "Solo una cursada y no vencida" ~: cursadasVencidas [("Álgebra", 2022, 2)] ~?= [],
    "Solo una cursada y vencida" ~: cursadasVencidas [("Introducción a la Programación", 2020, 1)] ~?= ["Introducción a la Programación"],
    "Cursada en el limite no vencida" ~: cursadasVencidas [("Introducción a la Programación", 2021, 2)] ~?= [],
    "Cursada en el limite vencida" ~: cursadasVencidas [("Introducción a la Programación", 2021, 1)] ~?= ["Introducción a la Programación"],
    "Cursada de 1993" ~: cursadasVencidas [("Taller de Álgebra", 1993, 0)] ~?= ["Taller de Álgebra"],
    "Materias vencidas repetidas, devuelve sin repetidos" ~: cursadasVencidas [("M1", 2010, 1), ("M1", 2020, 1)] ~?= ["M1"]
    ]

-- ------------ FUNCIONES AUXILIARES ------------
-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)
expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)
