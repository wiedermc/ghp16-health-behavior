
import pandas as pd

# Load the dataset
file_path = "gesundheitskompetenz_final_GHP16_PAM_levels_with_GHP16_total.xlsx"
df = pd.read_excel(file_path)

# Define the columns corresponding to the Mistrust Index
mistrust_items = ["YourGP", "PrivatePublicSpecialists", "Pharmacist", "Nurses"]

# Drop rows with missing values
df_mistrust = df[mistrust_items].dropna()

# Calculate Cronbach's alpha manually
item_variances = df_mistrust.var(axis=0, ddof=1)
total_score = df_mistrust.sum(axis=1)
total_variance = total_score.var(ddof=1)
n_items = len(mistrust_items)

cronbach_alpha = (n_items / (n_items - 1)) * (1 - item_variances.sum() / total_variance)

print(f"Cronbach's alpha for the Mistrust Index: {cronbach_alpha:.3f}")
