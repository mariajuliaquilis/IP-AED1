--RECURSIÓN SOBRE NÚMEROS ENTEROS

--Ejercicio 1.
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

--Ejercicio 2.
parteEntera :: Float -> Integer
parteEntera x | x < 1 = 0
              | otherwise = parteEntera(x-1) + 1

--Ejercicio 3:
{--
problema esDivisible (a: Z, b: Z) : Bool {
      requiere: { a > 0 ∧ b > 0}
      asegura: { (res = true) <-> a = b*k, para algún k con k ≠ 0}
--}

multiplicoNumero :: Integer -> Integer -> Integer -> Bool
multiplicoNumero a b c | a < b*c = False
                       | a == b*c = True
                       | otherwise = multiplicoNumero a b (c+1)

esDivisible :: Integer -> Integer -> Bool
esDivisible a b = multiplicoNumero a b 1 

--Ejercicio 4.
{--
problema sumoImpares (n: Z) : Z {
         requiere: {n >= 1}
         asegura: {res = suma de los primeros n números impares}
--}
sumoImparesHastaCiertoNumero :: Integer -> Integer -> Integer
sumoImparesHastaCiertoNumero n k | k == 0 = 0
                                 | (mod n 2 == 0) = (sumoImparesHastaCiertoNumero(n+1) (k))
                                 | otherwise = n + (sumoImparesHastaCiertoNumero(n+1) (k-1))      

sumaImpares :: Integer -> Integer
sumaImpares n = sumoImparesHastaCiertoNumero 1 n

--Ejercicio 5.
medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n*(medioFact(n-2))

--Ejercicio 6.
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | mod n 10 /= (mod(div n 10) 10) = False 
                      | otherwise = todosDigitosIguales(div n 10)

--Ejercicio 7.
cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos(div n 10)  

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos(n) = mod n 10
                 | otherwise = iesimoDigito (div n 10) i 

--Ejercicio 8.
{--
problema sumaDigitos (n: Z) : Z {
         requiere: {n >= 1}
         asegura: {res = suma de los dígitos de n}
--}
sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n 
              | otherwise = (mod n 10) + sumaDigitos (div n 10)

--Ejercicio 9.
esCapicua :: Integer -> Bool
esCapicua n | cantDigitos n == 1 = True 
            | (iesimoDigito n 1 == iesimoDigito n (cantDigitos n)) = esCapicua (mod (div n 10) 10)
            | otherwise = False

--Ejercicio 10
--a)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = f1(n-1) + 2^n

--b)
f2 :: Integer -> Float -> Float
f2 1 q = q
f2 n q = (f2 (n-1) q) + q^n

--c)
f3 :: Integer -> Float -> Float
f3 0 q = 0
f3 n q = (f3 (n-1) q) + q^(2*n - 1) + q^(2*n)

--d)
f4 :: Integer -> Float -> Float
f4 0 q = 1
f4 n q = (f3 n q) + (f2 (n-1) q)

--Ejercicio 11
--a)
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n*(factorial (n-1))

eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = eAprox(n-1) + 1/fromIntegral(factorial(n))

--b)
e :: Float
e = eAprox 10

--Ejercicio 12
sucesionRaizDe2 :: Integer -> Float
sucesionRaizDe2 1 = 2
sucesionRaizDe2 n = 2 + (1/sucesionRaizDe2(n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesionRaizDe2 n) - 1

--Ejercicio 13
f :: Integer -> Integer -> Integer
f 1 m = m --da m porque estoy haciendo la sumatoria desde j = 1 hasta m de 1^j que es sumar 1 m veces.
f n m = (f (n-1) m) + round(f2 m (fromIntegral(n)))

--Ejercicio 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n 1 = q*round(f2 n (fromIntegral(q)))
sumaPotencias q n m = (sumaPotencias q n (m-1)) + (q^m)*(round(f2 n (fromIntegral(q))))

--Ejercicio 15
sumatoria :: Integer -> Integer 
sumatoria 1 = 1
sumatoria n = n + sumatoria(n-1)

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n 1 = fromIntegral(sumatoria n)
sumaRacionales n m = (sumaRacionales n (m-1)) + (1/fromIntegral (m))*(fromIntegral(sumatoria(n)))

--Ejercicio 16
--a)
minimoDivisorDeN :: Integer -> Integer -> Integer
minimoDivisorDeN n i | mod n i == 0 = i --me quedo con el primer numero natural que divide
                     | otherwise = minimoDivisorDeN n (i+1) --pruebo con el siguiente natural

