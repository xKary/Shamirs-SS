'''
Módulo que se encarga de la interacción con el usuario.
'''
import funciones_main
from rich import print
from rich.style import Style
from rich.console import Console

console = Console()
salir = False
opcion = ''

advertencia = Style(color = 'red', bold = True)
style = 'bold white'

console.print('Bienvenido', style = style, justify = 'center')
console.print('\nMenú\n', style = style, justify = 'center')

while not salir:
    console.print('[red]C[/] Cifrar  [blue]D[/] Descifrar  [green]S[/] Salir\n', style = style, justify = 'center')
    print('[bold white]Elige una opcion: \t', end = '')

    opcion = input().upper()

    if opcion == 'C':
        try:
            funciones_main.menu_cifrar()
        except FileNotFoundError:
            console.print('\nNo se encontró el archivo a cifrar.\n', style = advertencia, justify = 'center')
    elif opcion == 'D':
        try:
            funciones_main.menu_descifrar()
        except FileNotFoundError:
            console.print('\nNo se pudieron encontrar los archivos.\n', style = advertencia, justify = 'center')
    elif opcion == 'S':
        salir = True
    else:
        console.print('\nIntroduce una opción válida.\n', style = 'magenta3', justify = 'center')

console.print('¡Hasta luego!\n', style = style, justify = 'center')
