import unittest
from lib.Shamir_SS import cifrar
from lib.Shamir_SS import descifrar

class testCifrar(unittest.TestCase):
    def test_evalua_polinomio(self):
        self.assertEqual(cifrar.evalua_polinomio(0, [1, 2]), 1)
        self.assertEqual(cifrar.evalua_polinomio(0, [0, 2]), 0)

        self.assertEqual(cifrar.evalua_polinomio(1, [0, 2, 5]), 7)
        self.assertEqual(cifrar.evalua_polinomio(3, [2, 4, 3, 7]), 230)

    def test_genera_aleatorios(self):
        cero = len(cifrar.genera_aleatorios(0))
        diez = len(cifrar.genera_aleatorios(10))

        self.assertEqual(cero, 0)
        self.assertEqual(diez, 10)

        aleatorios = cifrar.genera_aleatorios(10_000)
        aleatorios.sort()
        for i in range(1, len(aleatorios)):
            self.assertNotEqual(aleatorios[i-1], aleatorios[i])

    def test_cifra(self):
        contenido = "texto a cifrar"
        (cifrado, shares) = cifrar.cifra(contenido.encode("utf-8"), 3, 2, "llave")
        self.assertEqual(len(shares), 3)
        self.assertNotEqual(contenido.encode("utf-8"), cifrado)
        self.assertFalse(contenido.encode("utf-8") in cifrado)

        shares.pop()
        valores = list(zip(*shares))
        descifrado = descifrar.descifra(cifrado, valores[0], valores[1])
        self.assertEqual(contenido, str(descifrado, "utf-8"))

if __name__ == '__main__':
    unittest.main()
