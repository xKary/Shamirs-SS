from getpass import getpass

def menuCifrar():
    archivo = input ('Archivo a cifrar: \t')
    if not archivoExiste(archivo, 'No se encontró el archivo a cifrar'):
        return
    archivoCifrado = input ('Archivo de evaluaciones: \t')
    evaluaciones = leerNatural ('Número de evaluaciones requeridas')
    necesarios = leerNatural ('Número de puntos necesarios')
    contrasenia = getpass("Contraseña: ")

    cifrar (archivo, archivoCifrado, evaluaciones, necesarios, contrasenia)

def menuDescifrar():
    archivoCifrado = input ('Archivo a descifrar: \t')
    if not archivoExiste(archivoCifrado, "No se encontró el archivo a descifrar"):
        return

    archivoEvaluaciones = input ('Archivo con evaluaciones: \t')
    if not archivoExiste(archivoEvaluaciones, "No se econtró el archivo con las evaluaciones"):
        return

    descifrar (archivoCifrado, archivoEvaluaciones)

def leerNatural(mensaje):
    natural = 0
    correcto = false
    while not correcto:
        try:
            natural = int(input(mensaje))
            correcto = true
        except ValueError:
            print ('Introduce un natural')
    return natural

def archivoExiste(arch, mensajeError):
    if not os.path.isfile (arch):
        print (mensajeError)
        return false
    return true

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
        menuCifrar()
    elif opcion == 'D':
        print ('vamos a descifrar')
        menuDescifrar()
    elif opcion == 'S':
        salir = True
    else:
        print ('Introduce una opción válida')

print ('Hasta luego.')
