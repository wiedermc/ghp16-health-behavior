
# Script to calculate weighted median GHP-16 scores by mistrust index and plot Figure 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def weighted_median(data, weights):
    sorted_data, sorted_weights = zip(*sorted(zip(data, weights)))
    cum_weights = np.cumsum(sorted_weights)
    cutoff = sum(sorted_weights) / 2.0
    return sorted_data[np.searchsorted(cum_weights, cutoff)]

def bootstrap_ci(data, weights, n_bootstrap=1000, ci=0.95):
    medians = []
    n = len(data)
    for _ in range(n_bootstrap):
        idx = np.random.choice(range(n), size=n, replace=True)
        sample_data = data[idx]
        sample_weights = weights[idx]
        medians.append(weighted_median(sample_data, sample_weights))
    lower = np.percentile(medians, (1 - ci) / 2 * 100)
    upper = np.percentile(medians, (1 + ci) / 2 * 100)
    return lower, upper

# Load your dataset (change file path if needed)
df = pd.read_excel("gesundheitskompetenz_final_GHP16_PAM_levels.xlsx")
df = df.dropna(subset=["Mistrust_Index", "GHP16_total_rescal", "Gewicht"])

summary_data = []
for i in sorted(df["Mistrust_Index"].dropna().unique()):
    group = df[df["Mistrust_Index"] == i]
    x = group["GHP16_total_rescal"].values
    w = group["Gewicht"].values
    median = weighted_median(x, w)
    ci_lower, ci_upper = bootstrap_ci(np.array(x), np.array(w))
    summary_data.append({"Mistrust_Index": i, "Median": median, "CI_lower": ci_lower, "CI_upper": ci_upper})

summary_df = pd.DataFrame(summary_data)

plt.figure(figsize=(10, 6))
plt.errorbar(
    summary_df["Mistrust_Index"],
    summary_df["Median"],
    yerr=[summary_df["Median"] - summary_df["CI_lower"], summary_df["CI_upper"] - summary_df["Median"]],
    fmt='o',
    ecolor='gray',
    capsize=4,
    marker='o',
    markersize=6,
    color='black'
)
plt.title("Figure 1. Weighted Median GHP-16 Score by Mistrust in Health Professionals")
plt.xlabel("Mistrust Index (range: 4–16)")
plt.ylabel("Weighted Median GHP-16 Score")
plt.xticks(summary_df["Mistrust_Index"])
plt.tight_layout()
plt.savefig("Figure1_GHP16_vs_Mistrust_Weighted.png", dpi=300)
