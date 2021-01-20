import os
from getpass import getpass

def menu_cifrar():
    archivo = input('Archivo a cifrar:                  ')
    if not archivo_existe(archivo, 'No se encontró el archivo a cifrar'):
        return
    archivo_cifrado = input('Archivo de evaluaciones:           ')
    evaluaciones = leer_natural('Número de evaluaciones requeridas: ')
    necesarios = leer_natural('Número de puntos necesarios:       ')
    contrasenia = getpass('Contraseña:                        ')

    cifrar (archivo, archivo_cifrado, evaluaciones, necesarios, contrasenia)

def menu_descifrar():
    archivo_cifrado = input('Archivo a descifrar:       ')
    if not archivo_existe(archivo_cifrado, "No se encontró el archivo a descifrar"):
        return

    archivo_evaluaciones = input ('Archivo con evaluaciones:  ')
    if not archivo_existe(archivo_evaluaciones, "No se econtró el archivo con las evaluaciones"):
        return

    descifrar (archivo_cifrado, archivo_evaluaciones)

def leer_natural(mensaje):
    natural = 0
    correcto = False
    while not correcto:
        try:
            natural = int(input(mensaje))
            correcto = True
        except ValueError:
            print ('Introduce un natural')
    return natural

def archivo_existe(arch, mensaje_error):
    if not os.path.isfile (arch):
        print (mensaje_error)
        return False
    return True

salir = False
opcion = ''

while not salir:
    print ('Menú')
    print ('C. Cifrar')
    print ('D. Descifrar')
    print ('S. Salir')

    print ('Elige una opcion: \t', end = '')

    opcion = input().upper()

    if opcion == 'C':
        print ('vamos a cifrar\n')
        menu_cifrar()
    elif opcion == 'D':
        print ('vamos a descifrar')
        menu_descifrar()
    elif opcion == 'S':
        salir = True
    else:
        print ('Introduce una opción válida')

print ('Hasta luego.')
