from Crypto.Cipher import AES
import gmpy2
from gmpy2 import mpz
"""
Descifrar
-----------------------------------
Módulo que se encarga de descrifrar
"""
primo = 7

def polinomioBase(i,valores_x):
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
            numerador *= gmpy2.f_mod((-1) * valores_x[j],primo)
            denominador *= gmpy2.f_mod(valores_x[i] - valores_x[j],primo)

    denoMod = gmpy2.invert(denominador,primo)

    return int(gmpy2.f_mod((numerador * denoMod),primo))

def interpolacionL(valores_x,valores_y):
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
        pi = polinomioBase(i,valores_x)
        p += (gmpy2.f_mod((valores_y[i] * pi),primo))

    return int(gmpy2.f_mod(p,primo))

def descrifrarArch(valores_x,valores_y,archCifrado):
    """
    Descrifrar archivo

    Función qué descrifra el archivo que recibe como parámetro

    Parameters
    ----------
    valores_x: list
        Valores x en los que el polinomio fue evaluado
    valores_y: list
        Resultado de la evaluación del polinomio en x
    archCifrado: arch
        Archivo que se descifrará

    Returns
    -------
    arch
        Archivo descifrado
    """
    llave = interpolacionL(valores_x,valores_y)
    #Convertir a bits
    #llave = llave.to_bytes(llave,'big')
    archDes = AES.new(llave, AES.MODE_CBC,'This is an IV456')
    return archDes.decrypt(archCifrado)
