import Solucion
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "materiasComisionN sin cursadas" ~: TestCase (assertPermutation (materiasComisionN [] 8 22)  []),
    "materiasComisionN una sola cursada TT " ~: TestCase (assertPermutation (materiasComisionN [algo1TT] 14 17) ["Algo1"]),
    "materiasComisionN una sola cursada TT repetido " ~: TestCase (assertPermutation (materiasComisionN [algo1TT, algo1TT] 14 17) ["Algo1"]),
    "materiasComisionN una sola cursada TM" ~: TestCase (assertPermutation (materiasComisionN [algo1TM] 14 17) []),
    "materiasComisionN una sola cursada TN" ~: TestCase (assertPermutation (materiasComisionN [algo1TN] 14 17) []),
    "materiasComisionN una de cada turno" ~: TestCase (assertPermutation (materiasComisionN [algo1TN, algo1TM, algo1TT] 14 17) ["Algo1"]),
    "materiasComisionN mmuchas TT" ~: TestCase (assertPermutation (materiasComisionN [algo1TT, algebraTMyTT, intensiva, analisisTT2] 14 17)  ["Algo1", "Algebra", "Materia intensiva", "Analisis"]),
    "materiasComisionN un poco de todo" ~:  TestCase (assertPermutation (materiasComisionN [algo1TT, algebraTMyTT, intensiva, analisisTT2, analisisTT, algebraTTyTN, algo1TM] 14 17)  ["Algo1", "Algebra", "Materia intensiva", "Analisis"]),
    "materiasComisionN muchas de otros turnos" ~: TestCase (assertPermutation (materiasComisionN [algo1TM, algo1TN, analisisTN ] 14 17) [])
    ]

algo1TM = ("Algo1", "Lunes", 9, 13)
algo1TT = ("Algo1", "Lunes", 14, 17)
algo1TN = ("Algo1", "Lunes", 17, 21)
algebraTMyTT = ("Algebra", "Martes", 11, 15)
algebraTTyTN = ("Algebra", "Martes", 16, 18)
intensiva = ("Materia intensiva", "Jueves", 9, 21)
analisisTT = ("Analisis", "Viernes", 15, 16)
analisisTT2 = ("Analisis", "Jueves", 14, 16)
analisisTN = ("Analisis", "Martes", 20, 22)

assertPermutation :: (Ord a, Show a) => [a] -> [a] -> Assertion
assertPermutation actual expected =
  assertBool msg (isPermutation actual expected)
  where
    msg = "Expected a permutation of " ++ show expected ++ ", but got " ++ show actual

isPermutation :: (Ord a) => [a] -> [a] -> Bool
isPermutation xs ys = sort xs == sort ys