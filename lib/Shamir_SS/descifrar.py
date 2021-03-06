"""
Módulo que se encarga de descrifrar el contenido del archivo indicado.
"""
import gmpy2
from gmpy2 import mpz
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from .constantes import PRIMO

def polinomio_base(i,valores_x):
    """
    Función qué calcula el polinomio de base Pi(x).

    @type  i: int
    @param i: Índice del valor x en qué calculamos la base.
    @type  valores_x: list
    @param valores_x: Valores x en los que el polinomio fue evaluado.
    @rtype:   int
    @return:  Resultado de la evaluación.
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
    Interpolación de Lagrange.

    Función qué calcula la interpolación de Lagrange evaluado en 0, a partir de t
    puntos del polinomio.

    @type  valores_x: list
    @param valores_x: Valores x en los que el polinomio fue evaluado.
    @type  valores_y: list
    @param valores_y: Resultado de la evaluación del polinomio en un punto x.
    @rtype:   int
    @return:  Evaluación del polinomio en 0.
    """
    p = 0;
    for i in range(0,len(valores_x)):
        pi = polinomio_base(i,valores_x)
        p += (gmpy2.f_mod((valores_y[i] * pi),PRIMO))

    return int(gmpy2.f_mod(p,PRIMO))


def descifra(contenido_cifrado, valores_x, valores_y):
    """
    Descrifrar archivo.

    Función qué descrifra el archivo que recibe como parámetro.

    @type contenido_cifrado: bytes
    @param contenido_cifrado: Contenido a descrifrar.
    @type  valores_x: list
    @param valores_x: Valores x en los que el polinomio fue evaluado.
    @type  valores_y: list
    @param valores_y: Resultado de la evaluación del polinomio en un punto x.
    @rtype:   bytes
    @return:  Archivo descifrado.
    """
    llave = interpolacion_Lagrange(valores_x,valores_y)
    llave_hex = hex(llave)[2:]
    if len(llave_hex) & 1 == 1:
        llave_hex = "0" + llave_hex
    llave_bytes = bytes.fromhex(llave_hex)
    iv = contenido_cifrado[:AES.block_size]
    cipher = AES.new(llave_bytes, AES.MODE_CBC,iv)

    resultado = cipher.decrypt(contenido_cifrado[AES.block_size:])
    return unpad(resultado, AES.block_size)
