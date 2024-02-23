import unittest
from ejercicio2 import definir_campeon

class TestDefinirCampeon(unittest.TestCase):
    
    def test_definir_campeon(self):
        # Caso de prueba donde hay un único campeón
        posiciones = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        sistema = (3, [10, 8, 6])
        resultado = definir_campeon(posiciones, sistema)
        self.assertEqual(resultado, {'1'})


if __name__ == '__main__':
    unittest.main()
