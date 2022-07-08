from time import sleep
    # Iserindo dados:
nome = str(input("Nome: ")).strip().upper()
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
media = (nota_1 + nota_2) / 2
print("Calculando sua média...")
sleep(1)

    # Calculando com condições:
if media < 5:
    print("""{}:
    Sua nota 1 foi {}!
    Sua nota 2 foi {}!
    Sua média foi {:.2f}!
    De acordo com as regras da escola você foi \033[7;41mREPROVADO.\033[m""".format(nome, nota_1, nota_2, media))

elif media >= 5 and media <= 6.9:
    print("""{}:
    Sua nota 1 foi{}!
    Sua nota 2 foi{}!
    Sua média foi {:.2f}!
    De acordo com as regras da escola você está de \033[7;40mRECUPERAÇÃO.\033[m""".format(nome, nota_1, nota_2, media))

elif media >= 7.0:
    print("""{}:
    Sua nota 1 foi {}!
    Sua nota 2 foi {}!
    Sua média foi {}!
    De acordo com as regras da escola você foi \033[7;42mAPROVADO!\033[m PARABÉNS""".format(nome, nota_1, nota_2, media))

