import unittest
from template_t1 import mejores_precios, seguidilla, elem_en_pos_pares, viajes_por_dia

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

class Ej2Test(unittest.TestCase):
    def test_trivial(self): # Testea que el valor devuelto sea un numero 
        res = seguidilla([],0.0)
        res = res>0 or res<=0 # Para este caso trivial, cualquier valor me sirve
        self.assertTrue(res)

class Ej3Test(unittest.TestCase):
    def test_trivial(self): # Testea que el resultado sea una lista
        res = elem_en_pos_pares([], 0.0) 
        self.assertEqual(res, [])


class Ej4Test(unittest.TestCase):
    def test_trivial(self): # Testea que el diccionario sea un diccionario (puede ser vacío)
        res = viajes_por_dia({},[])
        self.assertGreaterEqual(len(res.keys()), 0) 

if __name__ == '__main__':
    unittest.main(verbosity=2)

