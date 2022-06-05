# Stroke Prediction: Utilizando Arvores de decisão para detectar Acidentes Vasculares Cerebrais

## Quem sou eu:

Meu nome é Silvano Lopes, sou formado no Bacharelado em Ciências e Tecnologia e Engenharia de Computação pela Universidade Federal do Rio Grande do Norte (UFRN). Atualmente curso o Mestrado em Engenharia Elétrica e Computação pela UFRN, por meio do Programa de Pós Graduação em Engenharia Elétrica e Computação, na linha de pesquisa de processamento inteligente da informação.

## Motivação:

De acordo com a OMS (Organização Mundial de Saúde) os acidentes vasculares cerebrais (AVC) são responsáveis por 11% das mortes no planeta, sendo considerada a segunda maior causadora de mortes no mundo. de acordo com o ministério da saúde, Quanto mais rápido for o diagnóstico e o tratamento do AVC, maiores serão as chances de recuperação completa. Desta forma, torna-se primordial ficar atento aos sinais e sintomas e procurar atendimento médico imediato.

## Objetivo:

O objetivo desse projeto é aplicar a metodologia de Machine Learning Operations (MLOps),vista na disciplina EEC1509 - Aprendizagem de Máquina, para permitir que uma inteligência artificial seja capaz de prever quando uma pessoa possui predisposição a sofrer um possivel AVC, utilizando de informações sociais (tipo de emprego, tipo de moradia, gênero) e fisicas (Como dados da taxa de glicose média no sangue, Indice de Massa corporal) de um individuo. As informações foram coletadas a partir do dataset [Stroke-Prediction-Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) disponivel no [Kaggle](https://www.kaggle.com/) 

## Metodologia e Ferramentas:

Para Atingir o Objetivo proposto, foi necessário a realização dos seguintes passos:

1 - Por meio do [google Colab](https://colab.research.google.com), realizou-se a importação o conjunto de dados para a aplicação da ETL no conjunto de dados, sempre buscando armazenar os artefatos na plataforma de versionamento de dados [Weights and Bias](https://wandb.ai/site).

2 - Uma vez tratado os dados, realizou-se o as etapas de separação do conjunto de dados em treinamento e teste, aplicando o pipeline proposto em aula, para colocar as informações em conformidade com a entrada de dados de um classificador binário, além de buscar os melhores modelos de acordo com os hiperparametros utilizados. Nessa etapa foi utilizado o [Scikit-Learn](https://scikit-learn.org/stable/) para o treinamento da ML e As métricas de desempenho da IA foram armazenadas no [wandb](https://wandb.ai/site).

3 - Uma vez que foi gerado o melhor modelo de ML, nessa etapa foi necessário desenvolver e testar uma API capaz de utilizar a o modelo de IA para realizar as predições, sempre aplicando as melhores práticas de Continuous Integration (CI) e Continuous Delivery (CD). Nessa etapa foram utilizados o [github actions](https://docs.github.com/pt/actions) para o CI e o [Heroku](https://www.heroku.com/) para o CD. O desenvolvimento e testes da API foram feitos por meio do [FastAPI](https://fastapi.tiangolo.com/) e [PyTest](https://docs.pytest.org/en/7.1.x/).  

## Resultados:

O Maior desafio nesse tipo especifico de problema é o desbalanceamento natural das classes de saída. Em outras palavras, a classe minoritária possui um conjunto de dados muito pequeno quando comparado com a classe marjoritária, muito ocasionado pela raridade do evento (não vai ser todo mundo que teve ou vai ter um AVC). Para uma máquina de aprendizado trabalhando com classificação binária é um grande problema pois essa diferença vai gerar uma falsa precisão na etapa de treinamento, com valores acima dos 90%, sendo que na realidade, essa precisão só acontece por conta da grande diferença entre as classes minoritária e marjoritária. a tabela abaixo mostra os resultados do conjunto de testes e ilustra bem o problema:

|             | precision | recall    | f1-score  | support
|-------------|-----------|-----------|-----------|---------
| Classe 0    |      0.96 |      0.96 |    0.96   |   1458
| Classe 1    |      0.16 |      0.15 |    0.15   |     75

|             | precision | recall    | f1-score  | support
|-------------|-----------|-----------|-----------|---------
|    accuracy |           |           |    0.92   |   1533
|   macro avg |      0.56 |    0.55   |    0.56   |   1533
|weighted avg |      0.92 |    0.92   |    0.92   |   1533

Esse desbalanceamento das classes impacta na geração de falsos positivos e negativos. A matriz de confusão abaixo mostra bem o impacto do desbalanceamento dessas classes.

![confusion_matrix](https://user-images.githubusercontent.com/13625437/172027757-4bd229df-f750-4836-ac00-bf340b768f99.png)

Para mitigar esse problema, é possivel aplicar métodos de balanceamento de classes, de forma que o nivelamento dessas classes gere resultados mais próximos da realidade. Infelizmente, nesse projeto não foi possivel aplicar tais técnicas (ainda...)

![Hyperparameter_tuning](https://user-images.githubusercontent.com/13625437/172027387-34d9afe2-2af1-49ea-aa7b-8954475afa47.png)
