n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
if n1 > n2:
    print("[{}] o PRIMEIRO número é maior!".format(n1))
    print("[{}] o SEGUNDO número é menor!".format(n2))

elif n1 < n2:
    print("[{}] o SEGUNDO número é maior!".format(n2))
    print("[{}] o PRIMEIRO número é maior!".format(n1))

elif n1 == n2:
    print("[{}] e [{}] são de mesmo valor!".format(n1, n2))

else:
    print("Inválido!")