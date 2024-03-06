# Migrações

Este é um projeto que utiliza Migrations para criação e versionamento do banco de dados utilizados na pipeline

### O que são Migrações?
As migrações são scripts que descrevem as alterações no esquema do banco de dados ao longo do tempo. Eles definem como as tabelas são criadas, modificadas ou excluídas. Isso significa que você pode versionar as mudanças no esquema do banco de dados, permitindo que você reverta para versões anteriores ou atualize para versões mais recentes conforme necessário, mantendo a consistência dos dados.

### SQLAlchemy e Alembic
- **SQLAlchemy**: É uma biblioteca de mapeamento objeto-relacional (ORM) para Python, que fornece uma interface de alto nível para trabalhar com bancos de dados relacionais.
- **Alembic**: É uma ferramenta de migração de banco de dados para SQLAlchemy. Ela fornece uma maneira simples de gerenciar e aplicar Migrations em um banco de dados SQLAlchemy.

# Estrutura do banco de dados da pipeline
Essa pipeline utiliza um banco de dados do SDBD PostgreSQL. Os dados ingeridos são armazenados numa tabela denominada "Musica". 

A seguir, o código SQL de cada estrutura:


**Criação do banco de dados** 
   ```
   CREATE DATABASE Playlist;
   ```

**Criação da tabela**
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

# Tutorial de execução com Migrations
1. Crie e ative um ambiente virtual 

    ```
    cd migrations
    python -m venv venv
    venv/scripts/activate
    ```

2. Abra o arquivo `alembic.init` e insira as credenciais de conexão com o seu banco de dados no trecho semelhante ao a seguir:
    ```
    sqlalchemy.url = postgresql://user:password@host:port/db_name

    ```

3. Execute a criação da tabela

    ```
    alembic upgrade head
    ```

**Obs: A migração para criação da tabela (migração inicial) já está contido na pasta `versions`, dessa forma, só é preciso executar o comando acima.**
