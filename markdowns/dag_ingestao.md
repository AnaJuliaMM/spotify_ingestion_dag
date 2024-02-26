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

## Tarefas

A DAG é composta por uma série de tarefas interconectadas, formando um gráfico acíclico dirigido. Cada nó representa uma tarefa e as arestas indicam a ordem de execução. 
![Diagrama sem nome drawio](https://github.com/AnaJuliaMM/comite_2602/assets/123522605/faf67710-2a71-4e29-8ea5-7d47838797dc)

1. **`requisitar_token`**: Esta tarefa é responsável por autenticar-se na API do Spotify, obtendo um token de acesso necessário para realizar solicitações em nome do usuário.
2. **`ingestao`**: Uma vez autenticada, esta tarefa faz uma requisição à API do Spotify para obter as músicas contidas na playlist em questão. Por fim, as músicas obtidas são armazenadas no banco de dados PostgreSQL.



## Resultados



## Conclusão

A DAG de ingestão orquestrada pelo Apache Airflow é essencial para automatizar o processo de obtenção e armazenamento de músicas do Spotify em um banco de dados PostgreSQL. Ao dividir o fluxo de trabalho em tarefas distintas e interconectadas, garantimos uma execução eficiente e confiável do processo de ingestão.

Com esta explicação, esperamos ter fornecido uma compreensão clara da estrutura e funcionamento dessa DAG específica.
