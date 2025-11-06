import unittest
import ip_unittest
from solucion import matriz_pseudo_ordenada

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej4Test(ip_unittest.UnitTest):
    def __init__(self, *args, **kwargs):
        super(Ej4Test, self).__init__(*args, **kwargs)
        self.method = matriz_pseudo_ordenada

    def test_trivial(self):
        entrada:list[list[int]] = [[1]]
        entrada_pre:list[list[int]] = entrada[:]
        salida:bool = True
        res:bool = matriz_pseudo_ordenada(entrada)
        self.assertTrue(res)
        self.assertEqual(entrada, entrada_pre)
    
    def test_3x4_true(self):
        entrada:list[list[int]] = [
            [1, 3, 5, 5],
            [2, 1, 6, 7],
            [0, 2, 4, 8]
        ]
        entrada_pre:list[list[int]] = entrada[:]
        res:bool = matriz_pseudo_ordenada(entrada)
        self.assertTrue(res)
        self.assertEqual(entrada, entrada_pre)
    
    def test_4x3_false(self):
        entrada:list[list[int]] = [
            [0, 3, 5],
            [2, 2, 6],
            [0, 4, 4],
            [3, 5, 2]
        ]
        entrada_pre:list[list[int]] = entrada[:]
        res:bool = matriz_pseudo_ordenada(entrada)
        self.assertFalse(res)
        self.assertEqual(entrada, entrada_pre)
    
    def test_1_fila_true(self):
        entrada:list[list[int]] = [
            [5, 6, 8, 10],            
        ]
        entrada_pre:list[list[int]] = entrada[:]
        res:bool = matriz_pseudo_ordenada(entrada)
        self.assertTrue(res)
        self.assertEqual(entrada, entrada_pre)
    
    def test_1_columna(self):
        entrada:list[list[int]] = [
            [1],
            [2],
            [6],
            [3]
        ]
        entrada_pre:list[list[int]] = entrada[:]
        res:bool = matriz_pseudo_ordenada(entrada)
        self.assertTrue(res)
        self.assertEqual(entrada, entrada_pre)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

