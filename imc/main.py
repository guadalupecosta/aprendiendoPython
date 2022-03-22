# Calculadora de IMC
# IMC = peso / (altura * altura)
# < 19: delgado
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad

def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirElIMC():
    peso = float(input("Ingrese su peso en kilogramos"))
    alturaEnCM = float(input("Ingrese su altura en centímetros"))
    alturaEnMetros = alturaEnCM / 100
    imc = calcularIMC(peso, alturaEnMetros)

    print("Su IMC es de " + str(imc))

    if imc < 20:
        print("Delgado")
    if imc >= 20 and imc < 26:
        print("Peso normal")
    if imc >= 26 and imc < 30:
        print("Sobrepeso")
    if imc >= 30:
        print("Obesidad")

print("Ingrese los datos de la primer persona")
pedirElIMC()
print("Ingrese los datos de la segunda persona")
pedirElIMC()
print("Ingrese los datos de la tercer persona")
pedirElIMC()

