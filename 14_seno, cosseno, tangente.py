import math
angulo = float(input("Ângulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("Angulo é {:.2f},\nSeu cosseno é {:.2f}, \nSua tangente é: {:.2f}, \nSeu seno é : {:.2f}".format(angulo, cos, tan, sen))
