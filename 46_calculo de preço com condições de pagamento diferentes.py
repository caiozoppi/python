preco = float(input("Valor atual: "))
print("""
Qual forma de pagamento:
[1] à vista, dinheiro ou cheque = 10% de desconto!
[2] à vista no cartão = 5% de desconto!
[3] 2x no cartão = preço normal!
[4] 3x ou mais no cartão = acréscimo de 20% de juros!""")
opcao = int(input("Qual a sua opção?: "))

if opcao == 1:
    print("""
    [1] 10% de desconto!
    O valor será de R$ {:.2f}!""".format(preco - (preco * 0.1)))

elif opcao == 2:
    print("""
    [2] 5% de desconto!
    O valor será de R$ {:.2f}!""".format(preco - (preco * 0.05)))

elif opcao == 3:
    print("""
    [3] Preço normal!
    O valor será de R$ {:.2f}!""".format(preco))

elif opcao == 4:
    print("""
    [4] Acréscimo de 20% de juros!
    O valor será de R$ {:.2f}""".format(preco + (preco * 0.2)))