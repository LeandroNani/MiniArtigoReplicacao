# Códigos da Replicação Científica

Este diretório apresenta os códigos utilizados para o desenvolvimento do artigo de replicação e os dados brutos e finais.

## Artigo-base da replicação e análise replicada

O artigo [Characterising Volunteers' Task Execution Patterns Across Projects on Multi-Project Citizen Science Platforms](https://doi.org/10.48550/arXiv.1908.01344)  investiga a dinâmica de contribuições em plataformas online de ciência cidadã. Uma de suas principais constatações, evidenciada na Tabela 3, é a existência de uma disparidade significativa na distribuição de voluntários entre os projetos, com poucos projetos concentrando a maior parte dos colaboradores.

O objetivo desta replicação é verificar se essa tendência também se manifesta no contexto do desenvolvimento de software open source, utilizando como objeto de estudo o repositório do Visual Studio Code (VSCode). Em outras palavras, buscamos responder à seguinte pergunta: no repositório do VSCode, a contribuição se concentra em um pequeno grupo de desenvolvedores, ou se existe uma participação mais distribuída entre os colaboradores?

## Fases da replicação e códigos associados

1. Coletar dados de cada commit feito no repositório. Código [``getCommits.py``](getCommits.py);
1. Para cada programador, calcular a quantidade de dias em que fez pelo menos um commit no repositório. Código [``getDays.py``](getDays.py)
1. Gerar o gráfico com mesma lógica (eixos X e Y) do artigo-base. Código[``graphActivity``](graphActivity.R)


## Dados usados coletados e gerados na replicação

Os dados brutos coletados por meio da API ao rodar o código são salvos em um arquivo chamado  [``data.json``] não foi possível colocar o arquivo no repositório pois ele ultrapassava o tamanho permitido pelo github. A coleta dos dados foi feita em 05/10/2024. Os dados finais, totalmente processados e prontos para serem exibidos no gráfico, estão no arquivo [``activity.data``](activity.data).

---
_Leandro Pacheco (leandropacheco02@hotmail.com)_
_Lucas Maia (lmaiarocha23@gmail.com)_
_Otto Esteves (ottoesteves105@gmail.com)_
