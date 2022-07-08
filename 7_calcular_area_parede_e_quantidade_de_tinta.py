#inserir dados
a = float(input("Qual a altura da sua parede? "))
l = float(input("Qual a largura da sua parede? "))
#calcular
calc_area = a * l
calc_tint = (calc_area * 1)/2
#mostrando resultado na tela
print("Sua área é de: {:.2f} m² e você vai precisar de {:.2f} litros de tinta para poder pintá-la!".format( calc_area, calc_tint))

