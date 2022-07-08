from datetime import date

ano_nascimento = int(input("Em que ano nasceu: "))
hoje = date.today().year
if hoje - ano_nascimento < 18:
    print("""
    Você tem {} ano(s)!
    Seu alistamento será no ano de {}!
    Ainda faltam {} ano(s) para se alistar!""".format(hoje - ano_nascimento, (18 - (hoje - ano_nascimento)) + hoje, 18 - (hoje - ano_nascimento)))


elif hoje - ano_nascimento > 18:
    print("""
    Você tem {} ano(s)!
    Você deveria ter feito o alistamento em {}"
    Já se passaram {} ano(s) para você se alistar""".format(hoje - ano_nascimento, ano_nascimento + 18, (hoje - ano_nascimento) - 18))

elif hoje - ano_nascimento == 18:
    print("""
    Você tem {} anos!
    Você precisa se alistar \033[7;40mIMEDIATAMENTE\033[m!""".format(hoje - ano_nascimento))