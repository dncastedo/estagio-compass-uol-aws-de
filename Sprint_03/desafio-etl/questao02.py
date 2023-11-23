# Apresente a  média de faturamento bruto por ator.

import csv


def media_faturamento_por_ator(arquivo_csv, arquivo_saida):
    nomes_atores = []
    valores_ator = []
    
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        arquivo_lido = csv.DictReader(arquivo)
        for linha in arquivo_lido:
            nome_ator = linha['Actor']
            valor_ator = float(linha['Average per Movie'])
            
            nomes_atores.append(nome_ator)
            valores_ator.append(valor_ator)
    
    
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_texto:
        max_length = max(len(nome) for nome in nomes_atores)
        
        
        print("{:<{}}\t{}".format("Ator", max_length, "Média de Faturamento"), file=arquivo_texto)
        print("-" * (max_length + 16), file=arquivo_texto)
        
        
        for nome, valor in zip(nomes_atores, valores_ator):
            linha = "{:<{}}\t{}".format(nome, max_length, valor)
            print(linha, file=arquivo_texto)

        print("-" * (max_length + 16), file=arquivo_texto)


media_faturamento_por_ator('actors.csv', 'etapa-2.txt')
