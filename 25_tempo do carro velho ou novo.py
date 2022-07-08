"""tempo = int(input("Qual ano do seu carro? "))
if tempo >= 3:
    print("Seu carro é velho!")
else:
    print("Seu carro é NOVO")
print("___FIM___")"""
# Variáveis:
tempo_velho = int(input("Quantos anos é considerado um carro velho? "))
tempo_carro = int(input("Quantos anos te o seu carro? "))

#Condições:
if tempo_carro < tempo_velho:
    print("Seu carro é >>> NOVO <<<")
else:
    print("Seu carro é >>> VELHO <<< ")
print("-" * 20)
print("FIM")
print("-" * 20)


