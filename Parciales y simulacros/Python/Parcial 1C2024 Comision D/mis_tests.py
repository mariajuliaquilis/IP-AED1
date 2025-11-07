import unittest
from parcial import *

class ejercicio_1(unittest.TestCase):
    def test_ejercicio1_1(self):
        stock_cambios: list[tuple[str, int]] = [("Arroz", 50), ("Jamón", 100), ("Aceitunas", 15)]
        res_obtenido: dict[str, tuple[int, int]] = stock_productos(stock_cambios)
        res_esperado: dict[str, tuple[int, int]] = {"Arroz": (50, 50), "Jamón":(100,100), "Aceitunas":(15,15)}
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio1_2(self):
        stock_cambios: list[tuple[str, int]] = [("Arroz", 50), ("Jamón", 100), ("Aceitunas", 15), ("Aceite", 0), ("Jamón", 24), ("Aceitunas", 90)]
        res_obtenido: dict[str, tuple[int, int]] = stock_productos(stock_cambios)
        res_esperado: dict[str, tuple[int, int]] = {"Arroz": (50, 50), "Jamón":(24,100), "Aceitunas":(15,90), "Aceite":(0,0)}
        self.assertEqual(res_esperado, res_obtenido)

class ejercicio_2(unittest.TestCase):
    def test_ejercicio2_1(self):
        codigos_barra: list[int] = [100, 200, 101, 113, 150, 107]
        res_obtenido: list[int] = filtrar_codigos_primos(codigos_barra)
        res_esperado: list[int] = [101, 113, 107]
        self.assertEqual(res_esperado, res_obtenido)
    
    def test_ejercicio2_2(self):
        codigos_barra: list[int] = [100, 200, 300]
        res_obtenido: list[int] = filtrar_codigos_primos(codigos_barra)
        res_esperado: list[int] = []
        self.assertEqual(res_esperado, res_obtenido)
    
    def test_ejercicio2_3(self):
        codigos_barra: list[int] = [101, 113]
        res_obtenido: list[int] = filtrar_codigos_primos(codigos_barra)
        res_esperado: list[int] = [101, 113]
        self.assertEqual(res_esperado, res_obtenido)                      

class ejercicio_3(unittest.TestCase):
    def test_ejercicio3_1(self):
        tipos_pacientes_atendidos: list[str] = ["gato"]
        res_obtenido: int = subsecuencia_mas_larga(tipos_pacientes_atendidos)
        res_esperado: int = 0
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio3_2(self):
        tipos_pacientes_atendidos: list[str] = ["loro", "perro", "gato"]
        res_obtenido: int = subsecuencia_mas_larga(tipos_pacientes_atendidos)
        res_esperado: int = 1
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio3_3(self):
        tipos_pacientes_atendidos: list[str] = ["loro", "perro", "gato", "hamster","gato", "gato", "perro"]
        res_obtenido: int = subsecuencia_mas_larga(tipos_pacientes_atendidos)
        res_esperado: int = 4
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio3_4(self):
        tipos_pacientes_atendidos: list[str] = ["loro", "hamster","perro"]
        res_obtenido: int = subsecuencia_mas_larga(tipos_pacientes_atendidos)
        res_esperado: int = 2
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio3_5(self):
        tipos_pacientes_atendidos: list[str] = ["gato", "loro", "gato", "perro", "perro", "hamster", "gato"]
        res_obtenido: int = subsecuencia_mas_larga(tipos_pacientes_atendidos)
        res_esperado: int = 2
        self.assertEqual(res_esperado, res_obtenido)

class ejercicio_4(unittest.TestCase):
    def test_ejercicio4_1(self):
        responsables: list[list[str]] = [["Paula", "José", "Laura", "Germán", "Carolina"],
                                         ["Paula", "José", "Laura", "Germán", "Carolina"],
                                         ["Paula", "José", "Laura", "Germán", "Carolina"],
                                         ["Paula", "José", "Laura", "Germán", "Carolina"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"]]
        res_obtenido: list[tuple[bool, bool]] = un_responsable_por_turno(responsables)
        res_esperado: list[tuple[bool, bool]] = [(True, True), (True, True), (True, True), (True, True), (True, True)]
        self.assertEqual(res_esperado, res_obtenido)

    def test_ejercicio4_2(self):
        responsables: list[list[str]] = [["Paula", "José", "Laura", "Germán", "Virginia"],
                                         ["Paula", "José", "Laura", "Germán", "Carolina"],
                                         ["Paula", "José", "Marcos", "Germán", "Carolina"],
                                         ["Paula", "José", "Laura", "Germán", "Carolina"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"],
                                         ["Ramón", "Claudia", "Franco", "Marta", "Luis"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"],
                                         ["Lucas", "Claudia", "Franco", "Marta", "Luis"]]
        res_obtenido: list[tuple[bool, bool]] = un_responsable_por_turno(responsables)
        res_esperado: list[tuple[bool, bool]] = [(True, False), (True, True), (False, True), (True, True), (False, True)]
        self.assertEqual(res_esperado, res_obtenido)



if __name__ == "__main__":
    unittest.main(verbosity=2)