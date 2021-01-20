import cifrar
import descifrar

shares = cifrar.cifra("secret", "secret.aes", 2, 1, "pasvurd")

valores_x, valores_y = zip(*shares)
f = open("secret.aes", "rb")
data = bytes(f.read())
f.close()

#brittle as fuck
res = descifrar.descrifrar_archivo(valores_x, valores_y, data)
print(res)
print(res.decode("utf-8"))
