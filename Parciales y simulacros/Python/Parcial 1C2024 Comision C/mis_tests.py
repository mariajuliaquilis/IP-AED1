import unittest
from parcial import *

class ejercicio1(unittest.TestCase):
    def test_ej1_1(self):
        diccionario: dict[str, list[int]] = {"María": [0, 24, 67, 90, 52, 59, 78]}
        res_obtenido = promedio_de_salidas(diccionario)
        res_esperado = {"María": (3, 135/3)}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej1_2(self):        
        diccionario: dict[str, list[int]] = {"María": [0, 24, 67, 90, 52, 59, 78], "Santiago": [73, 60, 94, 12, 0, 45, 56, 78, 34]}
        res_obtenido = promedio_de_salidas(diccionario)
        res_esperado = {"María": (3, 135/3), "Santiago": (5, 207/5)}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej1_3(self):        
        diccionario: dict[str, list[int]] = {"María": [0, 0, 0, 0], "Santiago": [0, 0, 0, 0]}
        res_obtenido = promedio_de_salidas(diccionario)
        res_esperado = {"María": (0, 0.0), "Santiago": (0, 0.0)}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej1_4(self):        
        diccionario: dict[str, list[int]] = {"María": [0, 0, 0, 0], "Santiago": [23, 43, 55, 21, 38]}
        res_obtenido = promedio_de_salidas(diccionario)
        res_esperado = {"María": (0, 0.0), "Santiago": (5, 180/5)}
        self.assertEqual(res_obtenido, res_esperado)

class ejercicio2(unittest.TestCase):
    def test_ej2_1(self):
        lista: list[int] = [19,0,67,79,15,24]
        res_obtenido = tiempo_mas_rapido(lista)
        res_esperado = 4
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_2(self):
        lista: list[int] = [19,0,67,79,15,24,15]
        res_obtenido = tiempo_mas_rapido(lista)
        res_esperado = 4
        self.assertEqual(res_obtenido, res_esperado)
    
    def test_ej2_3(self):
        lista: list[int] = [19,24,56,0]
        res_obtenido = tiempo_mas_rapido(lista)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_4(self):
        lista: list[int] = [19,24,56,13]
        res_obtenido = tiempo_mas_rapido(lista)
        res_esperado = 3
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_5(self):
        lista: list[int] = [19,24,56,0, 17,17,17, 12, 65]
        res_obtenido = tiempo_mas_rapido(lista)
        res_esperado = 7
        self.assertEqual(res_obtenido, res_esperado)

class ejercicio3(unittest.TestCase):
    def test_ej3_1(self):
        lista: list[int] = [0,0,0,15,0,67]
        res_obtenido = racha_mas_larga(lista)
        res_esperado = (3,3)
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej3_2(self):
        lista: list[int] = [68, 34, 45, 50]
        res_obtenido = racha_mas_larga(lista)
        res_esperado = (1,3)
        self.assertEqual(res_obtenido, res_esperado)
    
    def test_ej3_3(self):
        lista: list[int] = [23, 40, 54, 80, 0]
        res_obtenido = racha_mas_larga(lista)
        res_esperado = (0, 2)
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej3_4(self):
        lista: list[int] = [23, 34, 0, 67, 45, 50, 43, 15, 90]
        res_obtenido = racha_mas_larga(lista)
        res_esperado = (4, 7)
        self.assertEqual(res_obtenido, res_esperado)

class ejercicio4(unittest.TestCase):
    def test_ej4_1(self):
        matriz: list[list[int]] = [[0,0,24,0], [12, 15, 0, 0], [0, 0, 70, 0], [0, 0, 63, 90]]
        res_obtenido = escape_en_solitario(matriz)
        res_esperado = [0, 2]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_2(self):
        matriz: list[list[int]] = [[0,0,24,0]]
        res_obtenido = escape_en_solitario(matriz)
        res_esperado = [0]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_3(self):
        matriz: list[list[int]] = [[12, 15, 0, 0]]
        res_obtenido = escape_en_solitario(matriz)
        res_esperado = []
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_4(self):
        matriz: list[list[int]] = [[0,0,0,0], [0, 0, 70, 0], [0, 0, 63, 90]]
        res_obtenido = escape_en_solitario(matriz)
        res_esperado = [1]
        self.assertEqual(res_obtenido, res_esperado)












if __name__ == "__main__":
    unittest.main(verbosity=2)