# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
# Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
# É o arquivo estudantes.csv de seu exercício.
# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
# Nome do estudante
# Três maiores notas, em ordem decrescente
# Média das três maiores notas, com duas casas decimais de precisão
# O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
# Exemplo:

# Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67

# Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções: round, map, sorted 

import csv

def processar_arquivo_csv(arquivo):
   
    with open(arquivo, 'r', encoding='UTF-8') as file:
       
        reader = csv.reader(file)
        
       
        linhas = list(reader)
        
       
        linhas_ordenadas = sorted(linhas, key=lambda x: x[0])
        
        
        for row in linhas_ordenadas:
            
            nome = row[0]
            
            
            notas = list(map(int, row[1:]))
            
            
            notas_ordem_decrescente = sorted(notas, reverse=True)
            
           
            tres_maiores_notas = notas_ordem_decrescente[:3]
            
            media = round(sum(tres_maiores_notas) / 3, 2)
            
          
            print(f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media}")


processar_arquivo_csv('exercicios-python/estudantes.csv')