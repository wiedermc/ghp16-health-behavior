
import pandas as pd
import numpy as np
from scipy.stats import kruskal, mannwhitneyu
from statsmodels.stats.weightstats import DescrStatsW

file_path = "gesundheitskompetenz_final_GHP16_PAM_levels.xlsx"
df = pd.read_excel(file_path)

group_vars = ['GenderM0F1', 'AgeGroup', 'GEO', 'Education', 'CitizenshipITXX', 'Language', 'Lives_Alone_binary', 'Workinthehealthorsocialsector', 'Health_Status_groups', 'HLS_score_cat4', 'PAM_level_cat', 'chronic_sum', 'has_chronic_disease']
score_column = "GHP16_total_rescal"
weight_column = "Gewicht"
results = []

for var in group_vars:
    if df[var].isnull().all():
        continue
    grouped = df[[var, score_column, weight_column]].dropna()
    desc_stats = []
    all_groups = []
    for name, group in grouped.groupby(var):
        dsw = DescrStatsW(group[score_column], weights=group[weight_column], ddof=0)
        median = np.median(np.repeat(group[score_column], group[weight_column].round().astype(int)))
        lower = dsw.tconfint_mean()[0]
        upper = dsw.tconfint_mean()[1]
        count = group[weight_column].sum()
        desc_stats.append((name, count, median, lower, upper))
        all_groups.append(group[score_column])
    if len(all_groups) > 2:
        _, p = kruskal(*all_groups)
    elif len(all_groups) == 2:
        _, p = mannwhitneyu(*all_groups)
    else:
        p = np.nan
    for stat in desc_stats:
        results.append({
            "Variable": var,
            "Group": stat[0],
            "Weighted N": round(stat[1], 1),
            "Weighted Median": round(stat[2], 2),
            "95% CI Lower": round(stat[3], 2),
            "95% CI Upper": round(stat[4], 2),
            "P-Value": round(p, 4)
        })
results_df = pd.DataFrame(results)
results_df.to_excel("GHP16_weighted_medians_with_pvalues.xlsx", index=False)
