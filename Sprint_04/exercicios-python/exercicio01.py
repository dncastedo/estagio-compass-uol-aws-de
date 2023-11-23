# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
# Você deverá aplicar as seguintes funções no exercício:
# map, filter, sorted, sum
# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
# a lista dos 5 maiores números pares em ordem decrescente;
# a soma destes valores.

def numeros():
    eh_par = lambda x: x % 2 == 0
    
    with open('exercicios-python/number.txt', 'r') as arquivo:
        numeros = list(map(int, arquivo.read().splitlines()))
    
    numeros_pares = list(filter(eh_par, numeros))
    
    numeros_ordenados = sorted(numeros_pares, reverse=True)
    
    top_5_numeros = numeros_ordenados[:5]
    
    soma_top_5_numeros = sum(top_5_numeros)
    
    print(top_5_numeros)
    print(soma_top_5_numeros)


numeros()