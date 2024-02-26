# Explicação da DAG de Ingestão 

Neste documento, vamos discutir a estrutura e o funcionamento de uma DAG (Directed Acyclic Graph) de ingestão, orquestrada pelo Apache Airflow. Essa DAG é responsável por realizar a ingestão de músicas de uma playlist do Spotify para um banco de dados PostgreSQL.

## Contexto 

Antes de entrarmos nos detalhes da DAG em si, é importante entendermos o contexto em que ela opera. 

### [Spotify API](https://developer.spotify.com/documentation/web-api)
A Spotify API é uma interface de programação que permite aos desenvolvedores acessarem  recursos e dados fornecidos pelo serviço de streaming de música Spotify. 
Neste projeto, utilizou-se o serviço que fornece uma lista com os detalhes das músicas que compõem uma playlist da qual o usuário é proprietário. [Obtenha itens da lista de reprodução (doc)](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks)
 
### [Apache Airflow](https://airflow.apache.org/)

O Apache Airflow é uma plataforma de código aberto para **criar**, **agendar** e **monitorar** fluxos de trabalho (ou DAGs). Ele permite definir tarefas dentro de **fluxos de trabalho interativos e visuais**, facilitando a orquestração de processos complexos.
Todos os fluxos de trabalhos do Apache Airflow (DAG) são definidos em código Python. 

### [XCOM - Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html)
No contexto do Apache Airflow, XCom (Cross Communication) é um sistema que permite a comunicação entre tarefas dentro de uma mesma DAG, permitindo o **compartilhamento de dados entre elas**. Isso é especialmente útil quando uma tarefa precisa passar informações para outra durante a execução do fluxo de trabalho. No entanto, os XCOMs são projetados **apenas para pequenas quantidades de dados**, ele não deve ser utilizado para passar grandes valores, como dataframes. 

## Tarefas 📆

![Diagrama sem nome drawio](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/faf67710-2a71-4e29-8ea5-7d47838797dc)

A troca de dados entre as tarefas acontece utilizando o serviço XCOM para transmissão do token da API.

## Execução 
### 1. Playlist
Uma playlist personalizada foi criada para a execução da DAG: [Playlist das estagiárias Squad 404](https://open.spotify.com/playlist/1BZo9URfhmlnt67zRYgM79).

### 2. Banco de dados
Foi criado um banco de dados no PostgreSQL, e construída uma tabela para armazenar as informações selecionadas

![Captura de tela 2024-02-26 105656](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/e955aa29-a796-457d-9d27-e4e68acf9498)


### 3. Código da DAG
- Código da DAG: [ingestao_api_spotify_postgres.py](../dags/ingestao_api_spotify_postgres.py)
- Variáveis de ambiente:
  
  <img width="900" alt="image" src="https://github.com/AnaJuliaMM/comite_2602/assets/123522605/8e00b9c9-8f19-49db-96ab-3a27226a36b2">
- Execução:
  
  https://github.com/AnaJuliaMM/comite_2602/assets/123522605/8a97abae-a940-4210-a961-e75fef4639b6
- XCOM:
  
   <img width="700" alt="image" src="https://github.com/AnaJuliaMM/comite_2602/assets/123522605/8215c95d-8cff-4b13-9f01-b7767a23f3fc">



### 4. Dados ingeridos
Após a execução da DAG, os dados foram ingeridos na tabela:

![Captura de tela 2024-02-26 105852](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/29ab1cc4-0843-4711-85f7-7edf9ff1d55c)


## Conclusão

A DAG de ingestão orquestrada pelo Apache Airflow é essencial para automatizar o processo de obtenção e armazenamento de músicas do Spotify em um banco de dados PostgreSQL. Ao dividir o fluxo de trabalho em tarefas distintas e interconectadas, garantimos uma execução eficiente e confiável do processo de ingestão.

Com esta explicação, esperamos ter fornecido uma compreensão clara da estrutura e funcionamento dessa DAG específica.😄
