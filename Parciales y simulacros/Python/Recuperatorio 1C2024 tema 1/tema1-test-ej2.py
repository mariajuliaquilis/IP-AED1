import unittest
import ip_unittest
from solucion import cantidad_digitos_pares

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test(ip_unittest.UnitTest):
    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        self.method = cantidad_digitos_pares

    def test_trivial(self):
        entrada:list[int] = []
        entrada_copia:list[int] = entrada[:]
        salida:int = 0
        res:int = cantidad_digitos_pares(entrada)
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_un_numero(self):
        entrada:list[int] = [421]
        entrada_copia:list[int] = entrada[:]
        salida:int = 2
        res = cantidad_digitos_pares(entrada)
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_varios_numeros(self): 
        entrada = [5434, 42, 811, 3139, 1] 
        entrada_copia:list[int] = entrada[:]
        salida:int = 5
        res:int = cantidad_digitos_pares(entrada)
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)        
   
    def test_sin_digitos_pares(self):
        entrada = [111, 333, 555]
        entrada_copia:list[int] = entrada[:]
        salida = 0
        res:int = cantidad_digitos_pares(entrada)
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
 
    def test_todos_digitos_pares(self):
        entrada = [2468, 284, 82]
        entrada_copia:list[int] = entrada[:]
        salida = 9
        res:int = cantidad_digitos_pares(entrada)
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_numero_cero(self):
        entrada = [0, 20, 103]
        salida = 4
        entrada_copia:list[int] = entrada[:]
        res:int = cantidad_digitos_pares(entrada)
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)        


if __name__ == '__main__':
    unittest.main(verbosity=2)
