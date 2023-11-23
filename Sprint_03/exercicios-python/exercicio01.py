# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. 
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
import datetime

nome = input("Digite seu nome: ")
idade_atual = int(input("Digite sua idade atual: "))

ano_atual = datetime.datetime.now().year
ano_completa_100 = ano_atual + (100 - idade_atual)

print(ano_completa_100)