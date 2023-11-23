# A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.

import csv

def faturamento_por_ator(arquivo_csv, arquivo_saida):
    atores_faturamento = {}

    with open(arquivo_csv, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ator = row['Actor']
            faturamento = float(row['Total Gross'])

            if ator in atores_faturamento:
                atores_faturamento[ator] += faturamento
            else:
                atores_faturamento[ator] = faturamento

    atores_ordenados = sorted(atores_faturamento.items(), key=lambda x: x[1], reverse=True)

    with open(arquivo_saida, 'w') as arquivo_txt:
        
        print('A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.\n', file=arquivo_txt)

        print("Ator\t\tFaturamento Total Bruto", file=arquivo_txt)
        
        print("--------------------------------------", file=arquivo_txt)

        max_length = max(len(ator) for ator, _ in atores_ordenados)
        for ator, faturamento in atores_ordenados:
            linha = "{:<{}}\t{}".format(ator, max_length, faturamento)
            
            print(linha, file=arquivo_txt)

        print("--------------------------------------", file=arquivo_txt)
        


faturamento_por_ator('actors.csv', 'etapa-5.txt')



