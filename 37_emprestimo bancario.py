from time import sleep
    # Inserindo dados:
v_imovel = float(input("Qual valor do imóvel que deseja comprar?: "))
prazo = int(input("Em quantos ANOS você quer pagar?: "))
v_renda = (float(input("Qual valor da sua renda atual?: ")))
capacidade = (v_renda * 0.3)
parcela = (v_imovel / (prazo * 12))
    #Calculando:
print("Calculando...")
sleep(1)
print("O valor do imóvel é: R$ {}!".format(v_imovel))
print("A parcela para esse valor de imóvel é R$ {}: !".format(parcela))
print("Sua renda é R$ {}: !".format(v_renda))
print("Sua capacidade de pagamento é R$ {}: !".format(capacidade))
if parcela > capacidade:
    print("\033[7;31mVocê não pode comprar!\033[m")
else:
    print("\033[7;40mPARABÉNS!!!\033[m")
