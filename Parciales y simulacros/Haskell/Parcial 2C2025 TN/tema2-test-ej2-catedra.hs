import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[    
    "Ejemplo1" ~: sanguchitoDeCerosMasGrande [0,5,0,2,0,1] ~?= 5,
    "Ejemplo2" ~: sanguchitoDeCerosMasGrande [1,0,3,1,0] ~?= 0,
    " No hay sanguchito" ~: sanguchitoDeCerosMasGrande [1,0,0,2,2,0] ~?= 0,
    " Hay un sanguchito" ~: sanguchitoDeCerosMasGrande [1,0,0,6,0,2] ~?= 6,
    " Hay varios sanguchitos" ~: sanguchitoDeCerosMasGrande [1,0,2,0,8,0,0,9] ~?= 8,
    " El mayor es 0" ~: sanguchitoDeCerosMasGrande [0,0,0,0,0,0] ~?= 0
    ]
