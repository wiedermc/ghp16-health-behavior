
import pandas as pd
import statsmodels.api as sm

# Load data
df = pd.read_excel("gesundheitskompetenz_final_GHP16_PAM_levels_with_GHP16_total.xlsx")

# Calculate GHP-16 total score and education category
ghp16_columns = [col for col in df.columns if col.startswith("GHP16_item_")]
df["GHP16_total"] = df[ghp16_columns].sum(axis=1)
df["Education_cat"] = df["Education"].astype("category")

# Define covariates
covariates = [
    "GHP16_total", "Mistrust_Index", "HBCWatchWeight5", "HLS_score_cat", "PAM_level_cat",
    "GenderM0F1", "AgeYears", "Education_cat", "Language", "Lives_Alone_binary",
    "Workinthehealthorsocialsector"
]

# Drop missing
regression_df = df[covariates].dropna()

# Convert categorical variables
regression_df["Education_cat"] = regression_df["Education_cat"].astype("category")
regression_df["Language"] = regression_df["Language"].astype("category")
regression_df["HLS_score_cat"] = regression_df["HLS_score_cat"].astype("category")
regression_df["PAM_level_cat"] = regression_df["PAM_level_cat"].astype("category")
regression_df["Workinthehealthorsocialsector"] = regression_df["Workinthehealthorsocialsector"].astype("category")

# Encode categoricals
X = pd.get_dummies(
    regression_df.drop(columns=["GHP16_total", "HBCWatchWeight5"]),
    drop_first=True
)
X = sm.add_constant(X)
y = regression_df["GHP16_total"]
weights = regression_df["HBCWatchWeight5"]

# Run weighted regression
model = sm.WLS(y, X, weights=weights).fit()

# Output
print(model.summary())
