m1 = float(input("Medida 1: "))
m2 = float(input("Medida 2: "))
m3 = float(input("Medida 3: "))
    #Dicionário:
cores = {"limpa" : "\033[m" ,
         "azul" : "\033[34m" ,
         "amarelo" : "\033[33m",
         "pretoebranco" : "\033[7;30"}

print("Calculando...")
if m1 > (m2 + m3) or m2 > (m1 + m3) or m3 > (m1 + m2):
    print("{}NÃO{} é possível construir um triângulo!".format(cores["amarelo"] , cores["limpa"]))
else:
    print("{}SIM{}, é possível construir um triângulo".format(cores["azul"] , cores["limpa"]))