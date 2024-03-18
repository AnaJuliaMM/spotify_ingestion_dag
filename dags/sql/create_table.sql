CREATE TABLE IF NOT EXISTS Musica (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    duracao_ms INTEGER NOT NULL,
    artistas VARCHAR(255) NOT NULL,
    nome_album VARCHAR(255),
    data_lancamento DATE NOT NULL,
    total_musicas_album INTEGER
    );