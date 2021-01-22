"""
Módulo que se encarga de la interacción con el usuario.
"""
import funciones_main

salir = False
opcion = ''

while not salir:
    print ('\nMenú')
    print ('C. Cifrar')
    print ('D. Descifrar')
    print ('S. Salir')

    print ('Elige una opcion: \t', end = '')

    opcion = input().upper()

    if opcion == 'C':
        try:
            funciones_main.menu_cifrar()
        except FileNotFoundError:
            print("No se encontró el archivo a cifrar.")
    elif opcion == 'D':
        try:
            funciones_main.menu_descifrar()
        except FileNotFoundError:
            print("No se pudieron encontrar los archivos.")
    elif opcion == 'S':
        salir = True
    else:
        print ('Introduce una opción válida.')

print ('Hasta luego.')
