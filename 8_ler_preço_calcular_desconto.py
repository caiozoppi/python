#inserir dados:
preço = float(input("Qual valor do produto? "))
#Calcular desconto de 5%
desc = preço - (preço * 0.05)
#Mostrando na tela:
print("O preço atual é de {:.2f} reais mas eu faço 5% de desconto para você! \nEntão o preço vai ficar: {:.2f} reais!".format(preço, desc))


