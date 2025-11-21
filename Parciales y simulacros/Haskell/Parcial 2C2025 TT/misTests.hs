import Test.HUnit
import Parcial

testmayorFibonacciEnRango = test[
    "ejemplo1" ~: (mayorFibonacciEnRango 4 10) ~?= 8,
    "ejemplo2" ~: (mayorFibonacciEnRango 5 8) ~?= 8,
    "ejemplo3" ~: (mayorFibonacciEnRango 13 13) ~?= 13,
    "ejemplo4" ~: (mayorFibonacciEnRango 140 300) ~?= 233,
    "ejemplo5" ~: (mayorFibonacciEnRango 140 145) ~?= 144
    ]    

testEsMontaniaRusa = test[
    "ejemplo1" ~: (esMontaniaRusa [1,2,4]) ~?= False,
    "ejemplo2" ~: (esMontaniaRusa [3,1,4,0]) ~?= True,
    "ejemplo3" ~: (esMontaniaRusa [2]) ~?= True,
    "ejemplo4" ~: (esMontaniaRusa []) ~?= True,
    "ejemplo5" ~: (esMontaniaRusa [1,3,2,0]) ~?= False
    ] 

testCatalogoPorAutores = test[
    "ejemplo1"~: (catalogoPorAutores [("García Márquez","Cien años de soledad"),("Borges","Ficciones"), ("García Márquez","El amor en los tiempos del cólera")]) ~?= 
                [("García Márquez", ["Cien años de soledad","El amor en los tiempos del cólera"]),("Borges",["Ficciones"])],
    "ejemplo2"~: (catalogoPorAutores [("Poe","El cuervo")]) ~?= [("Poe",["El cuervo"])],
    "ejemplo3"~: (catalogoPorAutores []) ~?= [],
    "ejemplo4"~: (catalogoPorAutores [("Kafka", "La metamorfosis"), ("Kafka", "El proceso")]) ~?= [("Kafka", ["La metamorfosis", "El proceso"])]
    ]

testFilaDelMaximo = test[
    "ejemplo1"~: (filaDelMaximo [[1,2,3],[4,5,6],[7,8,9]]) ~?= 3,
    "ejemplo2"~: (filaDelMaximo [[7,8,9], [4,5,6], [1,2,3]]) ~?= 1,
    "ejemplo3"~: (filaDelMaximo [[2]]) ~?= 1,
    "ejemplo4"~: (filaDelMaximo [[-2,-10,-8], [1,4,20], [-50,-23,34]]) ~?= 3,
    "ejemplo5"~: (filaDelMaximo [[-13,-4,-9], [-90,-35,-15], [-1,-2,-3]]) ~?= 3,
    "ejemplo6"~: (filaDelMaximo [[1,2,3],[7,8,9],[4,5,6]]) ~?= 2
    ]

--Corro todas las pruebas
runTests = runTestTT $ TestList [
    testmayorFibonacciEnRango,
    testEsMontaniaRusa,
    testCatalogoPorAutores,
    testFilaDelMaximo
    ]