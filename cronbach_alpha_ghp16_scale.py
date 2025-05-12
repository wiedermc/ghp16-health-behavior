
import pandas as pd

# Load the dataset
file_path = "gesundheitskompetenz_final_GHP16_PAM_levels_with_GHP16_total.xlsx"
df = pd.read_excel(file_path)

# Define GHP-16 item columns by matching their names
ghp16_items = [col for col in df.columns if col.startswith("GHP16_item_") and df[col].dropna().apply(lambda x: isinstance(x, (int, float))).all()]

# Drop rows with missing values
df_ghp16 = df[ghp16_items].dropna()

# Calculate Cronbach's alpha manually
item_variances = df_ghp16.var(axis=0, ddof=1)
total_score = df_ghp16.sum(axis=1)
total_variance = total_score.var(ddof=1)
n_items = len(ghp16_items)

cronbach_alpha = (n_items / (n_items - 1)) * (1 - item_variances.sum() / total_variance)

print(f"Cronbach's alpha for the GHP-16 scale: {cronbach_alpha:.3f}")
