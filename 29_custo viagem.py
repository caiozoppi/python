"""""    # Colher dados
km_tot = float(input("KM total da sua viagem: "))
km_p = float(input("KM para entrar na promoção: "))
v_km = float(input("Valor/km SEM promoção: "))
v_km_p = float(input("Valor/km COM promoção: "))
    # Calcular com condições
if km_tot <= km_p:
    print("O valor ESTÁ FORA DA PROMOÇÃO e será pago o total de R$ {:.2f}!".format((km_tot * v_km)))
else:
    print("O valor ESTÁ DENTRO DA PROMOÇÃO e ser pago o total de R$ {:.2f}!".format(km_tot * v_km_p))"""

viagem_tot = int(input("Viagem total: "))
km_para_promocao = float(input("KM para promoção: "))
v_promocao = float(input("Valor por km rodado na promoção: "))
v_sem_promocao = float(input("Valor normal: "))
preço = viagem_tot * v_sem_promocao if viagem_tot <= km_para_promocao else viagem_tot * v_promocao
print("Valor é R$ {}".format(preço))
