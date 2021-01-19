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

def cifrar(archivo,  archivo_cifrado, evaluaciones, shares_necesarios, password):
    """Función de acceso al modulo, recibe información necesaria para cifrar archivo y regresa Shares."""
    pass

def hash(password):
    """Hashea de una cadena."""
    pass

def cifra_archivo(nombre_archivo):
    """Cifra y escribe archivo"""
    pass

def genera_aleatorios(cantidad):
    """Genera una lista de de longitud _cantidad_ de números aleatorios"""
    pass

def evalua_polinomio(x, coeficientes):
    """Evalua el polinomio definido por _coeficientes_ en _x_ usando el método de Horner."""
    #Horner's method:
    #        result <- 0
    #        foreach i in {n-1..0}
    #            result <- (result * x) + coefficients[i]
    #        return result
    pass

def construye_share(x, y):
    """Construye una cadena que representa un Share del punto (_x_,_y_)"""
    pass
