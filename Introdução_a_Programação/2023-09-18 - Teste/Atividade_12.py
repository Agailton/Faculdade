import unittest
from atividade_01 import multiplicar
from atividade_01 import dividir

class TestMultiplicar(unittest.TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(multiplicar(2,3), 6)

    def test_multiplicar_quatro_por_dez(self):
        self.assertEqual(multiplicar(4, 10), 40)

class TestDividir(unittest.TestCase):

    def test_dividir_10_por_2(self):
        self.assertEqual(dividir(10,2), 5)

if __name__ == '__main__':
    unittest.main()