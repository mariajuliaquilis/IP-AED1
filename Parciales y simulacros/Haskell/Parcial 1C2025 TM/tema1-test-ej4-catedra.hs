import Parcial
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "Columna sin pares" ~: cantidadParesColumna [[1, 3], [5, 7], [9, 11]] 1 ~?= 0,
    "Columna con algunos pares" ~: cantidadParesColumna [[1, 2], [4, 5], [7, 8]] 2 ~?= 2,
    "Columna con todos pares" ~: cantidadParesColumna [[2, 4], [6, 8], [10, 12]] 1 ~?= 3,
    "Columna 1 con un solo elemento par" ~: cantidadParesColumna [[2]] 1 ~?= 1,
    "Columna 1 con un solo elemento impar" ~: cantidadParesColumna [[3]] 1 ~?= 0,
    "Columna 2 con un solo elemento par" ~: cantidadParesColumna [[1,4]] 2 ~?= 1,
    "Columna 2 con un solo elemento impar" ~: cantidadParesColumna [[1,3]] 2 ~?= 0,
    "Columna con pares e impares alternados" ~: cantidadParesColumna [[2,3],[3,4],[4,5],[5,6]] 1 ~?= 2,
    "Columna con todos impares" ~: cantidadParesColumna [[1,3,5],[7,9,11],[13,15,17]] 3 ~?= 0,
    "Columna con todos pares" ~: cantidadParesColumna [[2,4,6],[8,10,12],[14,16,18]] 2 ~?= 3,
    "Columna 1 en matriz rectangular" ~: cantidadParesColumna [[2,3,4],[4,5,6],[6,7,8],[8,9,10]] 1 ~?= 4,
    "Columna 3 en matriz rectangular" ~: cantidadParesColumna [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] 3 ~?= 2,
    "Columna 1 con valores negativos" ~: cantidadParesColumna [[-2,3],[4,5],[-6,7]] 1 ~?= 3,
    "Columna 3 con todos valores negativos" ~: cantidadParesColumna [[-2,3,-1872],[4,5,-8],[-6,7,-1]] 3 ~?= 2,
    "Columna 2 con ceros" ~: cantidadParesColumna [[1,0],[2,0],[3,0]] 2 ~?= 3
    ]
