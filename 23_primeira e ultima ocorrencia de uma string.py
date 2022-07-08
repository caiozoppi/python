frase = str(input("Digite uma frase: ")).strip().upper()
print("A letra A aparece {} vezes na frase!".format(frase.count("A")))
print("A letra A apareceu primeiro na posição: {} da frase!".format(frase.find("A")+1))
print("A última vez que a letra ""A"" apareceu foi na posição {} da frase!".format(frase.rfind("A")+1))
