import psycopg2
import json
import requests

def request_token():
    # URL para solicitar o token de acesso
    token_url = 'https://accounts.spotify.com/api/token'

    # Dados para a solicitação do token
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': '',
        'client_secret': ''
    }

    # Fazer a solicitação do token
    token = requests.post(token_url, data=token_data)

    # Verificar a resposta
    if token.status_code == 200:
        # Se a resposta for bem sucedida, imprima os dados
        print(token.json())
        return token.json()['access_token']

    else:
        # Se não, imprima o status code
        print(f"Erro status : {token.status_code}") 
        return token.status_code

try:

    url = "https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n/tracks"

    token = request_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Enviar solicitação GET para a API do Spotify com o token de acesso no cabeçalho de autorização
    response = requests.get(url, headers=headers)

    # Verificar se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converter a resposta JSON em um dicionário Python
        dados_playlist = response.json()

        # Agora você pode usar os dados da playlist conforme necessário
        print("Nome da playlist:", dados_playlist)
    else:
        # Se a solicitação não for bem-sucedida, imprima o código de status
        print("Erro ao acessar a API. Código de status:", response.status_code)

except requests.RequestException as e:
    # Se ocorrer um erro ao fazer a solicitação, imprima o erro
    print("Erro ao fazer solicitação para a API do Spotify:", e)

# O restante do código está comentado porque não está sendo usado no momento

# try:
#     # Conectar com o banco de dados
#     conn = psycopg2.connect(
#                 host="localhost",
#                 user="postgres",
#                 password="12345678",
#                 database="playlist"
#             )
#     cursor = conn.cursor()


#     dados = request_api()
   

#     # Construção e execução da inserção de dados
#     for item in dados["tracks"]["items"]:
#         try:
#             # Acessar a chave 'track' do objeto item. Chave que armazena as informações das músicas 
#             track = item['track']

#             # Extrair os nomes dos artistas e concatenar usando a palavra 'e'
#             nomes_artistas = [artista['name'] for artista in track['album']['artists']]
#             artistas_str = ' e '.join(nomes_artistas)
            
#             # Tratar strings que contenham apóstrofos
#             track_name = track['name'].replace("'", "''")
#             album_name = track['album']['name'].replace("'", "''")
            
#             cursor.execute(
#                 f"INSERT INTO Musica (nome, duracao_ms, artistas, nome_album, data_lancamento, total_musicas_album) "
#                 f"VALUES ('{track_name}', {track['duration_ms']}, '{artistas_str}', '{album_name}', TO_DATE('{track['album']['release_date']}', 'YYYY-MM-DD'), {track['album']['total_tracks']})"
#             )

#         except psycopg2.Error as e:
#             print("Erro ao inserir dados no PostgreSQL:", e)

#     # Confirmação da operação de inserção de dados e encerramento da conexão com o banco de dados
#     conn.commit()

# except Exception as e:
#     print(e)
# finally:
#     cursor.close()
#     conn.close()
#     print('PostgreSQL connection is closed')




