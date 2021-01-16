from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def polinomioBase(i,valores_x):
    pi = 1;
    for j in range(0,len(valores_x)):
        if j != i:
            pi *= (((-1) * valores_x[j]) / (valores_x[i] - valores_x[j]))
    return pi

def interpolacionL(valores_x,valores_y):
    p = 0;
    for i in range(0,len(valores_x)):
        pi = polinomioBase(i,valores_x)
        p += valores_y[i] * pi
    return p

def descrifrar(valores_x,valores_y,archCifrado):
    llave = interpolacionL(valores_x,valores_y)
    archDes = AES.new(llave, AES.MODE_CBC,'This is an IV456')
    return archDes.decrypt(archCifrado)
