# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
# Utilize a lista a seguir para testar sua função.
# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
def remover_duplicadas(lista):
    lista_sem_duplicadas = list(set(lista))
    return lista_sem_duplicadas

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_sem_duplicadas = remover_duplicadas(lista)

print(lista_sem_duplicadas)