    # Inserindo dados:
print("-=" * 20)
v_limite = float(input("Qual é a velocidade LIMITE? "))
v_atual = float(input("Qual a sua velocidade? "))
v_multa = float(input("Valor de multa por KM acima da velocidade limite? "))
print("-=" * 20)

    # Calculando:
print("Sua velocidade é {:.2f}!".format(v_atual))
print("O limite dessa rodovia é {:.2f}!".format(v_limite))
if v_atual <= v_limite:
    print("Ótimo, continue assim")
else:
    print("-=" * 20)
    print("EPA! Temos uma conta para acertar")
    print("Diriga-se para a prisão!")
    multa = float((v_atual - v_limite) * v_multa)
    print("Sua multa é de R$ {:.2f}!".format(multa))

