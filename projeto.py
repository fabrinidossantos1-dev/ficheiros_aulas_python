import matplotlib.pyplot as plt

# Dados de exemplo
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [1200, 1500, 1350, 1800, 2100, 1950]

# Criar o gráfico de linhas
plt.figure(figsize=(8, 4))
plt.plot(meses, vendas, marker="o", linestyle="-", color="b", label="Vendas (€)")

# Títulos e rótulos
plt.title("Evolução Mensal das Vendas")
plt.xlabel("Mês")
plt.ylabel("Valor (€)")
plt.grid(True)
plt.legend()

# Guardar e exibir o gráfico
plt.tight_layout()
plt.savefig("grafico_vendas.png", dpi=150)
plt.show()
