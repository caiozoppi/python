from datetime import date
ano = int(input("Informe o ano que deseja analisar e digite 0 se quiser analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto!".format(ano))
else:
    print("O ano {} ""NÃO É"" bissexto!".format(ano))