# Leia o arquivo actors.csv e codifique os cálculos solicitados 
#sobre o conjunto de dados utilizando a biblioteca Pandas. 
# Adicione apenas a resposta da questões nos espaços indicados. 
# Seu código-fonte deverá estar no Github.

# 1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('Sprint_07/exercicios-python/actors.csv')

ator_mais_filmes = df.loc[df['Number of Movies'].idxmax(), 'Actor']
quantidade_filmes = df['Number of Movies'].max()


print("O ator/atriz com o maior número de filmes é:", ator_mais_filmes)
print("Número de filmes:", quantidade_filmes)

#RESULTADO
# Número de filmes: 79