menorDivisor :: Integer -> Integer
menorDivisor 1 = 1
menorDivisor n = minimoDivisorDeN n 2

--b)
esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = (n == menorDivisor n)

--c)
maximoComunDivisor :: Integer -> Integer -> Integer
maximoComunDivisor a 0 = a
maximoComunDivisor a b = maximoComunDivisor b (mod a b)

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b = maximoComunDivisor a b == 1

--d)
siguientePrimo :: Integer -> Integer -> Integer -> Integer
siguientePrimo p n i | (i /= n) && (esPrimo(p)) = siguientePrimo (p+1) n (i+1)
                     | not(esPrimo(p)) = siguientePrimo (p+1) n i
                     | otherwise = p

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = siguientePrimo 2 n 1

--Ejercicio 17
auxFibonacci :: Integer -> Integer -> Bool 
auxFibonacci a b | fibonacci b > a = False
                 | fibonacci b == a = True
                 | otherwise = auxFibonacci a (b+1) 

esFibonacci :: Integer -> Bool
esFibonacci n = auxFibonacci n 0 

--Ejercicio 18
esPar :: Integer -> Bool
esPar n = mod n 2 == 0 

cualEsElParMasGrande :: Integer -> Integer -> Integer
cualEsElParMasGrande a b | ((esPar a && esPar b) && a >= b) || (esPar a && not(esPar b)) = a 
                         | ((esPar a && esPar b) && a < b ) || (not(esPar a) && esPar b) = b 
                         | otherwise = -1      

parMasGrande :: Integer -> Integer -> Integer -> Integer -> Integer
parMasGrande n d h res | (d == h) = res 
                       | res > (cualEsElParMasGrande (iesimoDigito n d) (iesimoDigito n (d+1))) = parMasGrande n (d+1) h res
                       | otherwise = parMasGrande n (d+1) h (cualEsElParMasGrande (iesimoDigito n d) (iesimoDigito n (d+1))) 

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = parMasGrande n 1 (cantDigitos(n)) (cualEsElParMasGrande (iesimoDigito n 1) (iesimoDigito n 1))

--Ejercicio 19
sumoPrimerosPrimos :: Integer -> Integer -> Integer -> Integer
sumoPrimerosPrimos p n i | (p == n) || (p > n) = p 
                         | otherwise = sumoPrimerosPrimos (p + (nEsimoPrimo (i+1)) ) n (i+1)

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = (n == sumoPrimerosPrimos (nEsimoPrimo 1) n 1)

--Ejercicio 20
-- ejemplo:
-- tomo a = 3, b = 5
-- si i = 3 -> sumaDivisores(3) = 1 + 3 = 4
-- si i = 4 -> sumaDivisores(4) = 1 + 2 + 4 = 7
-- si i = 5 -> sumaDivisores(5) = 1 + 5 = 6
-- tomaValorMax 3 5 = 4

sumaDivisores :: Integer -> Integer -> Integer -> Integer -> Integer
sumaDivisores n d h res | (d == h) = res+n
                        | mod n d == 0 = sumaDivisores n (d+1) h (res+d)
                        | otherwise = sumaDivisores n (d+1) h res

numeroConMayorSuma :: Integer -> Integer -> Integer
numeroConMayorSuma a b | (sumaDivisores a 1 a 0) >= (sumaDivisores b 1 b 0) = a 
                       | otherwise = b

numeroConElMaximoDivisor :: Integer -> Integer -> Integer -> Integer -> Integer
numeroConElMaximoDivisor a b i res | (a <= i && i <= b) && (numeroConMayorSuma a i == a) = numeroConElMaximoDivisor a b (i+1) a
                                   | (a <= i && i <= b) && (numeroConMayorSuma a i == i) = numeroConElMaximoDivisor i b (i+1) i 
                                   | otherwise = res

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax a b = numeroConElMaximoDivisor a b a a

--Ejercicio 21
teoremaPitagoras :: Integer -> Integer -> Integer -> Bool
teoremaPitagoras p q r = p^2 + q^2 <= r^2

satisfacePitagoras :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer -> Integer
satisfacePitagoras p q r i j res | (0 <= i && i <= p) && (0 <= j && j <= q) && (teoremaPitagoras i j r) = satisfacePitagoras p q r (i+1) j (res+1)
                                 | (0 <= i && i <= p) && (0 <= j && j <= q) && not(teoremaPitagoras i j r) = satisfacePitagoras p q r (i+1) j res
                                 | (0 <= j && j <= q) = satisfacePitagoras p q r 0 (j+1) res
                                 | otherwise = res


pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r = satisfacePitagoras m n r 0 0 0