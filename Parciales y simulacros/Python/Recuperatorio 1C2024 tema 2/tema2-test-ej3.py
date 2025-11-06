import unittest
import ip_unittest
from queue import Queue as Cola
from solucion import reordenar_cola_primero_numerosas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej3Test(ip_unittest.UnitTest):
    def __init__(self, *args, **kwargs):
        super(Ej3Test, self).__init__(*args, **kwargs)
        self.method = reordenar_cola_primero_numerosas

    def test_trivial(self):
        cola_entrada:Cola[tuple[str,int]] = Cola()
        # cola_pre:Cola[tuple[str,int]] = copiar_cola(cola_entrada)
        umbral:int = 0 
        res:Cola[tuple[str,int]] = reordenar_cola_primero_numerosas(cola_entrada,umbral)
        self.assertTrue(res.empty)

        # La cola de entrada no se modifica
        # self.assertEqual(cola_entrada.queue, cola_pre.queue)
    
    def test_un_paquete(self):
        cola_entrada:Cola[tuple[str,int]] = Cola()
        cola_entrada.put(('A', 10))
        # cola_pre:Cola[tuple[str,int]] = copiar_cola(cola_entrada)
        umbral:int = 10
        
        salida:Cola[tuple[str,int]] = Cola()
        salida.put(('A', 10))
        
        res:Cola[tuple[str,int]] = reordenar_cola_primero_numerosas(cola_entrada,umbral)
        self.assertEqual(res.queue, salida.queue)

        # La cola de entrada no se modifica
        # self.assertEqual(cola_entrada.queue, cola_pre.queue)
    
    def test_varios_paquetes_variado_peso(self):
        cola_entrada:Cola[tuple[str,int]] = Cola()
        cola_entrada.put(('A', 40))
        cola_entrada.put(('B', 10))
        cola_entrada.put(('C', 39))
        cola_entrada.put(('D', 41))
        # cola_pre:Cola[tuple[str,int]] = copiar_cola(cola_entrada)
        salida:Cola[tuple[str,int]] = Cola()
        salida.put(('A', 40))
        salida.put(('D', 41))
        salida.put(('B', 10))
        salida.put(('C', 39))
        
        umbral:int = 39
        res:Cola[tuple[str,int]] = reordenar_cola_primero_numerosas(cola_entrada,umbral)
        self.assertEqual(res.queue, salida.queue)
        
        # La cola de entrada no se modifica
        # self.assertEqual(cola_entrada.queue, cola_pre.queue)

    def test_todos_ligeros(self):
        paquetes = crear_cola([("P1", 3), ("P2", 2), ("P3", 1)])
        umbral = 5
        esperado = [("P1", 3), ("P2", 2), ("P3", 1)]
        resultado = reordenar_cola_primero_numerosas(paquetes, umbral)
        self.assertEqual(list(resultado.queue), esperado)
    
    def test_umbral_cero(self):
        paquetes = crear_cola([("P1", 5), ("P2", 10), ("P3", 3)])
        umbral = 0
        esperado = [("P1", 5), ("P2", 10), ("P3", 3)]
        resultado = reordenar_cola_primero_numerosas(paquetes, umbral)
        self.assertEqual(list(resultado.queue), esperado)
    
    def test_pesos_iguales_al_umbral(self):
        paquetes = crear_cola([("P1", 5), ("P2", 5), ("P3", 10)])
        umbral = 5
        esperado = [("P3", 10), ("P1", 5), ("P2", 5)]
        resultado = reordenar_cola_primero_numerosas(paquetes, umbral)
        self.assertEqual(list(resultado.queue), esperado)

def crear_cola(elementos):
    cola = Cola()
    for elem in elementos:
        cola.put(elem)
    return cola
    

# def copiar_cola(cola: Cola):
#     elementos = list(cola.queue)
#     nueva_cola = Cola()
#     for e in elementos:
#         nueva_cola.put(e)
#     return nueva_cola


if __name__ == '__main__':
    unittest.main(verbosity=2)

