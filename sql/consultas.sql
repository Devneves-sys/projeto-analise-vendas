-- Projeto: Análise de Vendas
-- Banco sugerido: PostgreSQL / MySQL / SQL Server
-- Tabela: vendas

-- 1. Faturamento total
SELECT
    SUM(valor_total) AS faturamento_total
FROM vendas;

-- 2. Quantidade total vendida
SELECT
    SUM(quantidade) AS quantidade_vendida
FROM vendas;

-- 3. Ticket médio
SELECT
    AVG(valor_total) AS ticket_medio
FROM vendas;

-- 4. Faturamento por categoria
SELECT
    categoria,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY categoria
ORDER BY faturamento DESC;

-- 5. Top 10 produtos por quantidade vendida
SELECT
    produto,
    SUM(quantidade) AS quantidade_vendida
FROM vendas
GROUP BY produto
ORDER BY quantidade_vendida DESC
LIMIT 10;

-- 6. Faturamento por região
SELECT
    regiao,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY regiao
ORDER BY faturamento DESC;

-- 7. Faturamento por canal
SELECT
    canal,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY canal
ORDER BY faturamento DESC;

-- 8. Faturamento por forma de pagamento
SELECT
    forma_pagamento,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY forma_pagamento
ORDER BY faturamento DESC;

-- 9. Vendas mensais
-- PostgreSQL:
SELECT
    DATE_TRUNC('month', data) AS mes,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY DATE_TRUNC('month', data)
ORDER BY mes;

-- 10. Clientes com maior faturamento
SELECT
    cliente,
    SUM(valor_total) AS faturamento
FROM vendas
GROUP BY cliente
ORDER BY faturamento DESC
LIMIT 10;