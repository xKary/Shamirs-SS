import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../lib")
from Shamir_SS import descifrar
from Shamir_SS import cifrar

class testDescifrar(unittest.TestCase):
    def test_polinomio_base(self):
        #test de lógica cuestionable
        valores_x = [25]
        self.assertEqual(descifrar.polinomio_base(0, valores_x), 1)
        #unos mas razonables
        #Para 2 puntos
        valores_x = [0,10]
        pol_base = descifrar.polinomio_base(1,valores_x)
        self.assertEqual(pol_base, 0)

        valores_x = [0,10]
        pol_base = descifrar.polinomio_base(0,valores_x)
        self.assertEqual(pol_base, 1)

    def test_interpolacion_lagrange(self):
        # poly (7,3,4)
        valores_x = [10, 27, -65]
        valores_y = [734, 5188, 29384]
        interpolacion = descifrar.interpolacion_Lagrange(valores_x, valores_y)
        self.assertEqual(interpolacion, 4)
        # poly (65, 2000, 37456, 878876, 4567, 0)
        valores_x = [1,2,3,4,5,6]
        valores_y = [922964, 3858366, 9112692, 17056028, 28129860, 42854874]
        interpolacion = descifrar.interpolacion_Lagrange(valores_x, valores_y)
        self.assertEqual(interpolacion, 0)
        # poly (2x+47)
        valores_x = [1,356666666666666666666666666]
        valores_y = [49, 713333333333333333333333379]
        interpolacion = descifrar.interpolacion_Lagrange(valores_x, valores_y)
        self.assertEqual(interpolacion, 47)

    def test_descifra(self):
        #basicamente checa compatibilidad con cifrar
        (texto_cifrado, shares) = cifrar.cifra("Prueba :!".encode("utf-8"), 10, 3, "llave")
        valores = list(zip(*shares))
        resultado = descifrar.descifra(texto_cifrado, valores[0], valores[1])
        self.assertEqual("Prueba :!", resultado)

if __name__ == '__main__':
    unittest.main()
