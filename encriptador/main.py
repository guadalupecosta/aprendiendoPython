def encriptar(texto):
    print("El texto a encriptar es: " + texto)
    textoFinal = ""
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal

def desencriptar(texto):
    print("El texto a desencriptar es: " + texto)
    textoFinal = ""
    contador = 0
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se encriptó correctamente.")

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se desencriptó correctamente.")

respuestaEoD = input("Presione 'E' para encriptar o 'D' para desencriptar ")
rutaArchivo = input("Ingrese la ruta del archivo ")

if respuestaEoD == "E":
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)