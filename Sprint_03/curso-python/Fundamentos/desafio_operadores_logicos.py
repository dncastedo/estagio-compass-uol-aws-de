# Os Trabalhos

trabalho_terca = False
trabalho_quinta = False

"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # xor
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))

# "{}, {} = {}".format(1, False, 'resultado')