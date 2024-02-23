import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):

    def test_palindromo_con_puntuacion(self):
        self.assertTrue(palindromo(""))

if __name__ == '__main__':
    unittest.main()