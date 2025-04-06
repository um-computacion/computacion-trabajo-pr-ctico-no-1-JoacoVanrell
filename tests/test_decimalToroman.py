import unittest
import sys
import os

# Agrega la carpeta 'src' al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importa la función desde el archivo correcto
from funciones_decimalToroman import decimal_a_romano

class TestDecimalARomano(unittest.TestCase):
   
    def test_numero_1(self):
        self.assertEqual(decimal_a_romano(1), 'I')

    def test_numero_2(self):
        self.assertEqual(decimal_a_romano(2), 'II')

    def test_numero_3(self):
        self.assertEqual(decimal_a_romano(3), 'III')

    def test_numero_4(self):
        self.assertEqual(decimal_a_romano(4), 'IV')

    def test_numero_5(self):
        self.assertEqual(decimal_a_romano(5), 'V')

    def test_numero_9(self):
        self.assertEqual(decimal_a_romano(9), 'IX')

    def test_numero_10(self):
        self.assertEqual(decimal_a_romano(10), 'X')

    def test_numero_40(self):
        self.assertEqual(decimal_a_romano(40), 'XL')

    def test_numero_50(self):
        self.assertEqual(decimal_a_romano(50), 'L')

    def test_numero_90(self):
        self.assertEqual(decimal_a_romano(90), 'XC')

    def test_numero_100(self):
        self.assertEqual(decimal_a_romano(100), 'C')

    def test_numero_400(self):
        self.assertEqual(decimal_a_romano(400), 'CD')

    def test_numero_500(self):
        self.assertEqual(decimal_a_romano(500), 'D')

    def test_numero_900(self):
        self.assertEqual(decimal_a_romano(900), 'CM')

    def test_numero_1000(self):
        self.assertEqual(decimal_a_romano(1000), 'M')

    def test_numero_1994(self):
        self.assertEqual(decimal_a_romano(1994), 'MCMXCIV')

    def test_numero_3999(self):
        self.assertEqual(decimal_a_romano(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
