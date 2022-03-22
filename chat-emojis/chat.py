seguirChateando = True
while seguirChateando:
    texto = input(">")
    if texto == "salir":
        seguirChateando = False
    texto = texto.replace(":)", "🙂")
    texto = texto.replace(":D", "😀")
    texto = texto.replace(":P", "😛")
    texto = texto.replace(">:(", "😠")
    texto = texto.replace(":(", "🙁")
    texto = texto.replace(":'(", "😭")
    texto = texto.replace(":|", "😐")
    texto = texto.replace(":O", "😮")

    print(texto)
