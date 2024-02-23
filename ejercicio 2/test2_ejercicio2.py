import unittest
from ejercicio2 import definir_campeon

class TestDefinirCampeon(unittest.TestCase):
    
    def test_varios_campeones(self):

        # Caso de prueba donde hay múltiples campeones
        posiciones = [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
        sistema = (3, [1, 1, 1])
        resultado = definir_campeon(posiciones, sistema)
        self.assertEqual(resultado, {'3', '1', '2'})

if __name__ == '__main__':
    unittest.main()
