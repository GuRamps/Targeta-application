# 4. Cálculo do percentual de faturamento por estado
# Faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Valor total do faturamento
total_faturamento = sum(faturamento_estados.values())

# Cálculo do percentual de cada estado
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}

# Exibição dos resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
