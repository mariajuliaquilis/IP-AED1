import unittest
from parcial import intercambiar_e_invertir_columnas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = intercambiar_e_invertir_columnas
    
    def test_intercambiar_e_invertir_columnas_en_matriz_1x2(self):
        matriz = [
            [10, 20]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [20, 10]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_2x2(self):
        matriz = [
            [1, 2],
            [3, 4]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [4, 3],
            [2, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_3x3(self):
        matriz = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 2)
        matriz_esperada = [
            [9, 2, 7],
            [6, 5, 4],
            [3, 8, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)

    def test_intercambiar_e_invertir_columnas_3x2(self):
        matriz = [
            [1, 2],
            [4, 5],
            [7, 8]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [8, 7],
            [5, 4],
            [2, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)

    def test_intercambiar_e_invertir_columnas_2x3(self):
        matriz = [
            [1, 2, 6],
            [4, 5, 4]
        ]
        intercambiar_e_invertir_columnas(matriz, 1, 2)
        matriz_esperada = [
            [1, 4, 5],
            [4, 6, 2],
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_iguales(self):
        matriz = [
            [1, 2, 1],
            [4, 5, 4],
            [7, 8, 7]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 2)
        matriz_esperada = [
            [7, 2, 7],
            [4, 5, 4],
            [1, 8, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_con_ceros(self):
        matriz = [
            [1, 0, 3],
            [4, 0, 6],
            [7, 0, 9]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [0, 7, 3],
            [0, 4, 6],
            [0, 1, 9]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_con_negativos(self):
        matriz = [
            [1, -2, 3],
            [-4, 5, -6],
            [-7, -8, 9]
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 2)
        matriz_esperada = [
            [9, -2, -7],
            [-6, 5, -4],
            [3, -8, 1]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_3x10(self):
        matriz = [
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
        ]
        intercambiar_e_invertir_columnas(matriz, 5, 8)
        matriz_esperada = [
            [11, 12, 13, 14, 15, 39, 17, 18, 36, 20],
            [21, 22, 23, 24, 25, 29, 27, 28, 26, 30],
            [31, 32, 33, 34, 35, 19, 37, 38, 16, 40]
        ]
        self.assertEqual(matriz, matriz_esperada)
    
    def test_intercambiar_e_invertir_columnas_en_matriz_8x3(self):
        matriz = [
            [11, 12, 13],
            [21, 22, 23],
            [31, 32, 33],
            [41, 42, 43],
            [51, 52, 53],
            [61, 62, 63],
            [71, 72, 73],
            [81, 82, 83],
        ]
        intercambiar_e_invertir_columnas(matriz, 0, 1)
        matriz_esperada = [
            [82, 81, 13],
            [72, 71, 23],
            [62, 61, 33],
            [52, 51, 43],
            [42, 41, 53],
            [32, 31, 63],
            [22, 21, 73],
            [12, 11, 83],
        ]
        self.assertEqual(matriz, matriz_esperada)
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
