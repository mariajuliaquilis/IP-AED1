import Solucion
import Test.HUnit
import Data.List

--main = runTestTT allTests
main = runTestTT allTests

allTests = test[
    "ambos vacíos" ~:  expectPermutacion (caracteresEnComun "" "") [],
    "primero vacío" ~:  expectPermutacion (caracteresEnComun "" "hola") [],
    "segundo vacío" ~:  expectPermutacion (caracteresEnComun "chau" "") [],
    "nada en común, misma long" ~:  expectPermutacion (caracteresEnComun "abc" "xyz") [],
    "nada en común, distinta long" ~:  expectPermutacion (caracteresEnComun "abcde" "xyz") [],
    "iguales sin repetidos" ~:  expectPermutacion (caracteresEnComun "abc" "abc") "cba",
    "iguales con repetidos" ~:  expectPermutacion (caracteresEnComun "abccc" "abccc") "cba",
    "primero incluído en segundo" ~:  expectPermutacion (caracteresEnComun "ab" "pabc") "ab",
    "segundo incluído en primero" ~:  expectPermutacion (caracteresEnComun "abcd" "ab") "ab",
    "mucho de todo" ~:  expectPermutacion (caracteresEnComun "xxayybzza" "xyuzd") "xyz",
    "con espacio en ambos" ~:  expectPermutacion (caracteresEnComun "xxa yy bzza" "xy uzd") " xyz",
    "con espacio solo en uno, punto en ambos" ~:  expectPermutacion (caracteresEnComun "xxa yy bzza." "xyuzd.") "xyz."
    ]


expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)