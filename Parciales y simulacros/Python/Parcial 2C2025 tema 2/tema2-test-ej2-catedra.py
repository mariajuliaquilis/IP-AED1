import unittest
from queue import LifoQueue as Pila
from solucion import buscar_cliente_prioritario

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
        self.method = buscar_cliente_prioritario

    def test_un_elem(self):
        clientes = crear_pila ([("Caro","bitcoin",120)] )
        clientes_final = crear_pila ( [] )


        res: str = buscar_cliente_prioritario(clientes)        
        self.assertEqual(res, "Caro")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_prioritario_al_prinfipio(self):
        clientes = crear_pila ([("Cacho","debito",10), ("Juan","debito",10), ("Caro","bitcoin",120)] )
        clientes_final = crear_pila ( [("Cacho","debito",10), ("Juan","debito",10)] )


        res: str = buscar_cliente_prioritario(clientes)        
        self.assertEqual(res, "Caro")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_prioritario_en_el_medio(self):
        clientes = crear_pila ([("Cacho","debito",10), ("Sol","bitcoin",120), ("Juan","debito",10)] )
        clientes_final = crear_pila ( [("Cacho","debito",10), ("Juan","debito",10)] )


        res: str = buscar_cliente_prioritario(clientes)        
        self.assertEqual(res, "Sol")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_prioritario_al_final(self):
        clientes = crear_pila ([ ("Lau","bitcoin",120),  ("Cacho","debito",10), ("Juan","debito",10)] )
        clientes_final = crear_pila ( [("Cacho","debito",10), ("Juan","debito",10)] )

        res: str = buscar_cliente_prioritario(clientes)        
        self.assertEqual(res, "Lau")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_varios_candidatos(self):
        clientes = crear_pila ([ ("Caro","bitcoin",120),  ("Cacho","debito",10), ("Juan","debito",10), ("Juana","bitcoin",120)] )
        clientes_final = crear_pila ( [  ("Cacho","debito",10), ("Juan","debito",10), ("Juana","bitcoin",120)] )

        res: str = buscar_cliente_prioritario(clientes)        
        self.assertEqual(res, "Caro")
        self.assertEqual(clientes.queue, clientes_final.queue)
        
    def test_varios_candidatos_justo(self):
        clientes = crear_pila ([ ("Caro","bitcoin",100),  ("Cacho","debito",10), ("Juan","debito",10), ("Luis","bitcoin",101), ("Juana","bitcoin",120)] )
        clientes_final = crear_pila ( [ ("Caro","bitcoin",100),  ("Cacho","debito",10), ("Juan","debito",10), ("Juana","bitcoin",120)] )

        res: str = buscar_cliente_prioritario(clientes)        
        self.assertEqual(res, "Luis")
        self.assertEqual(clientes.queue, clientes_final.queue)

    
def crear_pila(elementos):
    pila = Pila()
    for elem in elementos:
        pila.put(elem)
    return pila
    
    
if __name__ == '__main__':
        unittest.main(verbosity=2)