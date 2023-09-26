
# Elasticidade de Preço



## Descrição do Problema de Negócio

Sabemos que ao aumentar o preço de um produto a demanda tende a cair. Ainda assim, há alguns casos de produtos que ao aumentar o preço a demanda continua aumentando, maximizando o lucro. Partindo deste princípio, o objetivo deste projeto é entender o quanto vale a pena aumentar o preço de um produto sem que a demanda diminua de forma a reduzir os lucros, mas sim de aumentá-los. Ou então, o quanto vale a pena diminuir o preço de um produto para que a demanda aumente de forma significativa, assim aumentando também os lucros. Este fenômeno é chamado de **elasticidade de preço**.

## A Elasticidade de Preço

**1. Cálculo da elasticidade de preço:**
- O que o cálculo da elasticidade de preço indica: sensibilidade da demanda em relação à variação dos preços.
- Processo do cálculo: a elasticidade de preço é calculada através de uma regressão linear, onde a variável dependente X é o preço e a variável independente Y é a demanda. A reta da regressão que melhor se ajusta aos dados observados é obtida via método dos mínimos quadrados, o qual busca minimizar a soma dos quadrados dos erros entre os valores previstos e os valores reais.
- Equação da elasticidade de preço: (variação percentual na quantidade demandada) / (variação percentual no preço)


**2. Tipos de elasticidade de preço:**
- Elástica: maior que 1. Demanda muito sensível as mudanças de preço. Exemplo: se o preço de um produto aumentar em 10% e a quantidade demandada diminuir em mais de 60%, isso indica que a demanda é elástica.
- Inelástica: menor que 1. Demanda pouco sensível as mudanças de preço. Exemplo: se o preço de um produto aumentar em 10% e a quantidade demandada diminuir em menos de 1,5%, isso indica que a demanda é inelástica.
- Unitária: igual a 1. Demanda e preço sensíveis proporcionalmente.


**3. Interpretação do uso dos tipos de demanda:**
- Produtos com elasticidade alta são bons candidatos a redução de valor, premeditando um aumento na demanda.
- Produtos com elasticidade abaixo de 1 são bons candidatos a aumento de preço, pois impactam pouco na demanda.


**4. Elasticidade de preço cruzada:**
- A elasticidade cruzada identifica quanto que a variação de preço de um produto impacta na variação da demanda de outro produto ou vice-versa. Exemplo: ao aumentar em 5% o preço do produto A, a demanda do produto B reduz em 10%.
- Elasticidade de preço cruzada positiva: ocorre quando a quantidade demandada de um produto aumenta em resposta a um aumento no preço de um produto relacionado. Indica que os dois produtos são substitutos, e um aumento no preço de um produto leva os consumidores a buscar o produto alternativo, aumentando sua demanda.
- Elasticidade de preço cruzada negativa: ocorre quando a quantidade demandada de um produto diminui em resposta a um aumento no preço de um produto relacionado. Indica que os dois produtos são complementares, e um aumento no preço de um produto reduz a demanda pelo outro produto.
- Elasticidade de preço cruzada nula (ou próxima de zero): ocorre quando não há uma relação significativa entre a variação no preço de um produto e a quantidade demandada do outro produto. Indica que não há substitutos ou complementares próximos entre os dois produtos.

## O Conjunto de Dados

Foi escolhido um conjunto de dados que contém registros das compras ocorridas entre janeiro de 2020 e abril de 2020, em grandes lojas online, com categorias de produtos variados. Cada linha no arquivo representa um evento. Todos os eventos estão relacionados a produtos e usuários. Cada evento é como uma relação muitos-para-muitos entre produtos e usuários. Dados coletados pelo projeto Open CDP.

- Kaggle: https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store
- Open CDP: https://rees46.com/en/open-cdp

## Formato da Entrega

**1.** Aplicação Web onde os stakeholders podem escolher os aumentos e as diminuições percentuais nos preços e verificar as alterações geradas no faturamento de maneira interativa. Além disso, contém as tabelas resultantes dos cálculos da elasticidade de preço e da elasticidade de preço cruzada. Link da aplicação: https://elasticidadepreco-9yu7o6hwyjvedjgeanojfw.streamlit.app/.

**2.** Dashboard no Power BI contendo uma análise exploratória completa dos dados escolhidos no projeto, respondendo as seguintes perguntas:
- Quais os meses, quais as semanas e quais os dias da semana que vendem mais?
- Quais produtos possuem o maior preço médio?
- Quais produtos possuem a maior quantidade demandada?
- Qual é a quantidade demandada de produtos por semana?
- Qual é o preço médio dos produtos por semana?

**3.** Notebooks contendo a limpeza dos dados e o Modelo de Machine Learning treinado.

## Planejamento da Solução

Passo a passo resumido do projeto:
- 1. Coleta dos dados a partir da fonte escolhida.
- 2. Limpeza e seleção dos dados originais utilizando Python (Pandas/SQL).
- 3. Determinação das premissas para a escolha dos produtos a serem analisados no projeto.
- 4. Análise exploratória dos dados via Python e Power BI para retirada de insights.
- 5. Preparação dos dados para modelagem.
- 6. Modelagem dos dados: elasticidade de preço.
- 7. Modelagem dos dados: elasticidade de preço cruzada.
- 8. Orientação a objeto.
- 9. Criação da aplicação web.

## Premissas

