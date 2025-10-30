import unittest
from ejercicio_1 import *
from ejercicio_2 import *
from ejercicio_3 import *
from ejercicio_4 import *

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test(unittest.TestCase):
    def test_trivial(self): # Testea que la función devuelva una lista
        res = mejores_precios([],[])
        self.assertEqual(res, [])

    def test_dado_en_el_ejercicio(self): #Testea que la función devuelva res = [("leche", 151.0), ("yerba", 3939.1), ("jabón", 269.2)]
        res = mejores_precios([("leche", 151.0), ("yerba", 4719.5), ("jabón", 269.2)], [("leche", 261.2), ("yerba", 3939.1), ("jabón", 319.2)])
        self.assertEqual(res, [("leche", 151.0), ("yerba", 3939.1), ("jabón", 269.2)])

    def test_longitud_listas_igual_a_1(self): #Testea dos listas con longitud igual a 1
        res = mejores_precios([("leche", 151.0)], [("leche", 261.2)])
        self.assertEqual(res, [("leche", 151.0)])

    def test_que_devuelve_elementos_del_super1(self):
        res = mejores_precios([("leche", 151.0), ("yerba", 2000.0), ("jabón", 269.2)], [("leche", 261.2), ("yerba", 3939.1), ("jabón", 319.2)])
        self.assertEqual(res, [("leche", 151.0), ("yerba", 2000.0), ("jabón", 269.2)])
    
    def test_que_devuelve_elementos_del_super2(self):
        res = mejores_precios([("leche", 450.0), ("yerba", 2000.0), ("jabón", 269.2)], [("leche", 261.2), ("yerba", 500.0), ("jabón", 50.0)])
        self.assertEqual(res, [("leche", 261.2), ("yerba", 500.0), ("jabón", 50.0)])


class Ej2Test(unittest.TestCase):
    def test_trivial(self): # Testea que el valor devuelto sea un numero 
        res = seguidilla([],0.0)
        res = res>0 or res<=0 # Para este caso trivial, cualquier valor me sirve
        self.assertTrue(res)

    def test_ej2_ejemplo_1(self):
        calificaciones = [10,55,60,87,54,98,87,65,55,45,57]
        nota_minima = 60
        res_obtenido = seguidilla(calificaciones, nota_minima)
        res_esperado = 3
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_ejemplo_2(self):
        calificaciones = [10,55,60,65,54,64,65,55,45,57]
        nota_minima = 70
        res_obtenido = seguidilla(calificaciones, nota_minima)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_ejemplo_3(self):
        calificaciones = [10, 54, 62, 75, 90, 38, 17, 19, 67, 79, 14, 23, 100, 87, 89, 94, 32]
        nota_minima = 60
        res_obtenido = seguidilla(calificaciones, nota_minima)
        res_esperado = 4
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_ejemplo_4(self):
        calificaciones = [70,80,90,15,59,100,77,12,90]
        nota_minima = 60
        res_obtenido = seguidilla(calificaciones, nota_minima)
        res_esperado = 3
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_ejemplo_5(self):
        calificaciones = [10,70]
        nota_minima = 60
        res_obtenido = seguidilla(calificaciones, nota_minima)
        res_esperado = 1
        self.assertEqual(res_obtenido, res_esperado)

class Ej3Test(unittest.TestCase):
    def test_trivial(self): # Testea que el resultado sea una lista
        res = elem_en_pos_pares([], 0.0) 
        self.assertEqual(res, [])

    def test_ejemplo(self):
        elem = 1
        M = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 4, 5, 3, 2, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 1, 0, 0, 6, 0, 0, 1, 0],
            ]
        res = elem_en_pos_pares(M, elem)
        self.assertEqual(res, [True, True, True, False, False])

    def otro_test(self):
        elem = 7
        M = [
            [7,2,3],
            [2,9,7],
            [4,7,2],
            ]
        res = elem_en_pos_pares(M, elem)
        self.assertEqual(res, [True, True, False])

    def test_ejercicio3(self):
        elem = 2
        M = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 4, 5, 3, 2, 1],
            [0, 0, 0, 0, 2, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 2],
            [0, 2, 0, 0, 6, 0, 0, 1, 0],
            ]
        res = elem_en_pos_pares(M, elem)
        self.assertEqual(res, [False, False, True, True, False])

class Ej4Test(unittest.TestCase):
    def test_trivial(self): # Testea que el diccionario sea un diccionario (puede ser vacío)
        res = viajes_por_dia({},[])
        self.assertGreaterEqual(len(res.keys()), 0) 

    def test_ej4_dado_en_el_enunciado(self):
        viajes_diarios = {1 : ["Juan", "Maria"], 2 : ["Marcela","Juan"]}
        usuarios = ["Juan", "Maria", "Marcela"]
        res_obtenido = viajes_por_dia(viajes_diarios, usuarios)
        res_esperado = {"Juan" : 2, "Maria" : 1, "Marcela": 1}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo_1(self):
        viajes_diarios = {1 : ["Juan", "Maria"], 2 : ["Marcela","Juan"], 3 : ["Franco", "Rubén"], 4 : ["Juan", "Rubén"]}
        usuarios = ["Juan", "Maria", "Marcela", "Franco", "Rubén"]
        res_obtenido = viajes_por_dia(viajes_diarios, usuarios)
        res_esperado = {"Juan" : 3, "Maria" : 1, "Marcela": 1, "Franco" : 1, "Rubén" : 2}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo_2(self):
        viajes_diarios = {1 : ["Juan", "Maria"], 2 : ["Marcela","Juan"], 3 : ["Daniel"]}
        usuarios = ["Juan", "Maria", "Marcela", "Daniel", "Rubén"]
        res_obtenido = viajes_por_dia(viajes_diarios, usuarios)
        res_esperado = {"Juan" : 2, "Maria" : 1, "Marcela": 1, "Daniel" : 1, "Rubén" : 0}
        self.assertEqual(res_obtenido, res_esperado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
