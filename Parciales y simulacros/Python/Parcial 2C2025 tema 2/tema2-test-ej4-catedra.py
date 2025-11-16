import unittest
from queue import LifoQueue as Pila
from solucion import peliculas_mas_vistas

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
        self.method = peliculas_mas_vistas

    def test_un_solo_cliente(self):
        entrada:dict[str,str] = {
            'Ana': 'Avatar'
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Avatar': 1
        } 


        res:dict[str, int] = peliculas_mas_vistas(entrada, 1)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)

    def test_varias_peliculas_cumplen(self):
        entrada:dict[str,str] = {
            'Beto': 'Rio',
            'Ana': 'Endgame',
            'Caro': 'Rio',
            'Diego': 'Titanic',
            'Leo': 'Endgame',
            'Ian': 'Rio'
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Endgame': 2,
            'Rio': 3
        } 


        res:dict[str, int] = peliculas_mas_vistas(entrada, 2)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)

    def test_minimo_umbral(self):
        entrada:dict[str,str] = {
            'Beto': 'Rio',
            'Ana': 'Endgame',
            'Caro': 'Rio',
            'Diego': 'Rio',
            'Leo': 'Endgame',
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Endgame': 2,
            'Rio': 3
        } 


        res:dict[str, int] = peliculas_mas_vistas(entrada, 1)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)

    def test_al_menos_una_favorita(self):
        entrada:dict[str,str] = {
            'Beto': 'Endgame',
            'Ana': 'Avatar',
            'Caro': 'Rio',
            'Diego': 'Titanic'
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Endgame': 1,
            'Avatar': 1,
            'Rio': 1,
            'Titanic': 1
        } 


        res:dict[str, int] = peliculas_mas_vistas(entrada, 1)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)    

    def test_todas_favoritas(self):
        entrada:dict[str,str] = {
            'Beto': 'Endgame',
            'Ana': 'Endgame',
            'Caro': 'Rio',
            'Diego': 'Rio',
            'Leo': 'Avatar',
            'Ian': 'Avatar'
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Endgame': 2,
            'Rio': 2,
            'Avatar': 2,
        }
        res:dict[str, int] = peliculas_mas_vistas(entrada, 1)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)   

    def test_una_sola_cumple_varias_quedan_fuera(self):
        entrada:dict[str,str] = {
            'Beto': 'Endgame',
            'Ana': 'Matrix',
            'Caro': 'Titanic',
            'Diego': 'Rio',
            'Leo': 'Endgame',
            'Ian': 'Avatar'
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Endgame': 2
        }


        res:dict[str, int] = peliculas_mas_vistas(entrada, 2)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada) 

    def test_todos_prefieren_misma_pelicula(self):
        entrada:dict[str,str] = {
            'Beto': 'Rio',
            'Ana': 'Rio',
            'Caro': 'Rio',
            'Diego': 'Rio',
            'Leo': 'Rio',
            'Ian': 'Rio'
        }
        copia_entrada:dict[str, str] = entrada.copy()
        salida_esperada:dict[str, int] =  {
            'Rio': 6,
        }


        res:dict[str, int] = peliculas_mas_vistas(entrada, 6)        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
        
if __name__ == '__main__':
        unittest.main(verbosity=2)