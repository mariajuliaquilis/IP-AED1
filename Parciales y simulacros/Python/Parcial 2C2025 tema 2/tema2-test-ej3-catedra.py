import unittest
from queue import LifoQueue as Pila
from solucion import eliminar_fila_que_mas_suma

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
        self.method = eliminar_fila_que_mas_suma

    def test_una_fila(self):
        entrada:list[int] = [[1,2,3]] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =  [] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
        
    def test_mas_suma_al_principio(self):
        entrada:list[int] = [[10,2,3], [1,2,1], [10,2,1] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [[1,2,1], [10,2,1]] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
        
    def test_mas_suma_en_el_medio(self):
        entrada:list[int] = [[10,2,3], [1,20,1], [10,2,1] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [[10,2,3], [10,2,1]] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
        
    def test_mas_suma_al_final(self):
        entrada:list[int] = [[10,2,3], [1,2,1], [10,2,41] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [[10,2,3], [1,2,1]] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
        
    def test_mas_de_una(self):
        entrada:list[int] = [[10,2,3], [1,2,1], [5,5,5] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [ [1,2,1]] 
        
    def test_todas(self):
        entrada:list[int] = [[10,2,3], [1,2,12], [5,5,5] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [ ] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
    
    def test_ceros(self):
        entrada:list[int] = [[0,-2,-3], [0,0, 0], [-10,2,1] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [[0,-2,-3], [-10,2,1]] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
    
    def test_negativos(self):
        entrada:list[int] = [[-10,-2,-3], [-10,-1, -20], [-10,-2,-1] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [[-10,-2,-3], [-10,-1, -20],] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
    
    def test_una_columna(self):
        entrada:list[int] = [[0], [2], [-10] ] 
        copia_entrada:list[int] = entrada.copy()
        salida_esperada:list[int] =   [[0], [-10]] 


        res:list[int] = eliminar_fila_que_mas_suma (entrada )        
        self.assertEqual(res, salida_esperada)
        self.assertEqual(entrada, copia_entrada)
        
        
if __name__ == '__main__':
        unittest.main(verbosity=2)