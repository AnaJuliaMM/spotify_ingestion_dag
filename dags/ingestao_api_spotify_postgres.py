from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
import requests
import psycopg2


#  Etapa 1 - Faz a requisição do Token
def requisitar_token():

    # URL para solicitar o token de acesso
    token_url = 'https://accounts.spotify.com/api/token'

    # Dados para a solicitação do token
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': Variable.get("client_id"),
        'client_secret': Variable.get("client_secret")
    }

    # Fazer a solicitação do token
    token = requests.post(token_url, data=token_data)

    # Verificar a resposta
    if token.status_code == 200:
        # Se a resposta for bem sucedida, imprima os dados
        return token.json()['access_token']

    else:
        # Se não, imprima o status code
        return token.status_code
# Etapa 2 - Faz a requisição das músicas
def ingestao(task_instance):
    try:

        url = "https://api.spotify.com/v1/playlists/4qNBEfMO6fdn2k9xuFVeDQ/tracks"

        token = task_instance.xcom_pull(task_ids="requisitar_token")
        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Enviar solicitação GET para a API do Spotify com o token de acesso no cabeçalho de autorização
        response = requests.get(url, headers=headers)
        dados = response.json()

        # Verificar se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # conectar com o banco
            try:
             # Conectar com o banco de dados
                conn = psycopg2.connect(
                host= Variable.get("host"),
                user= Variable.get("user"),
                password= Variable.get("password"),
                database= Variable.get("database")
                    )
                cursor = conn.cursor()

                # Construção e execução da inserção de dados
                for item in dados["items"]:
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
                        return f"Erro ao inserir dados no PostgreSQL:{e}"

                # Confirmação da operação de inserção de dados e encerramento da conexão com o banco de dados
                conn.commit()

            except Exception as e:
                return f"Erro ao conectar com o PostgreSQL: {e}"
            finally:
                cursor.close()
                conn.close()
                return f"Conexão com o PostgreSQL fechada"

        else:
            # Se a solicitação não for bem-sucedida, imprima o código de status
            return response.status_code

    except requests.RequestException as e:
        # Se ocorrer um erro ao fazer a solicitação, imprima o erro
        return f"Erro ao fazer solicitação para a API do Spotify:, {e}"


with DAG ("ingestao_api_spotify_postgres", start_date= datetime(2024,2,22), schedule_interval= "30 * * * *", catchup= False) as dag:
    # task 1  
    requisitar_token= PythonOperator(
    task_id= "requisitar_token", 
    python_callable= requisitar_token
    )

    # task 2
    ingestao= PythonOperator(
    task_id= "ingestao",
    python_callable= ingestao
    )

    # interligando tasks
    requisitar_token >> ingestao
