"""Objetivo:
   1- Mostrar o nome completo em maiúsculo e minúsculo;
   2- Quantas letras ao todo; 
   3- Quantas letras sem considerar os "espaços";
   4- Quantas letras tem o primeiro nome;"""
"""Inserindo dados:"""
nome = str(input("Qual seu nome? ")).strip()
separa = nome.split()
"""Maiúsculo:"""
print("Seu nome em maiúsculo é: {}".format(nome.upper()))
"""Minúsculo"""
print("Seu nome em minúsculo é: {}".format(nome.lower()))
"""Quantas letras sem considerar "os espaços" """
print("Seu nome possui {} letras ao todo!".format(len(nome) - nome.count(" ")))
"""Quantas letras tem no seu primeiro nome"""
print("O seu primeiro nome possui {} letras!".format(len(separa[1])))




