m1 = float(input("Medida 1: "))
m2 = float(input("Medida 2: "))
m3 = float(input("Medida 3: "))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m2 + m1:
    if m1 == m2 and m2 == m3 and m1 == m3:
        print("""
        As medidas podem formar um triângulo Equilátero""")

    elif m1 == m2 == m3:
        print("""
        As medidas pordem formar um triângulo Isóceles""")

    elif m1 != m2 and m1 != m3 and m2 != m3:
        print("""
        As medidas porm formar um tirângulo Escaleno""")
else:
    print("As medidas informadas não podem formar um triângulo!")