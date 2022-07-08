from datetime import date

print("""Qual seu sexo?
      [M] - Masculino?
      [F] - Feminino?""")
sexo = str(input("Qual sua opção?: "))
if sexo == m:
    nasc = str(input("Nascimento: "))
    idade = date.today().year() - nasc
    if idade < 18:
        print("""
        Você tem {} ano(s)!
        Você vai se alistar em {} ano(s)!
        Seu alistamento será no ano de: {}!""".format(idade, 18 - idade , nasc + 18))
    elif idade > 18:
        print("""
        Você tem {} ano(s)!
        Você deveria ter se alistado no ano de: {}!
        Fazem {} ano(s) que você deveria ter se alistado!""".format(idade, nasc + 18, date.today().year() - (nasc + 18)))
    elif idade == 18:
        print("""
        Vá se alistar imediatamente!""")

elif sexo == f:
    print("""
    Você é mulher e não precisa prestar o EXÉRCITO! DISPENSADA!""")

