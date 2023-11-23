# 3. Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd
import numpy as np

df = pd.read_csv('Sprint_07/exercicios-python/actors.csv')

ator_maior_media = df.loc[df['Average per Movie'].idxmax(), 'Actor']
media_filmes = df['Average per Movie'].max()


print("O ator/atriz com o maior média por filmes é:", ator_maior_media)
print("Média por filmes:", media_filmes)

# RESULTADO
# Média por filmes: 451.8