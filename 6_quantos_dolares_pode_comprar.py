#inserindo dados
d = float(input("Quanto dinheiro você tem na sua carteira? \n > Digite o valor: R$ "))
cot_dol = float(input("Qual cotação do dolar hoje? (em caso de número quebrado coloque ponto ao invés de vírgular: ex: 5.66)! \n > Digite o valor: $ "))
#convertendo
conv_dol = d / cot_dol
#mostrando na tela
print("Você possui R$ {:.2f} na sua carteira! \nde acordo com a cotação de hoje (que você informou = $ {:.2f}!) você pode comprar: $ {:.2f}.".format(d, cot_dol, conv_dol))

