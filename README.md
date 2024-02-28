# DAG de ingestão de dados
Esse repositório contém o código para execução de uma DAG (Directed Acyclic Graph), orquestrada pelo Apache Airflow, responsável por realizar a ingestão de músicas de uma playlist do Spotify para um banco de dados PostgreSQL.

Acesse nossos recursos: 🔗
- [Engenharia de Dados](./markdowns/engenharia_dados.md)
- [Exemplo de uso da DAG](./markdowns/dag_ingestao.md)

## Estrutrura do projeto
- `dags:` DAGS
- `dev:` scripts utilizados para desenvolvimento das tarefas da DAG
- `markdown:` recursos de documentação do pipeline
- `docker-compose.yaml:` configuração Docker para execução do Apache Airflow no Docker

## Pré-requisitos
Antes de executar esta aplicação, é necessário garantir que você tenha os seguintes pré-requisitos instalados:

- Python (versão 3.11.0 ou superior)
- Docker e docker-compose
- PostgreSQL 
- Conta de desenvolvedor no Spotify para acesso à API - [documentação SpotifyAPI](https://developer.spotify.com/)
  

## Como Executar
Siga os passos abaixo para executar a aplicação:

1. Clone este repositório
   ```
   git clone https://github.com/AnaJuliaMM/comite_2602.git
   ```
2.  Utilize o arquivo _docker-compose.yaml_ para execução do Apache Airflow de acordo com o seguinte tutorial:
     -  [Instale e configure o Apache Airflow em Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#initialize-the-data:~:text=initialize%20the%20database.-,Setting%20the%20right%20Airflow%20user,-On%20Linux%2C%20the)
3. Crie um banco de dados no PostgreSQL e cria a seguinte tabela:      
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
2. Acesse a interface gráfica do Apache Airflow em `localhost:8080`
3. No arquivo `airflow_variables.json` insira os valores das variáveis de acordo com seu contexto
4. Na seção _Variables_ da interface, faça a o upload do arquivo e a importação das variáveis de ambiente
5. Mude o status da DAG para ativo e execute o pipeline
6. Visualize os dados inseridos no banco de dados:

![Captura de tela 2024-02-26 105852](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/29ab1cc4-0843-4711-85f7-7edf9ff1d55c)


Muito obrigada! Em caso de dúvida ou sugestão estamos à disposição 😄😉
