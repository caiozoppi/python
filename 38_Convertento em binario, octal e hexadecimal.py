"""numero = int(input("Digite um número inteiro: "))
print("Escolha como quer converter: ")
print("1 - Binário!\n2 - octal!\n3 - hexadecimal!")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("o número {} convertido para binário é {}".format(numero, bin(numero)))
elif opcao == 2:
    print(oct(numero))
elif opcao == 3:
    print(hex(numero))
else:
    print("Opção inválida! Re-inicie o programa")"""

from time import sleep

num = int(input("Número: "))
print("""Escolha uma opção:
[1] Binário
[2] Octal
[3] Hexadecimal""")
opcao = int(input("Sua opção: "))
print("Calculando...")
sleep(2)
if opcao == 1:
    print("[1]...o número {} convertido para binário é \033[7;40m{}\033[m!".format(num, bin(num)))

elif opcao == 2:
    print("[2]...o número {} convertido em OCTAL é \033[7;40m{}\033[m!".format(num, oct(num)))

elif opcao == 3:
    print("[3]...o número {} convertido em HEXADECIMAL é \033[7;40m{}\033[m!".format(num, hex(num)))

else:
    print("Inválido")