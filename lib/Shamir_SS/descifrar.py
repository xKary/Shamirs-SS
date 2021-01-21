import gmpy2
from gmpy2 import mpz
from Crypto.Cipher import AES
from .constantes import PRIMO
"""
Descifrar
-----------------------------------
Módulo que se encarga de descrifrar
"""

def polinomio_base(i,valores_x):
    """
    Polinomio de base Pi(x)

    Función qué calcula el polinomio de base Pi(x)

    Parameters
    ----------
    i: int
        índice del valor x en qué calculamos la base
    valores_x: list
        Valores x en los que el polinomio fue evaluado

    Returns
    -------
    int
        Resultado
    """
    numerador = 1
    denominador = 1
    for j in range(0,len(valores_x)):
        if j != i:
            numerador *= gmpy2.f_mod(-1 * mpz(valores_x[j]),PRIMO)
            denominador *= gmpy2.f_mod(mpz(valores_x[i] - valores_x[j]),PRIMO)

    deno_mod = gmpy2.invert(denominador,PRIMO)

    return int(gmpy2.f_mod(mpz(numerador * deno_mod),PRIMO))

def interpolacion_Lagrange(valores_x,valores_y):
    """
    Interpolación de Lagrange

    Función qué calcula la interpolación de Lagrange evaluado en 0

    Parameters
    ----------
    valores_x: list
        Valores x en los que el polinomio fue evaluado
    valores_y: list
        Resultado de la evaluación del polinomio en x

    Returns
    -------
    int
        Evaluación del polinomio en 0
    """
    p = 0;
    for i in range(0,len(valores_x)):
        pi = polinomio_base(i,valores_x)
        p += (gmpy2.f_mod((valores_y[i] * pi),PRIMO))

    return int(gmpy2.f_mod(p,PRIMO))


def descifra(contenido_cifrado, valores_x, valores_y):
    """
    Descrifrar archivo

    Función qué descrifra el archivo que recibe como parámetro

    Parameters
    ----------
    contenido_cifrado: arch
        Archivo que se descifrará
    valores_x: list
        Valores x en los que el polinomio fue evaluado
    valores_y: list
        Resultado de la evaluación del polinomio en x

    Returns
    -------
    arch
        Archivo descifrado
    """
    llave = interpolacion_Lagrange(valores_x,valores_y)
    llave_hex = hex(llave)[2:]
    if len(llave_hex) & 1 == 1:
        llave_hex = "0" + llave_hex
    llave_bytes = bytes.fromhex(llave_hex)
    iv = contenido_cifrado[:AES.block_size]
    cipher = AES.new(llave_bytes, AES.MODE_CBC,iv)

    return cipher.decrypt(contenido_cifrado[AES.block_size:])
