    #Importando bibliotecas:
import random
import math
from time import sleep
    # EScolher número aleatório entre 0 e 5:
escolhido = random.randint(0, 5)
    #Interagindo e colhendo dados:
print("-=-" * 30)
print("VAMOS VER SE VOCÊ ADIVINHA QUAL NÚMERO O COMPUTADOR VAI ESCOLHER DE 0 A 5!!!")
print("-=-" * 30)
n = float(input("\nDigite um número inteiro de 0 a 5: "))
n_int = math.trunc(n)
if n_int <= 5:
    print("Vamos ver se você acertou...")
    sleep(1)
    print(f"Você escolheu: {n_int}")
    print(f"Eu escolhi: {escolhido}")
    if escolhido == n:
        print("Parabéns")
        print("-=FIM=-")
    else:
        print("Não foi dessa vez! Tente novamente")
        print("-=FIM=-")
else:
    print("Apenas até 5")
    print("-=FIM=-")
