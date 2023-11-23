# Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
# Defina o atributo cor de sua classe , 
# de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
# Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
# Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
# “O avião de modelo “x” possui uma velocidade máxima de “y”, 
# capacidade para “z” passageiros e é da cor “w”.
# Sendo x, y, z e w cada um dos atributos da classe “Avião”.
# Valores de entrada:
# modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
# modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
# modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

class Avião:
    cor = "azul"

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade


entradas = [
    {"modelo": "BOIENG456", "velocidade_maxima": "1500 km/h", "capacidade": "400 passageiros"},
    {"modelo": "Embraer Praetor 600", "velocidade_maxima": "863 km/h", "capacidade": "14 passageiros"},
    {"modelo": "Antonov An-2", "velocidade_maxima": "258 km/h", "capacidade": "12 passageiros"}
]


aviões = []
for entrada in entradas:
    avião = Avião(entrada["modelo"], entrada["velocidade_maxima"], entrada["capacidade"])
    aviões.append(avião)


for avião in aviões:
    print(f"O avião de modelo {avião.modelo} possui uma velocidade máxima de {avião.velocidade_maxima}, capacidade para {avião.capacidade} e é da cor {avião.cor}.")
