import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import DescrStatsW

# Load data
file_path = "/content/drive/MyDrive/ghp_analysis/gesundheitskompetenz_final_GHP16_PAM_levels.xlsx"
df = pd.read_excel(file_path)

# Define the GHP-16 score and weights
score_col = "GHP16_total_rescal"
weight_col = "Gewicht"

# Define variables for comparison
variables = [
    "GenderM0F1", "AgeGroup", "GEO", "Education", "CitizenshipITXX", "Language",
    "Lives_Alone_binary", "Workinthehealthorsocialsector", "Health_Status_groups",
    "HLS_score_cat4", "PAM_level_cat", "chronic_sum", "has_chronic_disease"
]

# Helper function to calculate weighted median
def weighted_median(data, weights):
    data, weights = np.array(data), np.array(weights)
    sorter = np.argsort(data)
    data_sorted, weights_sorted = data[sorter], weights[sorter]
    cumsum = np.cumsum(weights_sorted)
    cutoff = weights_sorted.sum() / 2.0
    return data_sorted[np.where(cumsum >= cutoff)[0][0]]

# Prepare result list
results = []

for var in variables:
    group_data = df[[var, score_col, weight_col]].dropna()
    grouped = group_data.groupby(var)

    for group_name, group in grouped:
        desc = DescrStatsW(group[score_col], weights=group[weight_col], ddof=0)
        median = weighted_median(group[score_col], group[weight_col])
        results.append({
            "Variable": var,
            "Group": group_name,
            "Weighted N": round(group[weight_col].sum(), 1),
            "Median": round(median, 2),
            "Mean": round(desc.mean, 2),
            "95% CI Lower": round(desc.tconfint_mean()[0], 2),
            "95% CI Upper": round(desc.tconfint_mean()[1], 2)
        })

    # Kruskal-Wallis Test for p-value
    groups = [g[score_col].values for _, g in grouped]
    weights = [g[weight_col].values for _, g in grouped]

    # Expand the data to apply Kruskal-Wallis with weights (repeated rows)
    expanded = [np.repeat(g, w.astype(int)) for g, w in zip(groups, weights)]
    try:
        _, p_value = stats.kruskal(*expanded)
    except:
        p_value = np.nan

    results.append({
        "Variable": var,
        "Group": "p-value",
        "Weighted N": "",
        "Median": "",
        "Mean": "",
        "95% CI Lower": "",
        "95% CI Upper": round(p_value, 4)
    })

# Convert to DataFrame
results_df = pd.DataFrame(results)

# Export to Excel
export_path = "/content/drive/MyDrive/ghp_analysis/table1_ghp16_summary_stats.xlsx"
results_df.to_excel(export_path, index=False)
