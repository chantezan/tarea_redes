import unittest
from red import Red

class TestRed(unittest.TestCase):
    def test1(self):
        red = Red(cantidad=[1])
        red.capas[0][0].bias = 0.5
        red.capas[0][0].peso[0] = 0.4
        red.capas[0][0].peso[1] = 0.3
        red.capas[1][0].bias = 0.4
        red.capas[1][0].peso[0] = 0.3
        red.entrenar([[1,1]],[[1]],[],[],epocas=1)
        self.assertEqual(0.502101508999489 , red.capas[0][0].bias)
        self.assertEqual(0.40210150899948904, red.capas[0][0].peso[0])
        self.assertEqual(0.302101508999489 , red.capas[0][0].peso[1])
        self.assertEqual(0.43937745312797394, red.capas[1][0].bias)
        self.assertEqual(0.33026254863991883, red.capas[1][0].peso[0])

if __name__ == '__main__':
    unittest.main()