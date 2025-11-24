import Parcial
import Test.HUnit
import Data.List

main = runTestTT allTests

--normalize ordena la lista de tuplas, y también ordena la lista dentro del segundo elemento de cada tupla
--según el ordén alfabético. esto permite que el test pueda evaluar correctitud para el ej3 y acepte 
--varios ordenes de la lista outputteada.
normalize :: [(Integer, [String])] -> [(Integer, [String])]
normalize = sort . map (\(s, xs) -> (s, sort xs))


allTests = test[
    " Muchas series con distintas cantidades" ~: normalize (agruparPorCantidadDeTemporadas [("Otra2", 1), ("Lost",6),("Friends", 10),("Bojack",6), ("Serie", 6), ("Otra", 1)]) ~?= normalize [(1, ["Otra", "Otra2"]),(6,["Lost","Bojack", "Serie"]), (10,["Friends"])],    
    
    "Lista vacía" ~: normalize (agruparPorCantidadDeTemporadas []) ~?= normalize [],        
    
    "Una sola serie" ~: normalize (agruparPorCantidadDeTemporadas [("Breaking Bad", 5)]) ~?= normalize [(5, ["Breaking Bad"])],
    "Muchas series" ~: normalize (agruparPorCantidadDeTemporadas [("Gilmore", 10), ("Lost", 6), ("Friends", 10), ("Bojack", 6), ("Serie", 6), ("Otra", 1)]) ~?= normalize [(1, ["Otra"]), (6, ["Lost", "Bojack", "Serie"]), (10, ["Friends", "Gilmore"])],
    
    "Todas con misma cantidad" ~: normalize (agruparPorCantidadDeTemporadas [("S1", 3), ("S2", 3), ("S3", 3)]) ~?= normalize [(3, ["S1", "S2", "S3"])],
    
    "Todas diferentes" ~: normalize (agruparPorCantidadDeTemporadas [("S1", 1), ("S2", 2), ("S3", 3), ("S4", 4)]) ~?= normalize [(1, ["S1"]), (2, ["S2"]), (3, ["S3"]), (4, ["S4"])]
    
    ]

