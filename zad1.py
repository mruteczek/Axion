import os
import pandas as pd
import kagglehub


# Pobierz ścieżkę do folderu z zestawem danych
path = kagglehub.dataset_download("larsen0966/student-performance-data-set")
print("Ścieżka do folderu z danymi:", path)

# Połącz ścieżkę folderu z nazwą pliku CSV
file_path = os.path.join(path, "student-por.csv")



# Wczytaj dane do pandasa 
df = pd.read_csv(file_path, sep=",")

# Wyświetla nazwy kolumn
print(df.columns.tolist())

orelacja_matka = df['Medu'].corr(df['G3'])
korelacja_ojciec = df['Fedu'].corr(df['G3'])

print(f"Korelacja Pearsona - matka: {orelacja_matka:.3f}")
print(f"Korelacja Pearsona - ojciec: {korelacja_ojciec:.3f}")