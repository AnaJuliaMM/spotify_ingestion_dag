# DAG de ingestão de dados
Esse repositório contém o código para execução de uma DAG (Directed Acyclic Graph), orquestrada pelo Apache Airflow, responsável por realizar a ingestão de músicas de uma playlist do Spotify para um banco de dados PostgreSQL.

Acesse nossos recursos: 🔗
- [Engenharia de Dados](./markdowns/engenharia_dados.md)
- [Documentação da DAG](./markdowns/dag_ingestao.md)

## Estrutrura do projeto
- `dags:` DAGS
- `markdown:` recursos de documentação
- `postgres_conn:` scripts Python utilizados antes do desenvolvimento da DAG para execução manual
- `docker-compose.yaml:` executar Apache Airflow no Docker

## Pré-requisitos
Antes de executar esta aplicação, é necessário garantir que você tenha os seguintes pré-requisitos instalados:

- Python (versão 3.11.0 ou superior)
- Apache Airflow - [tutorial de instalaçao e configuração](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#initialize-the-database)
- PostgreSQL - [tutotial de download](https://www.postgresql.org/download/)
- Conta de desenvolvedor no Spotify para acesso à API
  
Certifique-se de ter configurado corretamente o Apache Airflow e o PostgreSQL antes de prosseguir com a execução da aplicação.

## Como Executar
Siga os passos abaixo para executar a aplicação:

1. Inicie o servidor do Apache Airflow
2. Certifique-se de que o PostgreSQL esteja em execução e acessível. Crie o banco de dados e a tabela para receber os dados
3. Configure as variáveis de ambiente necessárias (credenciais do usuário e credenciais de conexão com o banco de dados)
4. Execute a DAG de ingestão de músicas do Spotify no Apache Airflow.
5. Monitore o progresso da execução da DAG no painel do Apache Airflow e verifique se não há erros relatados.



## Resultado esperado
![Captura de tela 2024-02-26 105852](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/29ab1cc4-0843-4711-85f7-7edf9ff1d55c)


Muito obrigada! Em caso de dúvida ou sugestão estamos à disposição 😄😉
