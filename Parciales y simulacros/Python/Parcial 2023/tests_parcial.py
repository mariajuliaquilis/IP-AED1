import unittest
from ejercicio1 import *
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *

class tests_ejercicio_1(unittest.TestCase):
    def test_ejercicio1_enunciado(self):
        s = ["LLA", "UP", "LLA", "LLA", "UP"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP", "UP", "LLA", "LLA", "LLA"]
        self.assertEqual(res_obtenido, res_esperado)
    
    def test_ejercicio1_ejemplo2(self):
        s = ["LLA", "LLA", "LLA", "UP"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP", "LLA", "LLA", "LLA"]
        self.assertEqual(res_obtenido, res_esperado)
    
    def test_ejercicio1_ejemplo3(self):
        s = ["UP", "UP", "LLA", "LLA", "LLA"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP", "UP", "LLA", "LLA", "LLA"]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio1_ejemplo4(self):
        s = ["UP", "UP"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP", "UP"]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio1_ejemplo5(self):
        s = ["LLA", "LLA", "LLA"]
        res_obtenido = acomodar(s)
        res_esperado = ["LLA", "LLA", "LLA"]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio1_ejemplo6(self):
        s = ["LLA"]
        res_obtenido = acomodar(s)
        res_esperado = ["LLA"]
        self.assertEqual(res_obtenido, res_esperado)
    
    def test_ejercicio1_ejemplo7(self):
        s = ["UP"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP"]
        self.assertEqual(res_obtenido, res_esperado)
    
    def test_ejercicio1_ejemplo8(self):
        s = ["UP", "LLA"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP","LLA"]
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio1_ejemplo9(self):
        s = ["LLA", "UP"]
        res_obtenido = acomodar(s)
        res_esperado = ["UP","LLA"]
        self.assertEqual(res_obtenido, res_esperado)


class tests_ejercicio_2(unittest.TestCase):
    def test_ejercicio_2_enunciado(self):
        s = [1,-2,0,5,-7,3]
        u = 5
        res_obtenido = pos_umbral(s, u)
        res_esperado = 3
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio_2_ejemplo2(self):
        s = [1,-2,0,5,-7,3]
        u = 8
        res_obtenido = pos_umbral(s, u)
        res_esperado = 5
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio_2_ejemplo3(self):
        s = [13, 14, 15]
        u = 16
        res_obtenido = pos_umbral(s, u)
        res_esperado = 1
        self.assertEqual(res_obtenido, res_esperado)

class tests_ejercicio_3(unittest.TestCase):
    def test_ejercicio_3_enunciado(self):
        m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
        res_obtenido = columnas_repetidas(m)
        res_esperado = True
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio_3_ejemplo_2(self):
        m = [[1,1],[-5,-5],[0,0]]
        res_obtenido = columnas_repetidas(m)
        res_esperado = True
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio_3_ejemplo_3(self):
        m = [[1,2],[-5,6],[0,0]]
        res_obtenido = columnas_repetidas(m)
        res_esperado = False
        self.assertEqual(res_obtenido, res_esperado)



class tests_ejercicio_4(unittest.TestCase):
    def test_ejercicio_4_enunciado(self):
        naciones= ["arg", "aus", "nz", "sud"]
        torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
        res_obtenido = cuenta_posiciones_por_nacion(naciones, torneos)
        res_esperado = res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio_4_ejemplo2(self):
        naciones= ["arg", "aus"]
        torneos= {2023:["arg", "aus"], 2022:["aus", "arg"]}
        res_obtenido = cuenta_posiciones_por_nacion(naciones, torneos)
        res_esperado = res = {"arg": [1,1], "aus": [1,1]}
        self.assertEqual(res_obtenido, res_esperado)

    def test_ejercicio_4_ejemplo3(self):
        naciones= ["arg", "aus", "nz"]
        torneos= {2023:["nz","arg", "aus"], 2022:["nz","aus", "arg"]}
        res_obtenido = cuenta_posiciones_por_nacion(naciones, torneos)
        res_esperado = res = {"arg": [0,1,1], "aus": [0,1,1], "nz": [2,0,0]}
        self.assertEqual(res_obtenido, res_esperado)
   


if __name__ == "__main__":
    unittest.main(verbosity=2)