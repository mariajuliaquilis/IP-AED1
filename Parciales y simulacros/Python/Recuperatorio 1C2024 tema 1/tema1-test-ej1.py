import unittest
import ip_unittest
from solucion import gestion_notas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''


class Ej1Test(ip_unittest.UnitTest):
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = gestion_notas

    def test_trivial(self):
        entrada:list[tuple[str, str, int]] = []
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = {}
        res = gestion_notas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_un_estudiante(self):
        entrada:list[tuple[str, str, int]] = [('Juan', 'Matemática', 5)]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = {'Juan': [('Matemática', 5)]}
        res = gestion_notas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_repite_estudiantes(self):
        # Hay estudiantes que tienen notas en distintas materias
        entrada:list[tuple[str, str, int]] = [
            ('Juan', 'Geografía', 5),
            ('Ana', 'Matemática', 9),
            ('Lucas', 'Lengua y Literatura', 6),
            ('Ana', 'Lengua y Literatura', 4),            
            ('Juan', 'Matemática', 5)
        ]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        
        salida = {
            'Juan':[('Geografía', 5), ('Matemática', 5)],
            'Ana': [('Matemática', 9), ('Lengua y Literatura', 4)],
            'Lucas': [('Lengua y Literatura', 6)]
        }
        res = gestion_notas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_solo_un_estudiante_varias_materias(self):
        entrada:list[tuple[str, str, int]] = [
            ('Juan', 'Matemática', 5),
            ('Juan', 'Lengua y Literatura', 6),
            ('Juan', 'Computación', 9),
            ('Juan', 'Arte', 9)
        ]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        
        salida = {
            'Juan':[('Matemática', 5), ('Lengua y Literatura', 6), ('Computación', 9), ('Arte', 9)]}
        res = gestion_notas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_notas_minimas_y_maximas(self):
        entrada = [("Pedro", "Geografía", 1), ("Lucía", "Historia", 10)]
        esperado = {
            "Pedro": [("Geografía", 1)],
            "Lucía": [("Historia", 10)]
        }
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        res = gestion_notas(entrada)
        self.assertDictEqualWithUnorderedLists(res, esperado)
        self.assertEqual(entrada, entrada_copia)

    def assertDictEqualWithUnorderedLists(self, dict1, dict2):
            self.assertEqual(dict1.keys(), dict2.keys(), "Los diccionarios tienen distintias claves.")
            
            for key in dict1:
                self.assertCountEqual(dict1[key], dict2[key], f"Las listas de la clave '{key}' no son iguales")

if __name__ == '__main__':
    unittest.main(verbosity=2)
