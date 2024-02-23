import unittest
from ejercicio2 import definir_campeon

class TestDefinirCampeon(unittest.TestCase):
    
    def test_definir_campeon(self):
        # Caso de prueba donde hay un único campeón
        posiciones = [[1, 2, 3, 4, 5], [10, 1, 2, 3, 4], [9, 10, 1, 2, 3]]
        sistema = (5, [5, 4, 3, 2, 1])
        resultado = definir_campeon(posiciones, sistema)
        self.assertEqual(resultado, {'1'})


if __name__ == '__main__':
    unittest.main()
