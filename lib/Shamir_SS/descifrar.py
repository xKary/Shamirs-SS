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
            numerador *= gmpy2.f_mod((-1) * valores_x[j],PRIMO)
            denominador *= gmpy2.f_mod(valores_x[i] - valores_x[j],PRIMO)

    deno_mod = gmpy2.invert(denominador,PRIMO)

    return int(gmpy2.f_mod((numerador * deno_mod),PRIMO))

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

def descrifrar_archivo(valores_x,valores_y,arch_cifrado):
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
    llave = interpolacion_Lagrange(valores_x,valores_y)
    print(llave)
    llave_b = llave.to_bytes(32, "big")
    vector_inicial = arch_cifrado[:AES.block_size]
    cipher = AES.new(llave_b, AES.MODE_CBC,vector_inicial)
    return cipher.decrypt(arch_cifrado[AES.block_size:])

def descifrar(archivo_cifrado, archivo_evaluaciones):
    archivo = open(archivo_cifrado, "r")
    contenido_cifrado = archivo.read()
    archivo.close()

    x = []
    y = []

    evaluaciones = open(archivo_evaluaciones, "r")
    while(True):
        punto = evaluaciones.readline()
        p = punto.split(", ")
        x.append(p[1])
        y.append(p[2])
        if not linea:
            break
    evaluaciones.close()

    if(len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        raise NameError('El archivo de evaluaciones está incompleto.')

    contenido_descifrado = descrifrar_archivo(x,y,contenido)
