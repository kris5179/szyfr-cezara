testowy_tekst = "AbCdefYZZ1234##$"

print("a = " + str(ord("a")))
print("A = " + str(ord("A")))
print("z = " + str(ord("z")))
print("Z = " + str(ord("Z")))

def encode(tekst):
    lista = list(tekst)
    for i in range(len(lista)):
        znak = ord(lista[i])
        znak = znak + 1

        if znak == 90:
            znak = 65
        lista[i] = chr(znak)
    return ''.join(lista)

print("test")
print(testowy_tekst)
print(encode(testowy_tekst))