import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "materiasTurnoTarde sin cursadas" ~: TestCase (assertPermutation (materiasTurnoTarde [])  []),
    "materiasTurnoTarde una sola cursada TT " ~: TestCase (assertPermutation (materiasTurnoTarde [algo1TT]) ["Algo1"]),
    "materiasTurnoTarde una sola cursada TM" ~: TestCase (assertPermutation (materiasTurnoTarde [algo1TM]) []),
    "materiasTurnoTarde una sola cursada TN" ~: TestCase (assertPermutation (materiasTurnoTarde [algo1TN]) []),
    "materiasTurnoTarde una de cada turno" ~: TestCase (assertPermutation (materiasTurnoTarde [algo1TN, algo1TM, algo1TT]) ["Algo1"]),
    "materiasTurnoTarde mmuchas TT" ~: TestCase (assertPermutation (materiasTurnoTarde [algo1TT, algebraTMyTT, intensiva, analisisTT2])  ["Algo1", "Algebra", "Materia intensiva", "Analisis"]),
    "materiasTurnoTarde un poco de todo" ~:  TestCase (assertPermutation (materiasTurnoTarde [algo1TT, algebraTMyTT, intensiva, analisisTT2, analisisTT, algebraTTyTN, algo1TM])  ["Algo1", "Algebra", "Materia intensiva", "Analisis"]),
    "materiasTurnoTarde muchas de otros turnos" ~: TestCase (assertPermutation (materiasTurnoTarde [algo1TM, algo1TN, analisisTN ]) [])
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
assertPermutation expected actual =
  assertBool msg (isPermutation expected actual)
  where
    msg = "Expected a permutation of " ++ show expected ++ ", but got " ++ show actual

isPermutation :: (Ord a) => [a] -> [a] -> Bool
isPermutation xs ys = sort xs == sort ys