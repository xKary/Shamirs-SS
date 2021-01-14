
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
        print ('vamos a cifrar')
    elif opcion == 'D':
        print ('vamos a descifrar')
    elif opcion == 'S':
        salir = True
    else:
        print ('Introduce una opción válida')

print ('Hasta luego.')
