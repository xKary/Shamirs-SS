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
from gmpy2 import mpz
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

#python no tiene consts :c
MOD_PRIME = mpz("208351617316091241234326746312124448251235562226470491514186331217050270460481")
rand_state = gmpy2.random_state() # puede ser mas limpio?

def cifrar(archivo, nombre_cifrado, shares_totales, shares_necesarios, password):
    """Función de acceso al módulo, dado un archivo lo cifra y produce los shares necesarios para abrirlo

    archivo: nombre del archivo
    nombre_cifrado: nombre del archivo de salida
    shares_totales: número de shares por producir
    shares_necesarios: número de shares necesarios para obtener la llave
    password: contraseña en texto plano

    regresa una lista de shares
    """
    # if shares_totales < shares_necesarios fail ?
    # El hash que usa mpz es una cadena hexadecimal y el que usa cifrar requiere bytes, por lo que hay que convertirlos
    password_hash = hash(password)
    cifrar_archivo(archivo, nombre_cifrado, bytes.hex(password_hash))
    coeficientes = [mpz(password_hash, base=16)] + genera_aleatorios(shares_necesarios -1)
    shares = []
    for x in genera_aleatorios(shares_totales):
        y = evalua_polinomio(x, coeficientes)
        shares.append((x,y))
    return string_shares(shares)

def hash_p(password):
    """Hashea de una cadena, la regresa como una cadena hexadecimal"""
    h = SHA256.new()
    h.update(password.encode("utf-8"))# update recibe bytes
    return h.hexdigest()

def cifra_archivo(nombre_archivo, nombre_cifrado, llave):
    """Cifra y escribe archivo"""
    pass

def genera_aleatorios(cantidad):
    """Genera una lista de de longitud _cantidad_ de números aleatorios mpz"""
    numeros_aleatorios = []
    for i in cantidad:
        numeros_aleatorios.append(gmpy2.mpz_random(rand_state, MOD_PRIME))
    return numeros_aleatorios

def evalua_polinomio(x, coeficientes):
    """Evalua el polinomio definido por _coeficientes_ en _x_ usando el método de Horner."""
    resultado = 0
    x_ajustado = f_mod(x, MOD_PRIME)
    for i in reversed(range(0, coeficientes)): # range es inclusivo en el primer argumento, exclusivo en el segundo
        multiplicacion = f_mod(resultado * x_ajustado, MOD_PRIME)
        resultado = f_mod(multiplicacion + coeficientes[i], MOD_PRIME)
    return resultado
    #Horner's method:
    #        result <- 0
    #        foreach i in {n-1..0}
    #            result <- (result * x) + coefficients[i]
    #        return result

def (x, y):
    """Construye una cadena que representa un Share del punto (_x_,_y_)"""
    pass
