# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

# Use as variáveis abaixo para representar cada operação matemática
# mediana
# media
# valor_minimo 
# valor_maximo 

import random

random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = min(random_list)
valor_maximo = max(random_list)


random_list.sort()


tamanho = len(random_list)
if tamanho % 2 == 0:
    indice1 = tamanho // 2
    indice2 = indice1 - 1
    mediana = (random_list[indice1] + random_list[indice2]) / 2
else:
    indice = tamanho // 2
    mediana = random_list[indice]


media = sum(random_list) / tamanho


print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")