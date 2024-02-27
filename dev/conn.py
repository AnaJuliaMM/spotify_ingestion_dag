# Esse script extrai dados do arquivo "output" que contém uma amostra dos dados da API e os insere no banco de dados 

import psycopg2
import json

try:
    # Conectar com o banco de dados
    conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="12345678",
                database="playlist"
            )
    cursor = conn.cursor()

   # Abre o arquivo 'dados.json' para leitura
    with open('./sample_data/template_1.json', 'r', encoding='utf-8') as arquivo:
    # Carrega os dados JSON do arquivo em um dicionário Python
        dados = json.load(arquivo)

    # Construção e execução da inserção de dados
    for item in dados["tracks"]["items"]:
        try:
            # Acessar a chave 'track' do objeto item. Chave que armazena as informações das músicas 
            track = item['track']

            # Extrair os nomes dos artistas e concatenar usando a palavra 'e'
            nomes_artistas = [artista['name'] for artista in track['album']['artists']]
            artistas_str = ' e '.join(nomes_artistas)
            
            # Tratar strings que contenham apóstrofos
            track_name = track['name'].replace("'", "''")
            album_name = track['album']['name'].replace("'", "''")
            
            cursor.execute(
                f"INSERT INTO Musica (nome, duracao_ms, artistas, nome_album, data_lancamento, total_musicas_album) "
                f"VALUES ('{track_name}', {track['duration_ms']}, '{artistas_str}', '{album_name}', TO_DATE('{track['album']['release_date']}', 'YYYY-MM-DD'), {track['album']['total_tracks']})"
            )

        except psycopg2.Error as e:
            print("Erro ao inserir dados no PostgreSQL:", e)

    # Confirmação da operação de inserção de dados e encerramento da conexão com o banco de dados
    conn.commit()

except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
    print('PostgreSQL connection is closed')

