import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO = BASE_DIR / "data" / "vendas.csv"
OUTPUT = BASE_DIR / "images"
OUTPUT.mkdir(exist_ok=True)

# 1. Carregamento
df = pd.read_csv(ARQUIVO, encoding="utf-8-sig")

# 2. Preparação
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.to_period("M").astype(str)

# 3. Qualidade dos dados
print("=== INFORMAÇÕES DO DATASET ===")
print(df.info())
print("\nValores nulos:")
print(df.isnull().sum())
print("\nDuplicados:", df.duplicated().sum())

# 4. KPIs
faturamento = df["valor_total"].sum()
quantidade_vendida = df["quantidade"].sum()
numero_vendas = df["id_venda"].nunique()
ticket_medio = faturamento / numero_vendas

print("\n=== KPIs ===")
print(f"Faturamento: R$ {faturamento:,.2f}")
print(f"Quantidade vendida: {quantidade_vendida}")
print(f"Número de vendas: {numero_vendas}")
print(f"Ticket médio: R$ {ticket_medio:,.2f}")

# 5. Produto mais vendido por quantidade
produto_mais_vendido = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== TOP 10 PRODUTOS ===")
print(produto_mais_vendido)

# 6. Faturamento por categoria
faturamento_categoria = (
    df.groupby("categoria")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== FATURAMENTO POR CATEGORIA ===")
print(faturamento_categoria)

# 7. Faturamento mensal
faturamento_mensal = (
    df.groupby("mes")["valor_total"]
    .sum()
    .sort_index()
)

# 8. Gráfico mensal
plt.figure(figsize=(10, 5))
faturamento_mensal.plot(marker="o")
plt.title("Faturamento mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT / "faturamento_mensal.png", dpi=150)
plt.close()

# 9. Gráfico por categoria
plt.figure(figsize=(9, 5))
faturamento_categoria.plot(kind="bar")
plt.title("Faturamento por categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT / "faturamento_categoria.png", dpi=150)
plt.close()

# 10. Exportação de um resumo
resumo = pd.DataFrame({
    "indicador": [
        "Faturamento",
        "Quantidade vendida",
        "Número de vendas",
        "Ticket médio"
    ],
    "valor": [
        faturamento,
        quantidade_vendida,
        numero_vendas,
        ticket_medio
    ]
})

resumo.to_csv(OUTPUT / "resumo_kpis.csv", index=False, encoding="utf-8-sig")

print("\nAnálise concluída.")
print(f"Arquivos gerados em: {OUTPUT}")