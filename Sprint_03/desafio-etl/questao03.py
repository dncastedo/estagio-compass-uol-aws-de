# Apresente o ator/atriz com a maior média de faturamento por filme.

import csv

def encontrar_ator_com_mais_filmes(arquivo_csv, arquivo_saida):
    maior_media_faturamento = 0
    ator_maior_media = None

    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        arquivo_lido = csv.DictReader(arquivo)
        for linha in arquivo_lido:
            ator = linha['Actor']
            media_faturamento = float(linha['Average per Movie'])

            if media_faturamento > maior_media_faturamento:
                maior_media_faturamento = media_faturamento
                ator_maior_media = ator

    if ator_maior_media:
        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_texto:
            print('Apresente o ator/atriz com a maior média de faturamento por filme.\n', file=arquivo_texto)
            print(f'O ator com o maior média de faturamento por filme: {ator_maior_media}\n', file=arquivo_texto)
            print(f'Média Por Faturamento: {maior_media_faturamento}\n', file=arquivo_texto)


encontrar_ator_com_mais_filmes('actors.csv', 'etapa-3.txt')