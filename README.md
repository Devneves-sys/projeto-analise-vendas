# 📊 Análise de Vendas — Data Analytics

Projeto de análise de dados desenvolvido para praticar um fluxo básico de **Data Analytics**, desde a preparação dos dados até a criação de indicadores e dashboards.

## 📊 Dashboard

![Dashboard de Análise de Vendas](images/dashboards.png)

## 🎯 Objetivo

Analisar um conjunto fictício de vendas para identificar:

- faturamento total;
- ticket médio;
- produtos mais vendidos;
- categorias com maior faturamento;
- evolução das vendas ao longo dos meses;
- desempenho por região;
- desempenho por canal de venda;
- principais clientes.

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas**
- **Matplotlib**
- **SQL**
- **Power BI**
- **Git/GitHub**

## 🔄 Pipeline do projeto

```text
Dados brutos
     ↓
CSV
     ↓
Tratamento com Python + Pandas
     ↓
Análise exploratória
     ↓
Consultas SQL
     ↓
Visualizações
     ↓
Dashboard no Power BI
     ↓
Insights
```

## 📁 Estrutura

```text
projeto-analise-vendas/
│
├── data/
│   └── vendas.csv
│
├── python/
│   └── analise_vendas.py
│
├── sql/
│   └── consultas.sql
│
├── dashboard/
│   └── dashboard.pbix
│
├── images/
│   ├── faturamento_mensal.png
│   ├── faturamento_categoria.png
│   └── resumo_kpis.csv
│
├── requirements.txt
└── README.md
```

## 🐍 Python

O script realiza:

1. leitura do CSV;
2. conversão de datas;
3. verificação de valores nulos;
4. verificação de registros duplicados;
5. criação de indicadores;
6. agrupamentos com `groupby`;
7. análise mensal;
8. criação de gráficos;
9. exportação de um resumo dos KPIs.

Para executar:

```bash
pip install -r requirements.txt
python python/analise_vendas.py
```

## 🗄️ SQL

O arquivo `sql/consultas.sql` contém consultas para:

- faturamento;
- quantidade vendida;
- ticket médio;
- ranking de produtos;
- categorias;
- regiões;
- canais;
- formas de pagamento;
- vendas mensais;
- clientes.

## 📈 Power BI

O dashboard foi planejado para apresentar uma visão executiva e simples dos dados.

### KPIs

- Faturamento total
- Número de vendas
- Quantidade vendida
- Ticket médio

### Gráficos

- Faturamento por mês
- Faturamento por categoria
- Top 10 produtos
- Faturamento por região
- Faturamento por canal
- Faturamento por forma de pagamento

### Filtros

- período;
- região;
- estado;
- categoria;
- produto;
- canal;
- forma de pagamento.

## 💡 Principais perguntas de negócio

Este projeto procura responder:

1. Qual foi o faturamento total?
2. Qual mês apresentou o maior faturamento?
3. Qual categoria gerou mais receita?
4. Quais produtos tiveram maior volume de vendas?
5. Qual região teve melhor desempenho?
6. Qual canal de vendas gerou mais receita?
7. Qual é o ticket médio?
8. Quais clientes representam maior faturamento?

## 📌 Observação

Os dados utilizados são **fictícios**, criados exclusivamente para fins de estudo e demonstração de conhecimentos em análise de dados.

## 👨‍💻 Autor

**Mateus Fernandes Neves**

Projeto desenvolvido como parte do portfólio de estudos em tecnologia e dados.