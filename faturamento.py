# 3. Análise de faturamento diário de uma distribuidora
import json

# Dados de faturamento (JSON)
faturamento_json = '''
{
    "dias": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 26742.6612},
        {"dia": 7, "valor": 0.0},
        {"dia": 8, "valor": 42931.033},
        {"dia": 9, "valor": 0.0},
        {"dia": 10, "valor": 11191.4722}
    ]
}
'''

# Parse JSON
faturamento = json.loads(faturamento_json)
valores = [dia["valor"] for dia in faturamento["dias"] if dia["valor"] > 0]

# Menor e maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Média mensal de faturamento (ignorando dias sem faturamento)
media_mensal = sum(valores) / len(valores)

# Dias com faturamento acima da média
dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

# Resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
