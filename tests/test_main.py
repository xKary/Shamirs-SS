import os
import unittest
from unittest import mock
import funciones_main

class testMain(unittest.TestCase):

    def test_leer_archivo(self):
        contenido = str.encode('Buen día')
        #Crear archivo para realizar el test
        with open('prueba.txt', "wb") as f:
            f.write(contenido)

        contenido_leido = funciones_main.leer_archivo('prueba.txt')
        #Eliminar el archivo creado con el proposito de probar
        os.remove('prueba.txt')

        self.assertEqual(contenido_leido, contenido)

    def test_escribir_archivo(self):
        contenido = str.encode('Buen día')
        funciones_main.escribir_archivo('prueba.txt',contenido)

        escribio_archivo = os.path.isfile('prueba.txt')
        #Eliminar el archivo creado con el proposito de probar
        os.remove('prueba.txt')

        self.assertEqual(escribio_archivo,True)

    def test_leer_evaluaciones(self):
        evaluaciones = "1, 2\n5, 6\n10, 15\n"
        #Crear archivo para realizar el test
        with open('prueba.txt', "w") as f:
            f.write(evaluaciones)

        esperado= ([1,5,10],[2,6,15])
        resultado_main = funciones_main.leer_evaluaciones('prueba.txt')
        #Eliminar el archivo creado con el proposito de probar
        os.remove('prueba.txt')

        self.assertEqual(resultado_main, esperado)

    def test_nombre_original(self):
        nombre_orig = funciones_main.nombre_original('prueba.txt.aes')
        self.assertEqual(nombre_orig, 'prueba.txt')

    @mock.patch('funciones_main.input', create = True)
    def test_leer_entero(self,mocked_input):
        mocked_input.side_effect = '5'
        n_main = funciones_main.leer_entero('Natural')
        self.assertEqual(n_main, 5)

    def test_archivo_existe(self):
        archivo = 'prueba'
        existe_main = funciones_main.archivo_existe(archivo)
        self.assertEqual(existe_main, False)

    def evaluaciones_toString(self):
        evaluaciones = [[1,2],[5,6],[10,15]]
        esperado = "1, 2\n5, 6\n10,15\n"
        resultado_main = funciones_main.evaluaciones(evaluaciones)
        self.assertEqual(resultado_main, esperado)

if __name__ == '__main__':
    unittest.main()
