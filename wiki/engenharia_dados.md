
# Introdução a Engenharia de dados

### O que é Engenharia de Dados?

A engenharia de dados é a área responsável por desenvolver, implementar e manter um ambiente propício para armazenamento e processamento de grandes quantidades de dados. Esses ambientes tem processos que chamamos de pipelines, que contém etapas relacionadas a fluxos de dados, desde a extração passando pelo armazenamento até a distribuição dos dados para consumo.

### Pipeline
É um processo composto por várias etapas, que possuem essencialmente 3 passos: Extração na origem, processamento e carregamento no destino
![Pipelines](https://blog.zooxsmart.com/hubfs/imagem-pt-Artigo-de-Blog--Pipeline-de-dados.jpg)
### Diferença entre Engenheiro de dados e Analista de dados

Os engenheiros de dados são responsáveis por reunir, validar e preparar os dados, garantindo sua qualidade e disponibilidade para análise. Por outro lado, os analistas de dados utilizam esses dados preparados para extrair insights e promover melhores decisões de negócios por meio de análises avançadas e modelagem estatística

### Batch vs. Streaming

Existem duas abordagens principais para processar dados: Batch e Streaming.

- Batch envolve processar grandes volumes de dados estáticos em intervalos definidos. 

- Streaming envolve processar dados continuamente, à medida que são gerados em tempo real.

Ambas as abordagens têm suas vantagens e desvantagens. O Batch é eficaz para processar grandes volumes de dados de uma só vez, enquanto o Streaming oferece análises em tempo real, mas pode exigir mais recursos.

![Batch vs Streaming](https://k21academy.com/wp-content/uploads/2020/11/BatchProcessingStreamProcessing_Diagram-02.png)

# [Apache Airflow](https://airflow.apache.org/)

O Apache Airflow é uma plataforma de código aberto para **criar**, **agendar** e **monitorar** pipelines de dados (ou DAGs). Ele permite definir tarefas dentro de **fluxos de trabalho interativos e visuais**, facilitando a orquestração de processos complexos.
Todos os fluxos de trabalhos do Apache Airflow (DAG) são definidos em código Python. 


### DAGs (Directed Acyclic Graphs)

Um conceito importante no Apache Airflow são os DAGs. Eles são usados para representar visualmente o fluxo de trabalho de dados, mostrando a dependência entre as tarefas.

![Exemplo de DAG](https://cdn-us1.hash.ai/site/dag-example.png)


### [Exemplo de DAG](dag_ingestao.md)

Temos um pipeline de dados que envolve a coleta de dados de uma fonte, a transformação desses dados e, finalmente, o carregamento dos dados em um armazenamento de destino.