- Os únicos atributos considerados na análise foram preço, demanda e datas. Não foram considerados fatores externos, tais como renda dos consumidores, e nem fatores externos, tais como crises econômicas.
- Foi determinada uma categoria e uma marca da categoria escolhida para o projeto, em que tanto a categoria quanto a marca encontravam-se entre as top 5 mais vendidas. Deste modo, a amostragem dos dados é maior, proporcionando uma aplicação prática mais significativa.
- Para uma maior relevância prática da análise, foram considerados apenas produtos que possuíssem, no mínimo, 3 variações no preço durante o período de 01 de janeiro de 2020 a 30 de abril de 2020.

## Coleta e Limpeza dos Dados

As etapas de coleta e de limpeza dos dados encontram-se detalhadas no arquivo 'data_cleaning.ipynb'. A estratégia utilizada foi selecionar apenas as colunas de interesse, as quais eram: data da compra, código do produto, categoria do produto, marca do produto e valor da compra. Quanto as linhas, foram selecionadas apenas as que caracterizavam compras (visto que as visualizações não eram necessárias), reduzindo o tamanho do conjunto de dados em mais de 90% (de quase 10GB para, em média, 60MB). Também foram removidas as linhas que continham algum dado faltante, para não comprometer os resultados da análise. Após finalizada a limpeza, foram concatenados os conjuntos dos meses de janeiro a abril, formando um único dataframe completo e pronto para a etapa de análise exploratória e de modelagem.

## Determinação dos Produtos Escolhidos para o Projeto

Os produtos escolhidos para o projeto seguiram as premissas citadas anteriormente. Para a escolha, foram buscadas as 5 categorias mais vendidas (para que houvessem mais dados disponíveis para o treino) e escolhida uma que continha um preço médio significativo. Partindo deste ponto, foi escolhida a categoria **headphone**. Após escolhida a categoria, foi escolhida a marca desta categoria que possuísse mais produtos vendidos: **Acer**.

## Principais conclusões da Análise Exploratória dos Dados

- Existem 79 produtos que apresentam ao menos uma variação no seu preço durante o período analisado e 62 produtos que apresentam ao menos duas variações no seu preço durante o período analisado.
- O mês que mais vendeu headphones foi abril. Em compensação, o mês que menos vendeu foi janeiro, bem distante dos demais em relação às vendas.
- O dia do mês que mais vendeu headphones no período analisado foi o dia 12 (com mais de 900 mil dólares acumulados em vendas), seguido pelo dia 16 (com mais de 800 mil dólares em vendas). Em compensação, o dia que menos vendeu foi o dia 20, com pouco mais de 300 mil dólares em vendas.
- O dia da semana que mais vendeu foi quarta-feira, com valor acumulado no período de US$ 3,2 mi. Em contrapartida, dia da semana que menos vende é terça, com valor acumulado no período de US$ 2,6 mi.
- A semana que mais vendeu headphones durante o período analisado foi a semana 14, seguida pelas semanas 7 e 13, respectivamente. Enquanto isso, a semana que menos vendeu foi a primeira.

## Estratégia de Preparação dos Dados

1. Criação de coluna de demanda de compras por semana através da contagem dos produtos.
2. Criação de coluna de preço médio por semana através da média dos preços dos produtos.
3. Transposição da tabela original, onde os códigos dos produtos viraram colunas e as linhas foram preenchidas pelos preços médios dos produtos por semana (x_price).
4. Transposição da tabela original, onde os códigos dos produtos viraram colunas e as linhas foram preenchidas pelas demandas dos produtos por semana (y_demand).
5. Preenchimento dos valores nulos da tabela 'x_price' através mediana dos preços, a fim de gerar um menor impacto no valor médio e na etapa da modelagem de Machine Learning.
6. Preenchimento dos valores nulos da tabela 'y_demand' com 0, visto que estes valores nulos indicam que naquela semana não houve nenhuma compra.

## Resultados do Modelo

Os resultados do modelo podem ser visualizados no notebook 'elasticidade_preco.ipynb' e na aplicação web, onde são exibidas uma tabela contendo as elasticidades e outra contendo as elasticidades cruzadas. O produto que apresentou a maior elasticidade de preço absoluta foi o de código 1304849, com uma elasticidade de 128.41, mostrando uma grande sensilidade na demanda a partir da variação do seu preço, sendo um bom candidato para redução de preço. Enquanto isso, o produto de código 1307310 foi o que apresentou a menor elasticidade absoluta (2.93), mostrando baixa sensibilidade na demanda a partir da variação do seu preço, sendo um bom candidato para aumento de preço.

## Resultados de Negócio

Os resultados de negócio comprovam as hipóteses do resultado do modelo, visto que, simulando uma redução percentual de 10% no preço o produto mais impactado é justamente o de código 1304849, o qual demonstra um aumento percentual acumulado no faturamento para o período de 4 meses de 1055.77%, saltando de US$ 45,709.30 para US$ 528,294.08, uma variação absoluta de US$ 482,584.78.

Considerando um aumento percentual de 10% nos preços o produto mais impactado é o de código 1307310, apresentando um aumento percentual acumulado no faturamento durante o período analisado de 274.74%, saltando de US$ 723,973.64 para US$ 2,713,008.30, uma variação absoluta de US$ 1,989,034.66.

Demais testes e variações percentuais podem ser testadas pelos stakeholders por meio da aplicação web desenvolvida. 


