import sqlite3
import csv 
import os

arquivo_entrada = 'pokedex.csv'
arquivo_saida = 'pokedex_sem_primeira_linha.csv'

# Abra o arquivo de entrada
with open(arquivo_entrada, 'r', newline='') as arquivo_csv_entrada:
    leitor_csv = csv.reader(arquivo_csv_entrada)

    # Leia todas as linhas do arquivo CSV
    linhas = list(leitor_csv)

    # Verifique se a primeira linha está vazia
    if not linhas[0]:
        # Se a primeira linha estiver vazia, salve todas as outras linhas em um novo arquivo
        with open(arquivo_saida, 'w', newline='') as arquivo_csv_saida:
            escritor_csv = csv.writer(arquivo_csv_saida)
            escritor_csv.writerows(linhas[1:])


os.replace(arquivo_saida, arquivo_entrada)




conn = sqlite3.connect('pokedex_primeira_geracao.db')
cursor = conn.cursor()


with open('pokedex.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    for linha in leitor_csv:
        id = linha[0]
        nome = linha[1]
        type = linha[2]
        total = linha[3]
        hp = linha[4]
        attack = linha[5]
        defense = linha[6]
        sp_atk = linha[7]
        sp_def = linha[8]
        speed = linha[9]
        cursor.execute("INSERT INTO pokedex (id, nome,type,total,hp,attack,defense, sp_atk, sp_def, speed) VALUES (?, ?,?,?,?,?,?,?,?,?)",
                        (id, nome,type, total, hp, attack, defense, sp_atk, sp_def, speed))
        
conn.commit()
conn.close()
