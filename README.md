
# Elasticidade de Preço



## Descrição do Problema de Negócio

Sabemos que ao aumentar o preço de um produto a demanda tende a cair. Ainda assim, há alguns casos de produtos que ao aumentar o preço a demanda continua aumentando, maximizando o lucro. Partindo deste princípio, o objetivo deste projeto é entender o quanto vale a pena aumentar o preço de um produto sem que a demanda diminua de forma a reduzir os lucros, mas sim de aumentá-los. Ou então, o quanto vale a pena diminuir o preço de um produto para que a demanda aumente de forma significativa, assim aumentando também os lucros. Este fenômeno é chamado de **elasticidade de preço**.
## A Elasticidade de Preço

**1. Cálculo da elasticidade de preço:**
- O que o cálculo da elasticidade de preço indica: sensibilidade da demanda em relação à variação dos preços.
- Processo do cálculo: a elasticidade de preço é calculada através de uma regressão linear, onde a variável dependente X é o preço e a variável independente Y é a demanda. A reta da regressão que melhor se ajusta aos dados observados é obtida via método dos mínimos quadrados, o qual busca minimizar a soma dos quadrados dos erros entre os valores previstos e os valores reais.
- Equação da elasticidade de preço: variação percentual na quantidade demandada) / (variação percentual no preço)


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

**1.** Aplicação Web onde os stakeholders podem escolher os aumentos e as diminuições percentuais nos preços e verificar as alterações geradas no faturamento de maneira interativa.

**2.** Dashboard no Power BI contendo uma análise exploratória completa dos dados escolhidos no projeto, respondendo as seguintes perguntas:
- Quais os meses, quais as semanas e quais os dias da semana que vendem mais?
- Quais produtos possuem o maior preço médio?
- Quais produtos possuem a maior quantidade demandada?
- Qual é a quantidade demandada de produtos por semana?
- Qual é o preço médio dos produtos por semana?

**3.** Arquivos .csv contendo:
- Conjunto de dados completo e limpo, com todos os eventos de compra, todas as categorias e todas as marcas.
- Resultados dos cálculos de elasticidade de preço.
- Resultados dos cálculos de elasticidade de preço cruzada.

**4.** Modelo de Machine Learning treinado.
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

