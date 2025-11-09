import unittest
from parcial import mantuvieron_residencia

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
        self.method = mantuvieron_residencia

    def test_sin_habitantes(self):
        censo1 = {}
        censo2 = {}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_una_sola_persona_mantiene(self):
        censo1 = {'Juan': 'Merlo'}
        censo2 = {'Juan': 'Merlo'}
        esperado = {'Merlo': 1}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_una_sola_persona_se_muda(self):
        censo1 = {'Juan': 'Merlo'}
        censo2 = {'Juan': 'Castelar'}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_sin_residencia_mantenida(self):
        censo1 = {'Armando': 'San Miguel',
                  'Julieta': 'Ezeiza'}
        censo2 = {'Armando': 'La Matanza',
                  'Julieta': 'Zarate'}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)
        
    def test_residencia_mantenida_en_una_localidad(self):
        censo1 = {'Juan': 'Merlo', 'Ana': 'Merlo'}
        censo2 = {'Juan': 'Castelar', 'Ana': 'Merlo'}
        esperado = {'Merlo': 1}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_residencia_mantenida_en_varias_localidades(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Florencio Varela',
                  'Ignacio': 'Ciudad Autónoma de Buenos Aires',
                  'Malena': 'Berazategui',
                  'Oriana': 'Ciudad Autónoma de Buenos Aires',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        esperado = {'Florencio Varela': 1, 'Quilmes': 2}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_todos_mantienen_residencia(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Oriana': 'San Miguel',
                  'Malena': 'Avellaneda',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        esperado = {'Florencio Varela': 1, 'Quilmes': 3, 'La Plata': 1, 'Avellaneda': 1, 'San Miguel': 1}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_todos_se_mudan(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Ezeiza',
                  'Tony': 'Avellaneda',
                  'Oriana': 'Quilmes',
                  'Malena': 'La Plata',
                  'Gonzalo': 'San Isidro',
                  'Ignacio': 'Florencio Varela',
                  'Maria': 'Berazategui'}
        
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_residencias_cruzadas_no_mantenidas(self):
        censo1 = {'Armando': 'San Miguel',
                  'Julieta': 'Ezeiza'}
        censo2 = {'Armando': 'Ezeiza',
                  'Julieta': 'San Miguel'}
        esperado = {}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)

    def test_no_modifica_inputs(self):
        censo1 = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo1_copia = {'Carolina': 'Florencio Varela',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'La Plata',
                  'Ignacio': 'Quilmes',
                  'Malena': 'Avellaneda',
                  'Oriana': 'San Miguel',
                  'Maria': 'Quilmes'}
        
        censo2 = {'Carolina': 'Florencio Varela',
                  'Ignacio': 'Ciudad Autónoma de Buenos Aires',
                  'Malena': 'Berazategui',
                  'Oriana': 'Ciudad Autónoma de Buenos Aires',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        censo2_copia = {'Carolina': 'Florencio Varela',
                  'Ignacio': 'Ciudad Autónoma de Buenos Aires',
                  'Malena': 'Berazategui',
                  'Oriana': 'Ciudad Autónoma de Buenos Aires',
                  'Tony': 'Quilmes',
                  'Gonzalo': 'Quilmes',
                  'Maria': 'Quilmes'}
        
        esperado = {'Florencio Varela': 1, 'Quilmes': 2}
        self.assertEqual(mantuvieron_residencia(censo1, censo2), esperado)
        self.assertEqual(censo1, censo1_copia)
        self.assertEqual(censo2, censo2_copia)
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
