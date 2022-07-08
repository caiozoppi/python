from datetime import date

nasc = int(input("Ano nascimento: "))
idade = date.today().year - nasc
if idade <= 9:
    print("""
    {} anos é MIRIM!""".format(idade))

elif idade > 9 and idade <= 14:
    print("""
    {} anos é INFANTIL!""".format(idade))

elif idade > 14 and idade <= 19:
    print("""
    {} anos é JÚNIOR!""".format(idade))

elif idade > 19 and idade <=25:
    print("""
    {} anos é SÊNIOR!""".format(idade))

else:
    print("""
    {} anos é MASTER!""".format(idade))