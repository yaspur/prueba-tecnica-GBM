import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):

    def test_no_es_palindromo(self):
        self.assertFalse(palindromo("Yasid"))
        self.assertFalse(palindromo("GBM"))

if __name__ == '__main__':
    unittest.main()