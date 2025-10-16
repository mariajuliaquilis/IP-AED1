import unittest
from guia6 import *

class Test_es_multiplo_de(unittest.TestCase):
    def test_1(self):
        n = 8
        m = 4
        self.assertTrue(es_multiplo_de(n, m))

    def test_2(self):
        n = 8
        m = 5
        self.assertFalse(es_multiplo_de(n, m))

class Test_es_par(unittest.TestCase):
    def test_1(self):
        n = 8
        self.assertTrue(es_par(8))

    def test_2(self):
        n = 13
        self.assertFalse(es_par(13))

class Test_cantidad_de_pizzas(unittest.TestCase):
    def test_1(self):
        comensales = 4
        min_cant_porciones = 1
        res_obtenido = cantidad_de_pizzas(comensales, min_cant_porciones)
        res_esperado = 1
        self.assertEqual(res_obtenido, res_esperado)

    def test_2(self):
        comensales = 4
        min_cant_porciones = 3
        res_obtenido = cantidad_de_pizzas(comensales, min_cant_porciones)
        res_esperado = 2
        self.assertEqual(res_obtenido, res_esperado)

    def test_3(self):
        comensales = 5
        min_cant_porciones = 2
        res_obtenido = cantidad_de_pizzas(comensales, min_cant_porciones)
        res_esperado = 2
        self.assertEqual(res_obtenido, res_esperado)

class Test_alguno_es_0(unittest.TestCase):
    def test_1(self):
        numero1 = 8
        numero2 = 2
        resultado_obtenido = alguno_es_0(numero1, numero2)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_2(self):
        numero1 = 0
        numero2 = 2
        resultado_obtenido = alguno_es_0(numero1, numero2)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_3(self):
        numero1 = 8
        numero2 = 0
        resultado_obtenido = alguno_es_0(numero1, numero2)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_4(self):
        numero1 = 0
        numero2 = 0
        resultado_obtenido = alguno_es_0(numero1, numero2)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_ambos_son_0(unittest.TestCase):
    def test_1(self):
        numero1 = 0
        numero2 = 0
        resultado_obtenido = ambos_son_0(numero1, numero2)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_2(self):
        numero1 = 0
        numero2 = 4
        resultado_obtenido = ambos_son_0(numero1, numero2)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_1(self):
        numero1 = 3
        numero2 = 6
        resultado_obtenido = ambos_son_0(numero1, numero2)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_es_nombre_largo(unittest.TestCase):
    def test_1(self):
        nombre = "Clara"
        resultado_obtenido = es_nombre_largo(nombre)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_2(self):
        nombre = "Valentina"
        resultado_obtenido = es_nombre_largo(nombre)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_es_bisiesto(unittest.TestCase):
    def test_1(self):
        año = 2025
        resultado_obtenido = es_bisiesto(año)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_2(self):
        año = 2000
        resultado_obtenido = es_bisiesto(año)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_3(self):
        año = 1900
        resultado_obtenido = es_bisiesto(año)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_peso_pino(unittest.TestCase):
    def test_1(self):
        altura = 2
        resultado_obtenido = peso_pino(altura)
        resultado_esperado = 600
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        altura = 5
        resultado_obtenido = peso_pino(altura)
        resultado_esperado = 1300
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_3(self):
        altura = 7
        resultado_obtenido = peso_pino(altura)
        resultado_esperado = 1700
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_es_peso_util(unittest.TestCase):
    def test_1(self):
        peso = 300
        resultado_obtenido = es_peso_util(peso)
        resultado_esperado = False
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        peso = 900
        resultado_obtenido = es_peso_util(peso)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_sirve_pino(unittest.TestCase):
    def test_1(self):
        altura = 2
        resultado_obtenido = sirve_pino(altura)
        resultado_esperado = True
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        altura = 500
        resultado_obtenido = sirve_pino(altura)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_devolver_el_doble_si_es_par(unittest.TestCase):
    def test_1(self):
        numero = 4
        resultado_obtenido = devolver_el_doble_si_es_par(numero)
        resultado_esperado = 8
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        numero = 3
        resultado_obtenido = devolver_el_doble_si_es_par(numero)
        resultado_esperado = 3
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_devolver_valor_si_es_par_sino_el_que_sigue(unittest.TestCase):
    def test_1(self):
        numero = 4
        resultado_obtenido = devolver_valor_si_es_par_sino_el_que_sigue(numero)
        resultado_esperado = 4
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        numero = 3
        resultado_obtenido = devolver_valor_si_es_par_sino_el_que_sigue(numero)
        resultado_esperado = 4
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(unittest.TestCase):
    def test_1(self):
        numero = 6
        resultado_obtenido = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero)
        resultado_esperado = 12
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        numero = 18
        resultado_obtenido = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero)
        resultado_esperado = 36
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_lindo_nombre(unittest.TestCase):
    def test_1(self):
        nombre = "Georgina"
        resultado_obtenido = lindo_nombre(nombre)
        resultado_esperado = "Tu nombre tiene muchas letras!"
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        nombre = "Juan"
        resultado_obtenido = lindo_nombre(nombre)
        resultado_esperado = "Tu nombre tiene menos de 5 caracteres"
        self.assertEqual(resultado_obtenido, resultado_esperado)

class Test_te_toca_trabajar(unittest.TestCase):
    def test_1(self):
        sexo = "F"
        edad = 16
        resultado_obtenido = te_toca_trabajar(sexo, edad)
        resultado_esperado = "Andá de vacaciones"
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_2(self):
        sexo = "F"
        edad = 64
        resultado_obtenido = te_toca_trabajar(sexo, edad)
        resultado_esperado = "Andá de vacaciones"
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_3(self):
        sexo = "F"
        edad = 30
        resultado_obtenido = te_toca_trabajar(sexo, edad)
        resultado_esperado = "Te toca trabajar"
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_4(self):
        sexo = "M"
        edad = 16
        resultado_obtenido = te_toca_trabajar(sexo, edad)
        resultado_esperado = "Andá de vacaciones"
        self.assertEqual(resultado_esperado, resultado_obtenido)
    
    def test_5(self):
        sexo = "M"
        edad = 70
        resultado_obtenido = te_toca_trabajar(sexo, edad)
        resultado_esperado = "Andá de vacaciones"
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_6(self):
        sexo = "M"
        edad = 28
        resultado_obtenido = te_toca_trabajar(sexo, edad)
        resultado_esperado = "Te toca trabajar"
        self.assertEqual(resultado_esperado, resultado_obtenido)        

if __name__ == "__main__":
    unittest.main(verbosity=2)    