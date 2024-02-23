import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):

    def test_es_palindromo(self):
        self.assertTrue(palindromo("radar"))
        self.assertTrue(palindromo("anita lava la tina"))


if __name__ == '__main__':
    unittest.main()