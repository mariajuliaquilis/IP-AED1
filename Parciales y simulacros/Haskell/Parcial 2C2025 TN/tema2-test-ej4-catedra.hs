import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
  -- Caso básico: una sola fila con un solo mínimo
    "Una fila, un mínimo al inicio" ~: reemplazarMinimoDeCadaFila [[1, 2, 3]] 99 ~?= [[99, 2, 3]],
    
    -- Caso con múltiples mínimos en una fila
    "Una fila, múltiples mínimos" ~: reemplazarMinimoDeCadaFila [[2, -1, 2, -1, -1]] 99 ~?= [[2, 99, 2, 99, 99]],
    
    -- Caso con matriz de una columna
    "Matriz una columna" ~: reemplazarMinimoDeCadaFila [[5],[2],[-8],[2],[-7]] 0 ~?= [[0],[0],[0],[0],[0]],
    
    -- Caso con múltiples filas
    "Múltiples filas, inicio medio final" ~: reemplazarMinimoDeCadaFila [[1, 2, 3], [4, 0, 5], [10, 20, 2]] 999 ~?= [[999, 2, 3], [4, 999, 5], [10, 20, 999]],
    
    -- Caso con números negativos
    "reemplazar con números negativos" ~: reemplazarMinimoDeCadaFila [[-5, -2, 0, -2, 0], [1, -10, 5, -10, 5]] (-1) ~?= [[-1, -2, 0, -2, 0], [1, -1, 5, -1, 5]],
    
    -- Caso con todos elementos iguales
    "Todos iguales" ~: reemplazarMinimoDeCadaFila [[700, 700, 700], [3, 3, 3], [-1,-1,-1]] 100 ~?= [[100, 100, 100], [100, 100, 100], [100, 100, 100]],
    
    -- Caso con matriz 1x1
    "Matriz 1x1" ~: reemplazarMinimoDeCadaFila [[42]] 0 ~?= [[0]],
    
    -- Caso con valor igual al mínimo
    "Valor igual al mínimo no reemplaza" ~: reemplazarMinimoDeCadaFila [[10, 20, 10, 40, 10]] 10 ~?= [[10, 20, 10, 40, 10]],
    
    -- Caso con matrices más grandes
    "Matriz 7x3" ~: reemplazarMinimoDeCadaFila [[8, 7, 9, 8, 7, 8, 7], [1, 5, 9, 1, 5, 9, 5], [4, 4, 1, 4, -7, 6, -7]] 0 ~?= [[8, 0, 9, 8, 0, 8, 0], [0, 5, 9, 0, 5, 9, 5], [4, 4, 1, 4, 0, 6, 0]]

    ]
