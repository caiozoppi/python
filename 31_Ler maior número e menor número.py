n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("\nDigite o segundo número: "))
n3 = float(input("\nDigite o terceiro número: "))
lista = [n1, n2, n3]

print(lista)
print("O maior número é {:.2f}!".format(max(lista)))
print("O menor número é {:.2f}!".format(min(lista)))