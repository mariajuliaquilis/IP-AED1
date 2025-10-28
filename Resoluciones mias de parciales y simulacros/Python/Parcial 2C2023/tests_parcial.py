import unittest
from ejercicio1 import *
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *

class tests_ejercicio1(unittest.TestCase):
    def test_ej1_ejemplo_enunciado(self):
        s = [-1, 1, 1, 5, -7, 1, 3]
        n = 2
        elem = 1
        res_obtenido = ind_nesima_aparicion(s, n, elem)
        res_esperado = 2
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej1_ejemplo2(self):
        s = [1,2,3]
        n = 2 
        elem = 4
        res_obtenido = ind_nesima_aparicion(s, n, elem)
        res_esperado = -1
        self.assertEqual(res_obtenido, res_esperado) 
    
    def test_ej1_ejemplo3(self):
        s = [1,2,3]
        n = 1 
        elem = 1
        res_obtenido = ind_nesima_aparicion(s, n, elem)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado) 

    def test_ej1_ejemplo4(self):
        s = [1,2,3]
        n = 1 
        elem = 3
        res_obtenido = ind_nesima_aparicion(s, n, elem)
        res_esperado = 2
        self.assertEqual(res_obtenido, res_esperado) 

    def test_ej1_ejemplo5(self):
        s = [1,1,1,1,1,1]
        n = 3 
        elem = 1
        res_obtenido = ind_nesima_aparicion(s, n, elem)
        res_esperado = 2
        self.assertEqual(res_obtenido, res_esperado) 

    def test_ej1_ejemplo6(self):
        s = []
        n = 2
        elem = 5
        res_obtenido = ind_nesima_aparicion(s, n, elem)
        res_esperado = -1
        self.assertEqual(res_obtenido, res_esperado) 

class tests_ejercicio2(unittest.TestCase):
    def test_ej2_enunciado(self):
        s1 = [1, 3, 0, 1]
        s2 = [4, 0, 2, 3]
        res_obtenido = mezclar(s1, s2)
        res_esperado = [1, 4, 3, 0, 0, 2, 1, 3]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_secuencias_vacias(self):
        s1 = []
        s2 = []
        res_obtenido = mezclar(s1, s2)
        res_esperado = []
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej2_listas_de_longitud_igual_a_1(self):
        s1 = [2]
        s2 = [3]
        res_obtenido = mezclar(s1, s2)
        res_esperado = [2,3]
        self.assertEqual(res_obtenido, res_esperado)

class tests_ejercicio3(unittest.TestCase):
    def test_ej3_enunciado(self):
        caballos = ["linda", "petisa", "mister", "luck"]
        carreras = {"carrera1":["linda", "petisa", "mister", "luck"],
                    "carrera2":["petisa", "mister", "linda", "luck"]}
        res_obtenido = frecuencia_posiciones_por_caballo(caballos, carreras)
        res_esperado = {"petisa": [1,1,0,0],
                        "mister": [0,1,1,0],
                        "linda": [1,0,1,0],
                        "luck": [0,0,0,2]}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej3_ejemplo1(self):
        caballos = ["linda", "petisa"]
        carreras = {"carrera1":["linda", "petisa"],
                    "carrera2":["petisa", "linda"],
                    "carrera3":["linda", "petisa"]}
        res_obtenido = frecuencia_posiciones_por_caballo(caballos, carreras)
        res_esperado = {"petisa": [1,2],
                        "linda": [2,1]}
        self.assertEqual(res_obtenido, res_esperado)


class tests_ejercicio4(unittest.TestCase):
    def test_ej4_enunciado(self):
        m = [[1,2,2,1],
             [-5,6,6,-5],
             [0,1,1,0]]
        res_obtenido = matriz_capicua(m)
        res_esperado = True
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo1(self):
        m = []
        res_obtenido = matriz_capicua(m)
        res_esperado = True
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo2(self):
        m = [[1,2,3,1],
             [-5,6,6,-5],
             [0,1,1,0]]
        res_obtenido = matriz_capicua(m)
        res_esperado = False
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo3(self):
        m = [[1,2,2,1],
             [-5,6,6,-5],
             [0,4,1,0]]
        res_obtenido = matriz_capicua(m)
        res_esperado = False
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo4(self):
        m = [[1],
             [-5],
             [0]]
        res_obtenido = matriz_capicua(m)
        res_esperado = True
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo5(self):
        m = [[1,2,3,4],
             [-5,6,7,-5],
             [0,4,3,0]]
        res_obtenido = matriz_capicua(m)
        res_esperado = False
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo6(self):
        m = [[1,2,1],
             [-5,6,-5],
             [0,4,0]]
        res_obtenido = matriz_capicua(m)
        res_esperado = True
        self.assertEqual(res_obtenido, res_esperado)

    def test_ej4_ejemplo7(self):
        m = [[1,2,3],
             [-5,6,2],
             [0,4,1]]
        res_obtenido = matriz_capicua(m)
        res_esperado = False
        self.assertEqual(res_obtenido, res_esperado)


if __name__ == '__main__':
    unittest.main(verbosity=2)