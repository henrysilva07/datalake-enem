# Projeto: Construindo um Datalake no ambiente AWS

![image](https://user-images.githubusercontent.com/89877903/177229848-c75bfcb4-36f0-4249-a9ba-9f75bc347485.png)


## Motivação do Projeto

Uma empresa do setor de educação deseja construir um datalake para armazenar informações do ENEM com o intuito de entender o perfil dos candidatos e assim direcionar melhor suas campanhas dos seus cursos preparatórios com base nos dados dos exames anteriores. 

Posto isso, eles precisam de um engenheiro de dados que construa todo o ambiente do seu datalake, bem como desenvolva suas pipelines de maneira simples e peformática. 

## Descrição do Projeto 

Este projeto será criado em três passos:
  * Coleta dos arquivos do ENEM por meio de um script Python e armazenamento dos arquivos dentro de um bucket S3; 
  * Processamento dos dados utilizando o EMR da AWS, coletando os dados da raw data e armazenando na zona de staging;
  * Criação de Crawlers com o AWS Glue e utilizando a engine de datalake Athena para consultar os dados; 

### 1 Passo 

**Coleta dos dados do ENEM**

A coleta de dados foi realizada por meio do Python, utilizando a biblioteca requests foi possível consumir os dados direto da url e ,assim, extraí-los e armazená-los localmente. 

![image](https://user-images.githubusercontent.com/89877903/177228283-d01ccba8-61be-4b03-a57a-963aa761b15f.png)

**Criação do Bucket no S3 e Realizando o Upload dos arquivos**

Em seguida, foi criado o bucket no s3 que atuará como repositório do nosso datalake, bem como o upload dos dados na raw data

![image](https://user-images.githubusercontent.com/89877903/177228747-86c93dbd-d1e0-4218-8d63-7acf40968fd5.png)


### 2 Passo 

**Processando os dados no EMR**

Agora que temos os nossos dados dentro do bucket , precisamos processar esses dados para um formato colunar para reduzir o consumo de memória, além de facilitar a varredura dos crawlers. O formato que será utilizado é o parquet. 

![image](https://user-images.githubusercontent.com/89877903/177229089-910bfd77-60e7-47dc-843c-33f5e52a3779.png)

### 3 Passo 

**Criação de Crawlers e Utilizando o Athena para analisar os dados**

Uma das funcionalidades do Aws Glue é a criação de Crawlers que permitem entender o padrão de determinados dados dentro do seu datalake e então seja possível analisar esses dados com comandos SQL pelo Athena. Aqui é interessante que seja analisado os dados no formato colunar , como o parquet, pois o processo sera mais rápido e por consequência mais barato. 

Após a etapa de execução do Crawler, podemos analisar os dados utilizando a interface do Athena por meio de comandos SQL

![image](https://user-images.githubusercontent.com/89877903/177229508-d1831df1-4600-4f40-ad37-6a396c944837.png)

Todos os arquivos utilizados se encontram dentro deste repositório!





