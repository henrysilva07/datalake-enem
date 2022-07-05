# Projeto: Construindo um Datalake no ambiente AWS

## Motivação do Projeto

Uma empresa do setor de educação deseja construir um datalake para armazenar informações do ENEM com o intuito de entender o perfil dos candidatos e assim direcionar melhor suas campanhas dos seus cursos preparatórios com base nos dados dos exames anteriores. 

Posto isso, eles precisam de um engenheiro de dados que construa todo o ambiente do seu datalake, bem como desenvolva suas pipelines de maneira simples e peformática. 

## Descrição do Projeto 

Este projeto será criado em três passos:
  * Coleta dos arquivos do ENEM por meio de um script Python e armazenamento dos arquivos dentro de um bucket S3; 
  * Processamento dos dados utilizando o EMR da AWS, coletando os dados da raw data e armazenando na zona de staging;
  * Criação de Crawlers com o AWS Glue e utilizando a engine de datalake Athena para consultar os dados; 
