# 2. Apresente a média da coluna contendo o número de filmes.

import pandas as pd

df = pd.read_csv('Sprint_07/exercicios-python/actors.csv')

media = df['Number of Movies'].mean()
print("A média da coluna 'Number of Movies' é:", media)

# RESULTADO
# A média da coluna 'Number of Movies' é: 37.88