sal = float(input("Qual seu salário?: "))
sal_alto = float(input("Qual salário benchmarck?: "))
r_sal_normal = float(input("Qual % reajuste para salários NORMAIS?: "))
r_sal_alto = float(input("Qual % reajuste para salários acima do BENCHMARK?: "))
if sal > sal_alto:
    print("SALÁRIO ALTO! O salário era {} e agora é {}!".format(sal, (sal + (sal * r_sal_alto)*0.01)))
else:
    print("SALÁRIO BAIXO! O salário era {} e agora é {}!".format(sal, (sal + (sal * r_sal_normal)*0.01)))

