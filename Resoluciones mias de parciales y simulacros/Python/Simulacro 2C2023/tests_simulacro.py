import unittest
from ejercicio1 import *
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *

class tests_ejercicio_1(unittest.TestCase):
    def test_ejercicio_1_ejemplo_enunciado(self):
        s = [-1,4,0,4,100,0,100,0,-1,-1]
        e = 0
        res_obtenido = ultima_aparicion(s, e)
        res_esperado = 7
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio_1_ejemplo_2(self):
        s = [2,3]
        e = 2
        res_obtenido = ultima_aparicion(s, e)
        res_esperado = 0
        self.assertEqual(res_esperado, res_obtenido)
    
    def test_ejercicio_1_ejemplo_3(self):
        s = [2,3]
        e = 3
        res_obtenido = ultima_aparicion(s, e)
        res_esperado = 1
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio_1_ejemplo_4(self):
        s = [2]
        e = 2
        res_obtenido = ultima_aparicion(s, e)
        res_esperado = 0
        self.assertEqual(res_esperado, res_obtenido)
    
    def test_ejercicio_1_ejemplo_5(self):
        s = [2,3,3,3]
        e = 3
        res_obtenido = ultima_aparicion(s, e)
        res_esperado = 3
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio_1_ejemplo_6(self):
        s = [2,3,3,3,7]
        e = 7
        res_obtenido = ultima_aparicion(s, e)
        res_esperado = 4
        self.assertEqual(res_esperado, res_obtenido)

class tests_ejercicio_2(unittest.TestCase):
    def tests_ejercicio_2_enunciado(self):
        s = [-1,4,0,4,3,0,100,0,-1,-1]
        t = [0,100,5,0,100,-1,5]
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = [4,3,5]      
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_2_todos_repetidos(self):
        s = [-1,-1,-1]
        t = [-1]
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = []      
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_2_casi_todos_repetidos(self):
        s = [-1,-1,-1]
        t = [-1, 2]
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = [2]      
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_2_distintos(self):
        s = [-1]
        t = [4]
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = [-1, 4]      
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_2_s_es_vacio(self):
        s = []
        t = [4]
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = [4]      
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_2_t_es_vacio(self):
        s = [3]
        t = []
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = [3]      
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_2_secuencias_vacias(self):
        s = []
        t = []
        res_obtenido = elementos_exclusivos(s, t)
        res_esperado = []      
        self.assertEqual(res_obtenido, res_esperado)

class tests_ejercicio_3(unittest.TestCase):
    def tests_ejercicio_3_enunciado(self):
        alemán = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
        inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 2
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio3_ejemplo1(self):
        alemán = {"Madre": "Mutter", "Padre": "Vater", "Hermana": "Schwester"}
        inglés = {"Madre": "Mother", "Padre": "Father"}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio3_ejemplo2(self):
        alemán = {}
        inglés = {"Casa": "House"}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio3_ejemplo3(self):
        alemán = {"Casa": "Haus"}
        inglés = {}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio3_ejemplo4(self):
        alemán = {"Ojos": "Augen"}
        inglés = {"Ojos": "Eyes"}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio3_ejemplo5(self):
        alemán = {}
        inglés = {}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 0
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio3_ejemplo6(self):
        alemán = {"Invierno": "Winter", "Primavera": "Frühling"}
        inglés = {"Invierno": "Winter", "Primavera": "Spring"}
        res_obtenido = contar_traducciones_iguales(inglés, alemán)
        res_esperado = 1
        self.assertEqual(res_obtenido, res_esperado)

class tests_ejercicio_4(unittest.TestCase):
    def tests_ejercicio_4_enunciado(self):
        lista = [-1, 0, 4, 100, 100, -1, -1]
        res_obtenido = convertir_a_diccionario(lista)
        res_esperado = {-1:3, 0:1, 4:1, 100:2}
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_4_ejemplo_1(self):
        lista = []
        res_obtenido = convertir_a_diccionario(lista)
        res_esperado = {}
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_4_ejemplo_2(self):
        lista = [-1, 0]
        res_obtenido = convertir_a_diccionario(lista)
        res_esperado = {-1:1, 0:1}
        self.assertEqual(res_obtenido, res_esperado)

    def tests_ejercicio_4_ejemplo_3(self):
        lista = [-1, -1, -1]
        res_obtenido = convertir_a_diccionario(lista)
        res_esperado = {-1:3}
        self.assertEqual(res_obtenido, res_esperado)

if __name__ == '__main__':
    unittest.main(verbosity=2)