import Solucion
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "Divisores Propios" ~: divisoresPropios 1 ~?= [],
    "Divisores Propios" ~: divisoresPropios 6 ~?= [1,2,3],
    "Divisores Propios" ~: divisoresPropios 19979 ~?= [1],
    "Divisores Propios" ~: divisoresPropios 357 ~?= [1,3,7,17,21,51,119],
    "Divisores Propios" ~: divisoresPropios 66921 ~?= [1,3,22307]
    ]

