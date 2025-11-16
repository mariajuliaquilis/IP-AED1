import unittest
from solucion import subsecuencias_que_suman

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test():
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = subsecuencias_que_suman

    def test_vacia(self):
        entrada: list[int] = []
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 1)        
        self.assertEqual(res, [])
        self.assertEqual(entrada, entrada_copia)

    def test_un_elemento_no_alcanza(self):
        entrada: list[int] = [2]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 3)        
        self.assertEqual(res, [])
        self.assertEqual(entrada, entrada_copia)
        
    def test_un_elemento_se_pasa(self):
        entrada: list[int] = [2]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 1)        
        self.assertEqual(res, [])
        self.assertEqual(entrada, entrada_copia)

    def test_un_elemento_suma(self):
        entrada: list[int] = [2]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 2)        
        self.assertEqual(res, [[2]])
        self.assertEqual(entrada, entrada_copia)

    def test_una_sola_al_principio(self):
        entrada: list[int] = [2, 3, 14 , 25]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 19)        
        self.assertEqual(res, [[2, 3, 14]])
        self.assertEqual(entrada, entrada_copia)
        
    def test_una_sola_al_final(self):
        entrada: list[int] = [2, 3, 14 , 5]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 22)        
        self.assertEqual(res, [[3, 14, 5]])
        self.assertEqual(entrada, entrada_copia)
        
    def test_solo_repetidos_sin_sumar(self):
        entrada: list[int] = [2, 2, 2 , 2]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 2)        
        self.assertEqual(res, [[2], [2], [2], [2]])
        self.assertEqual(entrada, entrada_copia)
        
    def test_solo_repetidos(self):
        entrada: list[int] = [2, 2, 2 , 2]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 4)        
        self.assertEqual(res, [[2, 2], [2, 2], [2, 2]])
        self.assertEqual(entrada, entrada_copia)

    def test_repetidos(self):
        entrada: list[int] = [12, 2, 12 , 2]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 14)        
        self.assertEqual(res, [[12, 2], [2, 12], [12, 2]])
        self.assertEqual(entrada, entrada_copia)

    def test_largo_no_suma(self):
        entrada: list[int] = [12, 2, 33 , 2, 1, 3 , 4, 4, 6, 8,2,3,3,4,14]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 9)        
        self.assertEqual(res, [])
        
    def test_el_mezcladito(self):
        entrada: list[int] = [12, 2, 33 , 2, 1, 3 , 4, 4, 6, 8,1,2,3,4,14]
        entrada_copia: list[int] = entrada[:]
        res: int = subsecuencias_que_suman(entrada, 14)        
        self.assertEqual(res, [[12, 2], [2, 1, 3, 4, 4], [4, 4, 6], [6, 8], [8, 1, 2, 3], [14]])
        self.assertEqual(entrada, entrada_copia)

if __name__ == '__main__':
        unittest.main(verbosity=2)