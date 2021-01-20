import os
from getpass import getpass
from lib.Shamir_SS import cifrar, descifrar

def menu_cifrar():
    nombre_cifrado = input('Archivo a cifrar:                  ')
    if not archivo_existe(nombre_cifrado, 'No se encontró el archivo a cifrar'):
        return
    nombre_arch_evaluaciones = input('Archivo donde se guardarán las evaluaciones:           ')
    n_evaluaciones = leer_natural('Número de evaluaciones requeridas: ')
    necesarios = leer_natural('Número de puntos necesarios:       ')
    contrasenia = getpass('Contraseña:                        ')

    contenido = leer_archivo(nombre_cifrado)

    (contenido_cifrado, evaluaciones) = cifrar.cifra (contenido, n_evaluaciones, necesarios, contrasenia)

    # escribir
    escribir_archivo(nombre_cifrado + ".aes", contenido_cifrado)
    cadena = ""
    for (x,y) in evaluaciones:
        cadena += str(x) + ", " + str(y) + "\n"
    escribir_archivo(nombre_arch_evaluaciones, cadena.encode())

    # borrar el viejito
    os.remove(nombre_cifrado)

def menu_descifrar():
    archivo_cifrado = input('Archivo a descifrar:       ')
    if not archivo_existe(archivo_cifrado, "No se encontró el archivo a descifrar"):
        return

    archivo_evaluaciones = input ('Archivo con evaluaciones:  ')
    if not archivo_existe(archivo_evaluaciones, "No se econtró el archivo con las evaluaciones"):
        return


    contenido = leer_archivo(archivo_cifrado)
    (xs, ys) = leer_evaluaciones(archivo_evaluaciones)

    contenido_descifrado = descifrar.descifra (contenido, xs, ys)

    # escribir
    nom_original = nombre_original(archivo_cifrado)
    escribir_archivo(nom_original, contenido_descifrado)

    # borrar el viejito
    os.remove(archivo_cifrado)
    os.remove(archivo_evaluaciones)

def leer_archivo(nombre):
    with open(nombre, "rb") as lector:
        contenido = lector.read()
    return contenido

def escribir_archivo(nombre, contenido):
    with open(nombre, "wb") as f:
        f.write(contenido)

def leer_evaluaciones(archivo_evaluaciones):
    x = []
    y = []

    evaluaciones = open(archivo_evaluaciones, "r")
    while(True):
        punto = evaluaciones.readline()
        if not punto:
            break
        p = punto.split(", ")
        x.append(int(p[0]))
        y.append(int(p[1]))
        # if not linea:
        #     break
    evaluaciones.close()

    if(len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        raise NameError('El archivo de evaluaciones está incompleto.')

    return (x,y)

def nombre_original(nombre):
    pos = nombre.rfind(".")
    nombre_orig = nombre[:pos]
    return nombre_orig

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
