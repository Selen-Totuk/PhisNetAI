import pandas as pd

df = pd.read_csv("epostalar.csv")
X = df["icerik"]
y = df["etiket"]

# Buradan devamla mevcut eğitim kodunu uygula
