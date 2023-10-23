import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os


nome_arquivo_csv = 'pokedex.csv'
# Faz uma requisição HTTP para obter o conteúdo da página
url = 'https://pokemondb.net/pokedex/stats/gen1'
response = requests.get(url)
content = response.text

# Parseia o conteúdo HTML com o BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
tabela = soup.find('table', {'class': 'data-table'})

# Cria um arquivo CSV para escrita com codificação UTF-8
with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)

    # Percorre as linhas da tabela e extrai os dados
    for linha in tabela.find_all('tr'):
        dados_pokemon = []

        # Percorre as células da linha e extrai o conteúdo
        for celula in linha.find_all('td'):
            dados_pokemon.append(celula.text.strip())

        # Escreve os dados do Pokémon no arquivo CSV
        writer.writerow(dados_pokemon)





arquivo_entrada = nome_arquivo_csv
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


df = pd.read_csv('pokedex.csv',header=None)
nome_colunas = ['id','nome','type','total','hp','attack','defense','sp_atk', 'sp_def','speed']
df.columns = nome_colunas
print(df.head(10))