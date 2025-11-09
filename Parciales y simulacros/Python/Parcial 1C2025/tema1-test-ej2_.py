import unittest
from queue import Queue as Cola
from parcial import pasar_por_autoservicio

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        self.method = pasar_por_autoservicio
    
    def test_unico_cliente_se_retira(self):
        clientes = crear_cola([("Pedro", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Pedro")
    
    def test_unico_cliente_se_retira_y_cola_queda_vacia(self):
        clientes = crear_cola([("Juana", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Juana")

        self.assertTrue(clientes.empty())
    
    def test_cliente_al_final_de_la_cola_se_retira(self):
        clientes = crear_cola([("Ana", "efectivo", 13), ("Juan", "qr", 22), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Bruno")
    
    def test_cliente_al_inicio_de_la_cola_se_retira(self):
        clientes = crear_cola([("Jessica", "tarjeta", 14), ("Ana", "efectivo", 13), ("Juan", "qr", 22)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Jessica")
    
    def test_cliente_al_medio_de_la_cola_se_retira(self):
        clientes = crear_cola([("Juan", "qr", 22), ("Jorge", "tarjeta", 14), ("Ana", "efectivo", 13)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Jorge")
    
    def test_cliente_al_medio_de_la_cola_se_retira_y_el_resto_quedan(self):
        clientes = crear_cola([("Juan", "tarjeta", 22), ("Silvia", "qr", 14), ("Ana", "efectivo", 13)])
        clientes_final = crear_cola([("Juan", "tarjeta", 22), ("Ana", "efectivo", 13)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Silvia")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_selecciona_al_primer_cliente_con_varios_candidatos(self):
        clientes = crear_cola([("Juan", "qr", 22), ("Mercedes", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "efectivo", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Mercedes")

    def test_selecciona_al_primer_cliente_con_varios_candidatos_y_el_resto_quedan(self):
        clientes = crear_cola([("Juan", "qr", 22), ("Mercedes", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "efectivo", 13), ("Bruno", "tarjeta", 14)])
        clientes_final = crear_cola([("Juan", "qr", 22), ("Pedro", "transferencia", 12), ("Ana", "efectivo", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Mercedes")
        self.assertEqual(clientes.queue, clientes_final.queue)

    def test_selecciona_al_primer_cliente_con_todos_candidatos(self):
        clientes = crear_cola([("Marcelo", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "qr", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Marcelo")

    def test_selecciona_al_primer_cliente_con_todos_candidatos_y_el_resto_quedan(self):
        clientes = crear_cola([("Marcelo", "qr", 8), ("Pedro", "transferencia", 12), ("Ana", "qr", 13), ("Bruno", "tarjeta", 14)])
        clientes_final = crear_cola([("Pedro", "transferencia", 12), ("Ana", "qr", 13), ("Bruno", "tarjeta", 14)])
        resultado = pasar_por_autoservicio(clientes)

        self.assertEqual(resultado, "Marcelo")
        self.assertEqual(clientes.queue, clientes_final.queue)

def crear_cola(elementos):
    cola = Cola()
    for elem in elementos:
        cola.put(elem)
    return cola

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
