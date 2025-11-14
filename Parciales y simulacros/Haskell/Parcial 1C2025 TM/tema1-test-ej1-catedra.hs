import Parcial
import Test.HUnit

main = runTestTT allTests

allTests = test[
    -- Casos base y casos sin numeros abundantes
    "Rango sin números abundantes" ~: cantidadNumerosAbundantes 3 4 ~?= 0,
    "Rango de un solo número no abundante" ~: cantidadNumerosAbundantes 5 5 ~?= 0,
    "Rango pequeño sin abundantes" ~: cantidadNumerosAbundantes 1 5 ~?= 0,
    "Los primeros 11 números son no abundantes" ~: cantidadNumerosAbundantes 1 11 ~?= 0,
    -- Casos con numeros abundantes
    "Rango con un número abundante" ~: cantidadNumerosAbundantes 29 30 ~?= 1,
    "Rango con un número abundante, d y h iguales" ~: cantidadNumerosAbundantes 30 30 ~?= 1,
    "Rango con varios números abundantes" ~: cantidadNumerosAbundantes 3 30 ~?= 5,
    "Rango de un solo número abundante (grande)" ~: cantidadNumerosAbundantes 198126 198126 ~?= 1,
    "Rango que incluye varios abundantes (enunciado)" ~: cantidadNumerosAbundantes 12 24 ~?= 4,
    "Rango donde d y h son ambos abundantes" ~: cantidadNumerosAbundantes 18 30 ~?= 4,
    "Rango donde solo el límite superior es abundante" ~: cantidadNumerosAbundantes 10 12 ~?= 1,
    "Rango donde solo el límite inferior es abundante" ~: cantidadNumerosAbundantes 12 14 ~?= 1,
    "Rango grande" ~: cantidadNumerosAbundantes 30 198 ~?= 41
    ]
