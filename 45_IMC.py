peso = float(input("Peso em KG: "))
altura = float(input("Altura em M: "))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print("""
    Seu imc é {:.2f} e você está abaixo do peso ideal!""".format(imc))

elif imc <= 25:
    print("""
    Seu imc é {:.2f} e você está no seu peso ideal!""".format(imc))

elif imc <= 30:
    print("""
    Seu imc é {:.2f} e você está com sobrepeso!""".format(imc))

elif imc <=40:
    print("""
    Seu imc é {:.2f} e você está Obeso""".format(imc))

else:
    print("""
    Seu imc é {:.2f} e você está obeso mórbido!""".format(imc))
