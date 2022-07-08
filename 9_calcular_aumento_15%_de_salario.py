#inserir dados:
salario = float(input("Qual seu salário? R$ "))
aumento_sal = float(input("Qual % de aumento deseja? "))
#calcular
aumento = salario + (salario * (aumento_sal / 100))
#Mostrar na tela:
print("Seu salário atual é de R$ {:.2f} reais/ mês e com novo aumento de {:.2f}% ele vai para R$ {:.2f}".format(salario, aumento_sal, aumento))

