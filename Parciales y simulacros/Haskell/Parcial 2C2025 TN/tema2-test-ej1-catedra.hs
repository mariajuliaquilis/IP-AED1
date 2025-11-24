import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    " Rango tam 1 primo" ~: mayorNumeroConNDivisores 5 5 2 ~?= 5,
    " Un solo resultado" ~: mayorNumeroConNDivisores 1 9 4 ~?= 8,
    " Varios resultados, elige el mayor empieza en 1" ~: mayorNumeroConNDivisores 1 15 6 ~?= 12,
    -- Caso con números primos
    "Caso primo mayor" ~: mayorNumeroConNDivisores 10 20 2 ~?= 19,
    -- Caso con número perfecto (6 tiene 4 divisores: 1,2,3,6, 10 tiene 4 div 1 2 5 10)
    "Varios resultados, elige el mayor no empieza en 1" ~: mayorNumeroConNDivisores 4 10 4 ~?= 10,
    "tamaño 1 no es primo" ~: mayorNumeroConNDivisores 12 12 6 ~?= 12,
    -- Caso con múltiples opciones (debe devolver el mayor 9) 4 9
    "Múltiples opciones: mayorNumeroConNDivisores 1 10 3" ~: mayorNumeroConNDivisores 4 9 3 ~?= 9,  
    -- Caso extremo: número con muchos divisores 60, 72, 84, 90, 96 tienen 12 divisores, debe devolver 96
    "Caso extremo: número con muchos divisores" ~: mayorNumeroConNDivisores 60 100 12 ~?= 96
    ]
