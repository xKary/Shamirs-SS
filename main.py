import os
from getpass import getpass
from lib.Shamir_SS import cifrar, descifrar

def menu_cifrar():
    nombre_cifrado = leer_nombre_archivo('Archivo a cifrar:                  ', 'No se encontró el archivo a cifrar')
    contenido = leer_archivo(nombre_cifrado)
    nombre_arch_evaluaciones = input('Archivo donde se guardarán las evaluaciones:           ')
    n_evaluaciones = leer_natural('Número de evaluaciones a generar: ')
    necesarios = leer_natural('Número de evaluaciones necesarias:       ')
    contrasenia = getpass('Contraseña:                        ')

    (contenido_cifrado, evaluaciones) = cifrar.cifra (contenido, n_evaluaciones, necesarios, contrasenia)

    # escribir
    escribir_archivo(nombre_cifrado + ".aes", contenido_cifrado)
    escribir_archivo(nombre_arch_evaluaciones, evaluaciones_toString(evaluaciones).encode())

    # borrar el viejito
    os.remove(nombre_cifrado)

def menu_descifrar():
    archivo_cifrado= leer_nombre_archivo('Archivo a descifrar:       ', 'No se encontró el archivo a descifrar')
    archivo_evaluaciones = leer_nombre_archivo('Archivo con evaluaciones: ', 'No se econtró el archivo con las evaluaciones')
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
        if (len(p) != 2):
            raise NameError('El archivo de evaluaciones está incompleto')
        x.append(int(p[0]))
        y.append(int(p[1]))
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

def leer_nombre_archivo(mensaje, mensajeError):
    nombre = input(mensaje)
    if not archivo_existe(nombre, mensajeError):
        raise FileNotFoundError(mensajeError)
    return nombre

def archivo_existe(arch, mensaje_error):
    if not os.path.isfile (arch):
        return False
    return True

def evaluaciones_toString(evaluaciones):
    cadena = ""
    for (x,y) in evaluaciones:
        cadena += str(x) + ", " + str(y) + "\n"
    return cadena

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
        print ('vamos a cifrar\n')
        try:
            menu_cifrar()
        except FileNotFoundError:
            print("No se encontró el archivo a cifrar")
    elif opcion == 'D':
        print ('vamos a descifrar')
        menu_descifrar()
    elif opcion == 'S':
        salir = True
    else:
        print ('Introduce una opción válida')

print ('Hasta luego.')
