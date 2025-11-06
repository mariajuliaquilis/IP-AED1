import unittest
import ip_unittest
from solucion import gestion_ventas

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
        self.method = gestion_ventas
    
    def test_trivial(self):
        entrada:list[tuple[str, str, int]] = []
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = {}
        res = gestion_ventas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_un_vendedor(self):
        entrada:list[tuple[str, str, int]] = [('Juan', 'Monitor', 5)]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = {'Juan': [('Monitor', 5)]}
        res = gestion_ventas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_repite_vendedores(self):
        entrada:list[tuple[str, str, int]] = [
            ('Juan', 'Monitor', 5),
            ('Ana', 'PC', 9),
            ('Lucas', 'Teclado', 6),
            ('Ana', 'Teclado', 4),            
            ('Juan', 'Mouse', 5)
        ]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        
        salida = {
            'Juan':[('Monitor', 5), ('Mouse', 5)],
            'Ana': [('PC', 9), ('Teclado', 4)],
            'Lucas': [('Teclado', 6)]
        }
        res = gestion_ventas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_solo_un_vendedor_varias_materias(self):
        entrada:list[tuple[str, str, int]] = [
            ('Juan', 'Monitor', 5),
            ('Juan', 'PC', 6),
            ('Juan', 'Teclado', 9),
            ('Juan', 'Modem', 9)
        ]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        
        salida = {
            'Juan':[('Monitor', 5), ('PC', 6), ('Teclado', 9),
            ('Modem', 9)]
        }
        res = gestion_ventas(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_valores_minimas_y_maximas(self):
        entrada = [("Pedro", "Auriculares", 1), ("Lucía", "PenDrive", 10)]
        esperado = {
            "Pedro": [("Auriculares", 1)],
            "Lucía": [("PenDrive", 10)]
        }
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        res = gestion_ventas(entrada)
        self.assertDictEqualWithUnorderedLists(res, esperado)
        self.assertEqual(entrada, entrada_copia)

    def assertDictEqualWithUnorderedLists(self, dict1, dict2):
            self.assertEqual(dict1.keys(), dict2.keys(), "Los diccionarios tienen distintias claves.")
            
            for key in dict1:
                self.assertCountEqual(dict1[key], dict2[key], f"Las listas de la clave '{key}' no son iguales")


if __name__ == '__main__':
    unittest.main(verbosity=2)
