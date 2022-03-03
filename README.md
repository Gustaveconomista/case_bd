#  Eleição Brasileira de 2018: Quantidade e Proporção de votos para os candidatos a PR no 2º turno por Unidade da Federação

## Objetivo Geral
Analisar a distribuição de votos em cada um dos dois candidatos a presidência da república no 2º turno das eleições de 2018 por UF, de modo a identificar o perfil eleitoral estadual na época, e visualizar quais foram os estados determinantes para o resultado geral.

## Base de dados
Foram utilizados dados do resultado eleitoral a nível de partido para os municípios brasileiros, tirados do site [Basedosdados](https://basedosdados.org/dataset/br-tse-eleicoes).

# Roteiro

## Importação e Manipulação dos dados
Para esta primeira etapa foram utilizados os comandos dos seguintes pacotes:
* `basedosdados`(Importe);
* `pandas`(Manipulação)

## Visualização dos dados
Nesta parte foram utilizados os pacotes:
* `matplotlib.pyplot`(Geração de gráficos);
* `seaborn`(Adição de paletas de cores e outros acessórios gráficos)
E abaixo seguem os gráficos gerados:
![mapa_ufs](img/map_uf.png)

![grafico_partido](img/graf_partido.png)

## Adicional
Adicionalmente, é possível encontrar os gráficos gerados em modo imagem na subpasta "image".
