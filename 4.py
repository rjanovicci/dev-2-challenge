import json

with open("4.json") as file:
    faturamento = json.load(file)

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    print(f"{estado}: {valor / total:.2%}")
