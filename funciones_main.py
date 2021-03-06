"""
Módulo que contiene todas las funciones necesarias para interactuar
con el usuario.
"""
import os
from getpass import getpass
from rich import print
from rich.console import Console
from lib.Shamir_SS import cifrar, descifrar

def menu_cifrar():
    """
    Cifrar archivo interactivo.

    Función que pide un archivo en la línea de comandos, y lo cifra.
    """
    nombre_cifrado = leer_nombre_archivo('\nArchivo a cifrar:                                   ', 'No se encontró el archivo a cifrar')
    contenido = leer_archivo(nombre_cifrado)
    print
    nombre_arch_evaluaciones = input('Archivo donde se guardarán las evaluaciones:        ')

    #Validar que el número de evaluaciones sea mayor a 2
    while True:
        n_evaluaciones = leer_entero('Número de evaluaciones a generar:                   ')
        if(n_evaluaciones > 2):
            break
        else:
            print('[italic yellow]El número mínimo de llaves generadas debe ser 3.')

    #Validar que las llaves necesarias sean menores o iguales a las generadas
    while True:
        necesarios = leer_entero('Número de evaluaciones necesarias:                  ')
        if(necesarios <= n_evaluaciones and necesarios > 1):
            break
        else:
            print('[italic yellow]El número de llaves necesarias debe ser menor o igual al número de llaves generadas, y mayor a 1.')

    contrasenia = getpass('Contraseña:                        ')

    (contenido_cifrado, evaluaciones) = cifrar.cifra (contenido, n_evaluaciones, necesarios, contrasenia)

    # escribir
    escribir_archivo(nombre_cifrado + ".aes", contenido_cifrado)
    escribir_archivo(nombre_arch_evaluaciones, evaluaciones_toString(evaluaciones).encode())
    print("\n[bold green]El archivo se cifró con éxito.\n")

def menu_descifrar():
    """
    Descrifrar archivo interactivo.

    Función qué descrifra pide un archivo y evaluaciones, y lo descifra
    """
    archivo_cifrado = leer_nombre_archivo('\nArchivo a descifrar:       ', '[bold red]No se encontró el archivo a descifrar')
    archivo_evaluaciones = leer_nombre_archivo('Archivo con evaluaciones:  ', '[bold red]No se econtró el archivo con las evaluaciones')
    contenido = leer_archivo(archivo_cifrado)
    (xs, ys) = leer_evaluaciones(archivo_evaluaciones)

    try:
        contenido_descifrado = descifrar.descifra (contenido, xs, ys)

        # escribir
        nom_original = nombre_original(archivo_cifrado)
        escribir_archivo(nom_original, contenido_descifrado)
        print("\n[bold green]El archivo se descifró con éxito.\n")

    except ValueError:
        print("\n[bold red blink]No se pudo descifrar el archivo")


def leer_archivo(nombre):
    """
    Leer archivo

    Función que lee un archivo que recibe como parámetro.

    @type  nombre: string
    @param nombre: Nombre del archivo que se va a abrir.
    @rtype:   string
    @return:  Contenido del archivo.
    """
    with open(nombre, "rb") as lector:
        contenido = lector.read()
    return contenido

def escribir_archivo(nombre, contenido):
    """
    Escribir archivo

    Función que escribe en un archivo un contenido que recibe como parámetros

    @type  nombre: string
    @param nombre: Nombre del archivo que se va a escribir.
    @type  contenido: bytes
    @param contenido: Datos a guardar en el archivo.
    """
    with open(nombre, "wb") as f:
        f.write(contenido)

def leer_evaluaciones(archivo_evaluaciones):
    """
    Leer archivo con evaluaciones

    Función que lee un archivo con evaluaciones que recibe como parámetro

    @type  archivo_evaluaciones: string
    @param archivo_evaluaciones: Nombre del archivo que se va a abrir.
    @rtype:   (list, list)
    @return:  Las evaluaciones que estaban en el archivo.

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

    @type  nombre: string
    @param nombre: Nombre del archivo cifrado.
    @rtype:   string
    @return:  Nombre del archivo original.
    """
    pos = nombre.rfind(".")
    nombre_orig = nombre[:pos]
    return nombre_orig

def leer_entero(mensaje):
    """
    Leer Entero

    Función que lee valida que el usuario ingrese un número entero.

    @type  mensaje: string
    @param mensaje: Mensaje que se muestra al pedir el entero.
    @rtype:   int
    @return:  Número con el entero.
    """
    entero = 0
    correcto = False
    while not correcto:
        try:
            entero = int(input(mensaje))
            correcto = True
        except ValueError:
            print('[yellow]Introduce un entero.')
    return entero

def leer_nombre_archivo(mensaje, mensajeError):
    """
    Leer nombre de Archivo

    Función que recibe el nombre de un archivo, o bien la ruta donde
    se encuentra.
    Lanza excepción si no se encontró el archivo.

    @type  mensaje: string
    @param mensaje: Mensaje que se muestra al pedir el archivo.
    @type  mensajeError: string
    @param mensajeError: Mensaje que se muestra al no encontrar el archivo.
    @rtype:   string
    @return:  Cadena con el nombre del archivo.
    """
    nombre = input(mensaje)
    if not archivo_existe(nombre):
        raise FileNotFoundError(mensajeError)
    return nombre

def archivo_existe(arch):
    """
    Archivo existe

    Función que revisa si un archivo existe.

    @type  arch: string
    @param arch: Nombre del archivo a revisar.
    @rtype:   boolean
    @return:  Booleano, verdadero si existe el archivo.
    """
    if not os.path.isfile (arch):
        return False
    return True

def evaluaciones_toString(evaluaciones):
    """
    Evaluaciones a Cadena

    Función que convierte las evaluaciones en cadena

    @type  evaluaciones: list
    @param evaluaciones: Lista de tuplas con las evaluaciones (x, y).
    @rtype:   string
    @return:  Cadena que representa a las evaluaciones.
    """
    cadena = ""
    for (x,y) in evaluaciones:
        cadena += str(x) + ", " + str(y) + "\n"
    return cadena
