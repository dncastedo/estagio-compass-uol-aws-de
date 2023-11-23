# Utilizando high order functions, implemente o corpo da função conta_vogais. 
# O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
# É obrigatório aplicar as seguintes funções:  len, filter, lambda
# Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

def conta_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_encontradas = list(filter(lambda x: x in vogais, string.lower()))
    return len(vogais_encontradas)

print(conta_vogais("Hello, World!")) 
print(conta_vogais("Eu me chamo Diane do Nascimento Castedo")) 