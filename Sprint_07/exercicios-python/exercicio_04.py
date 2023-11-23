# 4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd
import numpy as np

df = pd.read_csv('Sprint_07/exercicios-python/actors.csv')

frequencia = df['#1 Movie'].value_counts()

maior_frequencia = frequencia.max()
filmes_mais_frequentes = frequencia[frequencia == maior_frequencia]

print("Filme(s) mais frequente(s):")
for filme, frequencia in filmes_mais_frequentes.items():
    print(filme, "- Frequência:", frequencia)

# RESULTADO
# The Avengers - Frequência: 6