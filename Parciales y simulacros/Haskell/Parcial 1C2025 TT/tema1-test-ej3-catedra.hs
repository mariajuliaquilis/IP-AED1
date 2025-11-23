import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "maximaSumaDeTresConsecutivos lista de 3" ~: maximaSumaDeTresConsecutivos [1,4,1] ~?= 6,
    "maximaSumaDeTresConsecutivos lista de 3 neg" ~: maximaSumaDeTresConsecutivos [-1,-2,-3] ~?= -6,
    "maximaSumaDeTresConsecutivos max al ppio " ~: maximaSumaDeTresConsecutivos [10,10,2,3,4,1] ~?= 22,
    "maximaSumaDeTresConsecutivos max al final" ~: maximaSumaDeTresConsecutivos [1,10,3,3,40,10] ~?= 53,
    "maximaSumaDeTresConsecutivos max en el medio" ~: maximaSumaDeTresConsecutivos [0,1,8,8,1,2] ~?= 17,
    "maximaSumaDeTresConsecutivos max repetido" ~: maximaSumaDeTresConsecutivos [10,20,5,10,20] ~?= 35,
    "maximaSumaDeTresConsecutivos max es 0" ~: maximaSumaDeTresConsecutivos [-2,-1,-55,0,0,0,-3] ~?= 0,
    "maximaSumaDeTresConsecutivos max es negativo" ~: maximaSumaDeTresConsecutivos [10,-20,-5,-50,40] ~?= -15
    ]

