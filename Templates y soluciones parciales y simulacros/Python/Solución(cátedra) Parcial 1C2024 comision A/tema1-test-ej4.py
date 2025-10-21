import inspect
import unittest
from solucion import nivel_de_ocupacion

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej4Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej4Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(nivel_de_ocupacion)
        if len(code.splitlines()) <= 2:
            Ej4Test.is_default = True

    def setUp(self):
        if Ej4Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")
    
    def test_caso_base(self):
        camas_por_piso = [
            [True, False, True],
            [False, False, True],
            [True, True, True]
        ]
        esperado = [2/3, 1/3, 1.0]
        esperado_100 = [2/3*100, 1/3*100, 1.0*100]
        res = nivel_de_ocupacion(camas_por_piso)
        self.assertTrue(res == esperado or res == esperado_100)

    def test_todas_camas_ocupadas(self):
        camas_por_piso = [
            [True, True, True,True, True, True],
            [True, True, True,True, True, True],
            [True, True, True,True, True, True]
        ]
        esperado = [1.0, 1.0, 1.0]
        esperado_100 = [100.0, 100.0, 100.0]
        res = nivel_de_ocupacion(camas_por_piso)
        self.assertTrue(res == esperado or res == esperado_100)

    def test_niguna_cama_ocupada(self):
        camas_por_piso = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]
        esperado = [0.0, 0.0, 0.0]
        res = nivel_de_ocupacion(camas_por_piso)
        self.assertTrue(res == esperado)

    def test_camas_mixtas(self):
        camas_por_piso = [
            [True, False, False],
            [True, True, False],
            [False, False, False]
        ]
        esperado = [1/3, 2/3, 0.0]
        esperado_100 = [1/3*100, 2/3*100, 0.0]
        res = nivel_de_ocupacion(camas_por_piso)
        self.assertTrue(res == esperado or res == esperado_100)

    def test_camas_mixtas_x6(self):
        camas_por_piso = [
            [True, False, True, False, True, False],
            [True, True, False, False, False, True],
            [False, False, False, False, True, False]
        ]
        esperado = [3/6, 3/6, 1/6]
        esperado_100 = [3/6*100, 3/6*100, 1/6*100]
        res = nivel_de_ocupacion(camas_por_piso)
        self.assertTrue(res == esperado or res == esperado_100)

        
    def test_nivel_de_ocupacion_mixtas_4(self):
    # Caso de varios pisos con distinta cantidad de camas ocupadas
        camas_por_piso = [[True,True,True,True], [True,True,True,False], [True,True,False,False], [False,False,False,False]]
        esperado = [1.0, 0.75, 0.50, 0]
        esperado_100 = [1.0*100, 0.75*100, 0.50*100, 0]
        res = nivel_de_ocupacion(camas_por_piso)
        self.assertTrue(res == esperado or res == esperado_100)


if __name__ == '__main__':
    unittest.main(verbosity=2)
