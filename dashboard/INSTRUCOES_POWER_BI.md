# Dashboard Power BI

Crie um arquivo chamado `dashboard.pbix` e importe:

`data/vendas.csv`

## Medidas DAX sugeridas

### Faturamento
```DAX
Faturamento = SUM(vendas[valor_total])
```

### Quantidade Vendida
```DAX
Quantidade Vendida = SUM(vendas[quantidade])
```

### Número de Vendas
```DAX
Número de Vendas = DISTINCTCOUNT(vendas[id_venda])
```

### Ticket Médio
```DAX
Ticket Médio = DIVIDE([Faturamento], [Número de Vendas])
```

## Visuais

1. Cartão — Faturamento
2. Cartão — Número de Vendas
3. Cartão — Quantidade Vendida
4. Cartão — Ticket Médio
5. Gráfico de linha — Faturamento por mês
6. Gráfico de barras — Faturamento por categoria
7. Gráfico de barras — Top 10 produtos
8. Gráfico de barras — Faturamento por região
9. Gráfico de rosca — Participação por canal
10. Gráfico de colunas — Faturamento por forma de pagamento

## Segmentações

- Data
- Região
- Estado
- Categoria
- Produto
- Canal
- Forma de pagamento