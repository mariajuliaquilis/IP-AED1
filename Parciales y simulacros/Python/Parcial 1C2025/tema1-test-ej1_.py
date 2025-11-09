import unittest
from parcial import cantidad_parejas_que_suman

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
        self.method = cantidad_parejas_que_suman

    def test_lista_vacia_devuelve_cero(self):
        entrada: list[int] = []
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 0)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

    def test_un_elemento_no_puede_formar_pareja(self):
        entrada: list[int] = [1]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 1)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

    def test_parejas_repetidas_cuenta_todas(self):
        entrada: list[int] = [2, 2, 2, 2, 2]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 4)
        self.assertEqual(res, 10)
        self.assertEqual(entrada, entrada_copia)

    def test_no_hay_parejas_con_si_mismo(self):
        entrada: list[int] = [2, 1]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 4)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

    def test_parejas_suman_valores_varios(self):
        entrada: list[int] = [1, 3, 2, 5, 4, 8]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 5)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)

    def test_parejas_con_numeros_negativos(self):
        entrada: list[int] = [-1, 6, -2, 3, 7, -3]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 5)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)
    
    def test_todos_negativos(self):
        entrada: list[int] = [-1, -2, -3, -4, -5, -6]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, -5)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)
    
    def test_todos_forman_pareja(self):
        entrada: list[int] = [1, 3, 4, 5, 6, 2]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 7)
        self.assertEqual(res, 3)
        self.assertEqual(entrada, entrada_copia)
    
    def test_suman_cero(self):
        entrada: list[int] = [1, 3, -1, 5, -6, 6]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 0)
        self.assertEqual(res, 2)
        self.assertEqual(entrada, entrada_copia)
    
    def test_no_hay_parejas(self):
        entrada: list[int] = [1, 2, 3, 4, 5, 6]
        entrada_copia: list[int] = entrada[:]
        res: int = cantidad_parejas_que_suman(entrada, 12)
        self.assertEqual(res, 0)
        self.assertEqual(entrada, entrada_copia)

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
