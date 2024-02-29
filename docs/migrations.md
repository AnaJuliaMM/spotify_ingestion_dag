# Criação do banco de dados

1. Crie um banco de dados no PostgreSQL com o nome desejado
ex:
   ```
   CREATE DATABASE Playlist;
   ```


2. Crie a seguinte tabela:  
    
   ```
   CREATE TABLE Musica (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    duracao_ms INTEGER NOT NULL,
    artistas VARCHAR(255) NOT NULL,
    nome_album VARCHAR(255),
    data_lancamento DATE NOT NULL,
    total_musicas_album INTEGER
    );
   ```
Assim, os dados provenientes da API serão tratados e inseridos adequadamente na tabela "Musica", garantindo correspondência com os nomes das colunas especificadas.