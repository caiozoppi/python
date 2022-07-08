'''
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hi = ((co ** 2) + (ca ** 2)) ** (1/2)
print("hipotenusa = {:.2f}".format(hi))
'''

'''
import math
co = float(input("cateto oposto: "))
ca = float(input("cateto adjacente: "))
hi = math.hypot(co, ca)
print("Cateto oposto é: {:.2f};\nCateto adjacente é: {:.2f};\nHipotenuza é : {:.2f}.".format(co, ca, hi))
'''

from math import hypot
co = float(input("Oposto: "))
ca = float(input("Adjacente: "))
print("A hypotenuza é : {:.2f}".format(hypot(ca, co)))




