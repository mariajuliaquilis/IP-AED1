import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "sumaIesimaColumna matriz1x1 " ~: sumaIesimaColumna matriz1x1 1 ~?= 3,
    "sumaIesimaColumna matriz2x1 " ~: sumaIesimaColumna matriz2x1 1 ~?= 0,
    "sumaIesimaColumna matriz2x2 col 1 " ~: sumaIesimaColumna matriz2x2 1 ~?= 0,
    "sumaIesimaColumna matriz2x2 col 2 " ~: sumaIesimaColumna matriz2x2 2 ~?= 5,
    "sumaIesimaColumna matriz2x3 col 1 " ~: sumaIesimaColumna matriz2x3 1 ~?= 0,
    "sumaIesimaColumna matriz2x3 col 2 " ~: sumaIesimaColumna matriz2x3 2 ~?= 5,
    "sumaIesimaColumna matriz2x3 col 3 " ~: sumaIesimaColumna matriz2x3 3 ~?= 7,
    "sumaIesimaColumna matrizFila col 1 " ~: sumaIesimaColumna matrizFila 1 ~?= 11,
    "sumaIesimaColumna matrizFila col 4 " ~: sumaIesimaColumna matrizFila 4 ~?= 14,
    "sumaIesimaColumna matrizFila col 7 " ~: sumaIesimaColumna matrizFila 7 ~?= 17,
    "sumaIesimaColumna matrizColumna col 1 " ~: sumaIesimaColumna matrizColumna 1 ~?= 100,
    "sumaIesimaColumna matrizGrande col 1 " ~: sumaIesimaColumna matriz100x100 1 ~?= 100,
    "sumaIesimaColumna matrizGrande col 10 " ~: sumaIesimaColumna matriz100x100 10 ~?= 1000,
    "sumaIesimaColumna matrizGrande col 100 " ~: sumaIesimaColumna matriz100x100 100 ~?= 10000,
    "sumaIesimaColumna matrizNxM col 20 " ~: sumaIesimaColumna matrizNxM 20 ~?= 1000,
    "sumaIesimaColumna matrizMxN col 8 " ~: sumaIesimaColumna matrizMxN 8 ~?= 14*50
    ]

matriz1x1 = [[3]]
matriz2x1 = [[3],[-3]]
matriz2x2 = [[3, 4],
             [-3, 1]]
matriz2x3 = [[3, 4, 0],
             [-3, 1, 7]]
matrizFila = [[11,12,13,14,15,16,17]]
matrizColumna = [[10],[15],[20],[25],[30]]
matriz100x100 = replicate 100 [1..100] 
matrizNxM = replicate 50 ([1..100]) 
matrizMxN = replicate 50 (take 20 [0,2..]) 
