import Parcial
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "Lista vacía" ~: saturarEnUmbralHastaNegativo [] 5 ~?= [],
    "Ningún elemento supera el umbral" ~: saturarEnUmbralHastaNegativo [1, 2, 3, 4] 5 ~?= [1, 2, 3, 4],
    "Algunos elementos superan el umbral" ~: saturarEnUmbralHastaNegativo [3, 6, 2, 9] 5 ~?= [3, 5, 2, 5],
    "Todos los elementos superan el umbral" ~: saturarEnUmbralHastaNegativo [6, 7, 8] 5 ~?= [5, 5, 5],
    "Lista con todos iguales al umbral" ~: saturarEnUmbralHastaNegativo [5, 5, 5] 5 ~?= [5, 5, 5],
    "Lista con un solo elemento menor al umbral" ~: saturarEnUmbralHastaNegativo [3] 5 ~?= [3],
    "Lista con un solo elemento igual al umbral" ~: saturarEnUmbralHastaNegativo [5] 5 ~?= [5],
    "Lista con un solo elemento mayor al umbral" ~: saturarEnUmbralHastaNegativo [7] 5 ~?= [5],
    "Lista con valores mixtos y umbral positivo" ~: saturarEnUmbralHastaNegativo [199, 0, 1, 2, 3, 4, 5, 6] 3 ~?= [3,0,1,2,3,3,3,3],
    "Lista con valores grandes" ~: saturarEnUmbralHastaNegativo [1000, 2000, 3000] 1500 ~?= [1000, 1500, 1500],
    "Lista con un negativo al final" ~: saturarEnUmbralHastaNegativo [3, 6, 2, 9, -1] 5 ~?= [3, 5, 2, 5],
    "Lista con varios negativos al final" ~: saturarEnUmbralHastaNegativo [3, 6, 2, 9, -1, -4, -6] 5 ~?= [3, 5, 2, 5],
    "Lista con varios negativos al principio" ~: saturarEnUmbralHastaNegativo [-1, -4, -6, 3, 6, 2, 9] 5 ~?= [],
    "Lista con positivos después de negativos" ~: saturarEnUmbralHastaNegativo [3, 6, 2, 9, -1, -4, 6] 5 ~?= [3, 5, 2, 5],
    "Lista con todos negativos" ~: saturarEnUmbralHastaNegativo [-1, -4, -6] 5 ~?= []
    ]
