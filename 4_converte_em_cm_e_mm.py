medida = float(input("Qual medida deseja converter para centímetros e milímetros?\n (digite em metros): "))
c_cm = medida * 100
c_mm = medida * 1000
print(" A medida é: {:.2f} metro(s)! \n convertido em cm fica: {:.2f} centímetros! \n convertido em mm fica: {:.2f} milímetros!".format(medida, c_cm, c_mm))
