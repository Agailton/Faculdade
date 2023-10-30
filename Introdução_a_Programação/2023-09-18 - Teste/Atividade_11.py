
import unittest
def somar(a, b):
    return a + b

class TestSoma(unittest.TestCase):

    def teste_soma_positivos(self):
        self.assertEquals(somar(2, 3),5)

    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -1),-2)



