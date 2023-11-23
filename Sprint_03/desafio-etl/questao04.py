# O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import csv

def filmes_mais_frequentes(arquivo_csv, arquivo_saida):
    filmes_frequentes = {}
    max_frequencia = 0

    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        arquivo_lido = csv.DictReader(arquivo)
        for linha in arquivo_lido:
            filme = linha['#1 Movie']
            if filme in filmes_frequentes:
                filmes_frequentes[filme] += 1
            else:
                filmes_frequentes[filme] = 1
            
            if filmes_frequentes[filme] > max_frequencia:
                max_frequencia = filmes_frequentes[filme]

    filmes_mais_frequentes = []
    for filme, frequencia in filmes_frequentes.items():
        if frequencia == max_frequencia:
            filmes_mais_frequentes.append((filme, frequencia))

    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_texto:
        for filme, frequencia in filmes_mais_frequentes:
            print('O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.\n', file=arquivo_texto)
            print(f'Filme: {filme}\n', file=arquivo_texto)
            print(f'Frequência: {frequencia}\n', file=arquivo_texto)
            print('---', file=arquivo_texto)

filmes_mais_frequentes('actors.csv', 'etapa-4.txt')
