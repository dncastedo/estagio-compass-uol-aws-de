
# Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.

import csv

def ator_com_mais_filmes(arquivo_csv, arquivo_saida):
    maior_numero_filmes = 0
    ator_mais_filmes = None

    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        arquivo_lido = csv.DictReader(arquivo)
        for linha in arquivo_lido:
            ator = linha['Actor']
            numero_filmes = int(linha['Number of Movies'])

            if numero_filmes > maior_numero_filmes:
                maior_numero_filmes = numero_filmes
                ator_mais_filmes = ator

    if ator_mais_filmes:
        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_texto:
            print('Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.\n', file=arquivo_texto)

            print(f'O ator com o maior número de filmes é: {ator_mais_filmes}\n', file=arquivo_texto)
            
            print(f'Quantidade de filmes: {maior_numero_filmes}\n', file=arquivo_texto)


ator_com_mais_filmes('actors.csv', 'etapa-1.txt')
