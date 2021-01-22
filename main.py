import os
from getpass import getpass
from lib.Shamir_SS import cifrar, descifrar

def menu_cifrar():
    """
    Cifrar archivo interactivo

    Función que pide un archivo en la línea de comandos, y lo cifra
    """
    nombre_cifrado = leer_nombre_archivo('Archivo a cifrar:                                   ', 'No se encontró el archivo a cifrar')
    contenido = leer_archivo(nombre_cifrado)
    nombre_arch_evaluaciones = input('Archivo donde se guardarán las evaluaciones:        ')
    n_evaluaciones = leer_natural('Número de evaluaciones a generar:                   ')
    necesarios = leer_natural('Número de evaluaciones necesarias:                  ')
    contrasenia = getpass('Contraseña:                        ')

    (contenido_cifrado, evaluaciones) = cifrar.cifra (contenido, n_evaluaciones, necesarios, contrasenia)

    # escribir
    escribir_archivo(nombre_cifrado + ".aes", contenido_cifrado)
    escribir_archivo(nombre_arch_evaluaciones, evaluaciones_toString(evaluaciones).encode())

def menu_descifrar():
    """
    Descrifrar archivo interactivo

    Función qué descrifra pide un archivo y evaluaciones, y lo descifra
    """
    archivo_cifrado = leer_nombre_archivo('Archivo a descifrar:       ', 'No se encontró el archivo a descifrar')
    archivo_evaluaciones = leer_nombre_archivo('Archivo con evaluaciones:  ', 'No se econtró el archivo con las evaluaciones')
    contenido = leer_archivo(archivo_cifrado)
    (xs, ys) = leer_evaluaciones(archivo_evaluaciones)

    try:
        contenido_descifrado = descifrar.descifra (contenido, xs, ys)

        # escribir
        nom_original = nombre_original(archivo_cifrado)
        escribir_archivo(nom_original, contenido_descifrado)

    except ValueError:
        print("\nNo se pudo descifrar el archivo")

def leer_archivo(nombre):
    """
    Leer archivo

    Función que lee un archivo que recibe como parámetro

    Parameters
    ----------
    nombre: string
        Nombre del archivo que se va a abrir
    Returns
    -------
    string
        Contenido del archivo
    """
    with open(nombre, "rb") as lector:
        contenido = lector.read()
    return contenido

def escribir_archivo(nombre, contenido):
    """
    Escribir archivo

    Función que escribe en un archivo un contenido que recibe como parámetros

    Parameters
    ----------
    nombre: string
        Nombre del archivo que se va a escribir
    contenido: bytes
        Datos a guardar en el archivo
    """
    with open(nombre, "wb") as f:
        f.write(contenido)

def leer_evaluaciones(archivo_evaluaciones):
    """
    Leer archivo con evaluaciones

    Función que lee un archivo con evaluaciones que recibe como parámetro

    Parameters
    ----------
    nombre: string
        Nombre del archivo que se va a abrir
    Returns
    -------
    (list, list)
        Las evaluaciones que estaban en el archivo
    """
    x = []
    y = []

    evaluaciones = open(archivo_evaluaciones, "r")
    while(True):
        punto = evaluaciones.readline()
        if not punto:
            break
        p = punto.split(", ")
        if (len(p) != 2):
            raise NameError('El archivo de evaluaciones está incompleto.')
        x.append(int(p[0]))
        y.append(int(p[1]))
    evaluaciones.close()

    if(len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        raise NameError('El archivo de evaluaciones está incompleto.')

    return (x,y)

def nombre_original(nombre):
    """
    Nombre Original

    Función que recibe el nombre del archivo cifrado, y regresa el original

    Parameters
    ----------
    nombre: string
        Nombre del archivo cifrado
    Returns
    -------
    string
        Nombre del archivo original
    """
    pos = nombre.rfind(".")
    nombre_orig = nombre[:pos]
    return nombre_orig

def leer_natural(mensaje):
    """
    Leer Natural

    Función que lee un natural del usuario

    Parameters
    ----------
    mensaje: string
        Mensaje al pedir el natural
    Returns
    -------
    int
        Número con el natural
    """
    natural = 0
    correcto = False
    while not correcto:
        try:
            natural = int(input(mensaje))
            if(natural > 0):
                correcto = True
        except ValueError:
            print ('Introduce un natural')
    return natural

def leer_nombre_archivo(mensaje, mensajeError):
    """
    Leer nombre de Archivo

    Función que recibe el nombre de un archivo.
    Lanza excepción si no se encontró el archivo.

    Parameters
    ----------
    mensaje: string
        Mensaje al pedir el archivo
    mensaje: mensajeError
        Mensaje de error al no encontrar el archivo
    Returns
    -------
    string
        Cadena con el nombre del archivo
    """
    nombre = input(mensaje)
    if not archivo_existe(nombre, mensajeError):
        raise FileNotFoundError(mensajeError)
    return nombre

def archivo_existe(arch):
    """
    Archivo existe

    Función que revisa si un archivo existe

    Parameters
    ----------
    arch: string
        nombre del archivo a revisar
    Returns
    -------
    boolean
        Booleano, verdadero si existe el archivo
    """
    if not os.path.isfile (arch):
        return False
    return True

def evaluaciones_toString(evaluaciones):
    """
    Evaluaciones a Cadena

    Función que convierte las evaluaciones en cadena

    Parameters
    ----------
    mensaje: evaluaciones
        Lista de tuplas con las evaluaciones (x, y)
    Returns
    -------
    string
        Cadena que representa a las evaluaciones
    """
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
        try:
            menu_cifrar()
        except FileNotFoundError:
            print("No se encontró el archivo a cifrar")
    elif opcion == 'D':
        try:
            menu_descifrar()
        except FileNotFoundError:
            print("No se pudieron encontrar los archivos")
    elif opcion == 'S':
        salir = True
    else:
        print ('Introduce una opción válida')

print ('Hasta luego.')
