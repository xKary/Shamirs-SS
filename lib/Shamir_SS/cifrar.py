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
    """Función de acceso al módulo, dado un archivo lo cifra y produce los shares necesarios para abrirlo

    archivo: nombre del archivo
    nombre_cifrado: nombre del archivo de salida
    shares_totales: número de shares por producir
    shares_necesarios: número de shares necesarios para obtener la llave
    password: contraseña en texto plano

    regresa una lista de shares
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
    """Hashea de una cadena, la regresa como una cadena hexadecimal"""
    h = SHA256.new()
    h.update(password.encode("utf-8"))# update recibe bytes
    return h.hexdigest()

def cifra_archivo(contenido, llave):
    """Cifra y escribe archivo"""
    # cifrarlo
    vector_inicial = Random.new().read(AES.block_size)
    cifrado = AES.new(llave, AES.MODE_CBC, vector_inicial)
    texto_cifrado = vector_inicial
    texto_cifrado += cifrado.encrypt(
            pad(contenido.encode("utf-8"), AES.block_size))

    return texto_cifrado

def genera_aleatorios(cantidad):
    """Genera una lista de de longitud _cantidad_ de números aleatorios mpz"""
    numeros_aleatorios = []
    for i in range(0,cantidad):
        aleatorio = rand.randint(0,PRIMO)
        numeros_aleatorios.append(aleatorio)
    return numeros_aleatorios

def evalua_polinomio(x, coeficientes):
    """Evalua el polinomio definido por _coeficientes_ en _x_ usando el método de Horner."""
    resultado = mpz(0)
    x_ajustado = gmpy2.f_mod(x, PRIMO)
    for i in reversed(range(0, len(coeficientes))): # range es inclusivo en el primer argumento, exclusivo en el segundo
        multiplicacion = gmpy2.f_mod(resultado * x_ajustado, PRIMO)
        resultado = gmpy2.f_mod(multiplicacion + coeficientes[i], PRIMO)
    return resultado
