import sqlite3

conn = sqlite3.connect('pokedex_primeira_geracao.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS pokedex (id PRIMARY KEY, nome TEXT, type TEXT, total NUBER, hp INTEGER, attack INTEGER, defense INTEGER, sp_atk INTEGER, sp_def INTEGER, speed INTEGER)''')

conn.commit()
conn.close()