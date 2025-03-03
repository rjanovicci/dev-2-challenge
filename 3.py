import json

with open("3.json") as file:
    faturamento = [v for v in json.load(file)["faturamento"] if v > 0]

print(f"Menor: {min(faturamento)}")
print(f"Maior: {max(faturamento)}")
print(f"Dias acima da media: {sum(v > (sum(faturamento) / len(faturamento)) for v in faturamento)}")
