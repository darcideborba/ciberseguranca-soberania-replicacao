"""Recalcula os totais do Quadro 3 a partir de data/matriz_codificacao.csv."""
import csv
from pathlib import Path
rows = list(csv.DictReader(open(Path(__file__).parents[1] / "data" / "matriz_codificacao.csv", encoding="utf-8")))
print(f"Instrumentos codificados: {len(rows)}")
for d in "GKITPECX":
    print(f"{d}: {sum(r[d] != '0' for r in rows)} (explícita: {sum(r[d] == '2' for r in rows)})")
s = [r["S"] for r in rows]
print(f"Soberania (qualquer): {sum(x != '0' for x in s)}; declarada: {sum('D' in x for x in s)}; instrumentada: {sum('I' in x for x in s)}")
