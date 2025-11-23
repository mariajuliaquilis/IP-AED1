import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "hayPrimosGemelos desde y hasta iguales" ~: hayPrimosGemelos 6 6 ~?= False,
    "hayPrimosGemelos desde y hasta iguales y primos" ~: hayPrimosGemelos 11 11 ~?= False,
    "hayPrimosGemelos bordes del rango son primos hnos" ~: hayPrimosGemelos 11 13 ~?= True,
    "hayPrimosGemelos rango incluye primos hnos" ~: hayPrimosGemelos 10 15 ~?= True,
    "hayPrimosGemelos desde es uno de los primos hnos" ~: hayPrimosGemelos 11 18 ~?= True,
    "hayPrimosGemelos hasta es uno de los primos hnos" ~: hayPrimosGemelos 6 13 ~?= True,
    "hayPrimosGemelos rango sin primos" ~: hayPrimosGemelos 90 95 ~?= False,
    "hayPrimosGemelos rango con un solo primo" ~: hayPrimosGemelos 98 102 ~?= False,
    "hayPrimosGemelos rango varios primos hermanos" ~: hayPrimosGemelos 10 103 ~?= True
    ]