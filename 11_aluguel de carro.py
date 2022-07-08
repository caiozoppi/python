#inserindo dados:
km = float(input("km rodado: "))
d = int(input("Dias: "))
#calculando:
v_d = 60
v_km = 0.15
v_p = ((v_d * d) + (km * v_km))
print("o valor a pagar é: R$ {:.2f}".format(v_p))
