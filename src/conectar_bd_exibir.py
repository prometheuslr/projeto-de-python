import sqlite3

conn = sqlite3.connect('pokedex_primeira_geracao.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM pokedex")

dados = cursor.fetchall()

tabela = 'pokedex'

cursor.execute(f'PRAGMA table_info({tabela})')
colunas = cursor.fetchall()

nomes_colunas = [coluna[1] for coluna in colunas]


pokedex = []

for linha in dados:
    pokedex.append(linha)

conn.close()

pokedex_dados = [i if not isinstance(i, tuple) else list(i) for i in pokedex]

quan_pok = len(pokedex_dados)

print(f"|{nomes_colunas[0]}|{nomes_colunas[1]}|{nomes_colunas[2]}|{nomes_colunas[3]}|{nomes_colunas[4]}|{nomes_colunas[5]}|"+
      f"{nomes_colunas[6]}|{nomes_colunas[7]}|{nomes_colunas[8]}|{nomes_colunas[9]}|")
for i in range(0,quan_pok):
    print(f'|{pokedex_dados[i]}|')