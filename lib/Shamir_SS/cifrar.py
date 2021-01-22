#Cifrar
#Se encarga de procesar contraseña, crear shares (y por consecuencia polinomio) y cifrar el archivo de entrada

# recibe contraseña en texto plano y archivo a cifrar
# se hashea contraseña con sha-256
# Se generan t-1 números aleatorios (coeficientes del polinomio)
# se construye un polinomio con el hash de la contraseña como el valor constante
# evalua el polinomio en n puntos aleatorios
# se regresan los n puntos como los shares

"""
Contiene la lógica para cifrar archivo y crear Shares necesarias para descifrarlo
"""

import gmpy2
import os
from gmpy2 import mpz
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import Crypto.Random as Random
import Crypto.Random.random as rand
from Crypto.Util.Padding import pad
from .constantes import PRIMO

def cifra(contenido, shares_totales, shares_necesarios, llave):
    """
    Función de acceso al módulo, cifra datos y produce los shares necesarios para abrirlo

    @type contenido: bytes
    @param contenido: bytes leidos de un archivo (que serán cifrados)
    @type shares_totales: int
    @param shares_totales: cantidad de shares que serán producidos (llaves que juntas pueden descifrar  al contenido)
    @type shares_necesarios: int
    @param shares_necesarios: cantidad mínima de shares necesarias para descifrar el contenido
    @type llave: string
    @param llave: llave con la que se cifrará el contenido
    @rtype: (bytes, list)
    @return: regresa una pareja ordenada con la primera entrada los bytes cifrados con llave hasheada, la segunda la lista de shares
    """
    # El hash que usa mpz es una cadena hexadecimal y el que usa cifrar requiere bytes, por lo que hay que convertirlos
    llave = hash_llave(llave)
    contenido_cifrado = cifra_archivo(contenido, bytes.fromhex(llave))
    coeficientes = [mpz(llave, base=16)] + genera_aleatorios(shares_necesarios -1)
    shares = []
    for x in genera_aleatorios(shares_totales):
        y = evalua_polinomio(x, coeficientes)
        shares.append((x,y))
    return (contenido_cifrado, shares)

def hash_llave(password):
    """
    Obtiene el hash de una cadena.

    @type: password: string
    @param: password: cadena a hashear
    @rtype: string
    @return: cadena del hash de password en hexadecimal
    """
    h = SHA256.new()
    h.update(password.encode("utf-8"))# update recibe bytes
    return h.hexdigest()

def cifra_archivo(contenido, llave):
    """
    Cifra contenido con llave, usando AES

    @type contenido: bytes
    @param contenido: bytes a cifrar.
    @type llave: bytes
    @param llave: 256 bits con los que se cifrará el contenido (en este caso producidos por sha256).
    @rtype bytes
    @return contenido cifrado
    """
    # cifrarlo
    vector_inicial = Random.new().read(AES.block_size)
    cifrado = AES.new(llave, AES.MODE_CBC, vector_inicial)
    texto_cifrado = vector_inicial
    texto_cifrado += cifrado.encrypt(
            pad(contenido, AES.block_size))
    return texto_cifrado

def genera_aleatorios(cantidad):
    """
    Genera aleatorios.

    Genera una lista de números aleatorios entre 0 y la constante PRIMO.

    @type cantidad: int
    @param cantidad: cantidad de números aleatorios a generar i.e. la longitud de la lista
    @rtype: list
    @return: lista de números aleatorios
    """
    numeros_aleatorios = []
    for i in range(0,cantidad):
        aleatorio = rand.randint(0,PRIMO)
        numeros_aleatorios.append(aleatorio)
    return numeros_aleatorios

def evalua_polinomio(x, coeficientes):
    """
    Evalua un polinomio en x

    @type x: int
    @param x: valor sobre el que se evalua el polinomio.
    @type coeficientes: list
    @param coeficientes: lista de coeficientes del polinomio en orden ascendiente ejemplo [4,1,2] -> 4+x+2x^2
    @rtype int
    @return regresa la evaluación del polinomio (todas estas operaciones son sobre el campo Z_PRIMO)
    """
    resultado = mpz(0)
    x_ajustado = gmpy2.f_mod(x, PRIMO)
    for i in reversed(range(0, len(coeficientes))): # range es inclusivo en el primer argumento, exclusivo en el segundo
        multiplicacion = gmpy2.f_mod(resultado * x_ajustado, PRIMO)
        resultado = gmpy2.f_mod(multiplicacion + coeficientes[i], PRIMO)
    return resultado
