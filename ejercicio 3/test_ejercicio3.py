import unittest
from ejercicio3 import calculo_min_steps

class TestSteps(unittest.TestCase):

    def test_steps(self):
        # Llama a la función y verifica si la salida es la esperada
        self.assertEqual(calculo_min_steps(1), 1)
        self.assertEqual(calculo_min_steps(2), 3)
        self.assertEqual(calculo_min_steps(3), 2)
        self.assertEqual(calculo_min_steps(4), 3)
        self.assertEqual(calculo_min_steps(5), 4)

if __name__ == '__main__':
    unittest.main()
