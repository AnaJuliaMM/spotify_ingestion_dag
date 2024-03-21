# DAG de ingestão de dados

Esse repositório contém o código para execução de uma DAG (Directed Acyclic Graph), orquestrada pelo Apache Airflow, responsável por realizar a ingestão de músicas de uma playlist do Spotify para um banco de dados PostgreSQL.

Acesse nossos recursos: 🔗

- [Engenharia de Dados](./wiki/engenharia_dados.md)
- [Exemplo de uso da DAG](./wiki/dag_ingestao.md)

## Estrutrura do projeto

- `dags:` arquivo da DAG
- `wiki:` recursos de documentação do pipeline
- `airflow_variables.json`: variáveis de ambiente para serem importadas no Airflow
- `docker-compose.yaml:` configuração Docker para execução do Apache Airflow no Docker

## Pré-requisitos

Antes de executar esta aplicação, é necessário garantir que você tenha os seguintes pré-requisitos instalados:

- Python (versão 3.11.0 ou superior)
- Docker (versão 24.0.6 ou superior)
- Docker-compose (versão 2.21.0-desktop.1 ou superior)
- PostgreSQL (versão 15 ou superior)
- Conta de desenvolvedor no Spotify para acesso à API - [documentação SpotifyAPI](https://developer.spotify.com/)

## Como Executar

Siga os passos abaixo para executar a aplicação:

1. Clone este repositório

   ```
   git clone https://github.com/AnaJuliaMM/comite_2602.git
   ```

2. Crie um arquivo `.env` na raiz do projeto e insira a seguinte configuração:

   ```
   AIRFLOW_UID=5000
   ```

3. Inicie o Apache Airflow
   ```
   docker-compose up -d
   ```
4. Acesse a interface gráfica do Apache Airflow em `localhost:8080`

5. Crie um banco de dados no PostgreSQL

6. No arquivo `airflow_variables.json` insira os valores das variáveis de acordo com seu contexto

7. Na seção _Variables_ da interface, faça a o upload do arquivo e a importação das variáveis de ambiente

8. Mude o status da DAG para ativo e execute o pipeline

## Resultado esperado

Visualize os dados inseridos no banco de dados ✨

![Captura de tela 2024-02-26 105852](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/29ab1cc4-0843-4711-85f7-7edf9ff1d55c)
