print(ord("b"))
resultado=""
texto= input("ingrese su texto: ")
for caracter in texto:
    if caracter.isalpha() == True:
        valor_ascci = ord(caracter)
        if valor_ascci >97 and valor_ascci<=122:
            limite=ord("z")
        elif valor_ascci>=65 and valor_ascci<=91:
            limite=ord ("Z")
        valor_ascci+=3
        if valor_ascci >=limite:
            valor_ascci -=26
        valor_ascci = chr(valor_ascci)
    else:
        valor_ascci += caracter
    resultado += valor_ascci
print ("el texto cifrado es: ", resultado)




