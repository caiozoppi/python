import random
from time import sleep

lista = ["papel", "pedra", "tesoura"]
pc = random.choice(lista).lower()
print("pc escolheu {}".format(pc))
print("""
Qual opção:
 [PAPEL]
 [PEDRA]
[TESOURA]""")
opcao = str(input("Qual sua opção: ")).strip().lower()
print("Você escolheu {}".format(opcao))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")

if opcao == "papel":
    if pc == "papel":
        print("""
        Você: {}
        PC: {}
        EMPATE""".format(opcao, pc))
    elif pc == "pedra":
        print("""
        Você: {}
        PC: {}
        GANHOU""".format(opcao, pc))
    elif pc == "tesoura":
        print("""
        Você: {}
        PC: {}
        PERDEU""".format(opcao, pc))

elif opcao == "pedra":
    if pc == "pedra":
        print("""
        Você: {}
        PC: {}
        EMPATE""".format(opcao, pc))
    elif pc == "papel":
        print("""
        Você: {}
        PC: {}
        PERDEU""".format(opcao, pc))
    elif pc == "tesoura":
        print("""
        Você: {}
        PC: {}
        GANHOU""".format(opcao, pc))

elif opcao == "tesoura":
    if pc == "tesoura":
        print("""
        Você: {}
        PC: {}
        EMPATE""".format(opcao, pc))
    elif pc == "papel":
        print("""
        Você: {}
        PC: {}
        GANHOU""".format(opcao, pc))
    elif pc == "pedra":
        print("""
        Você: {}
        PC: {}
        PERDEU""".format(opcao, pc))

