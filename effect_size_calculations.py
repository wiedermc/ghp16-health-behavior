
import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu, kruskal

def rank_biserial_effect_size(x1, x2):
    """
    Calculate rank biserial correlation for two independent samples.
    """
    u_stat, _ = mannwhitneyu(x1, x2, alternative='two-sided')
    n1 = len(x1)
    n2 = len(x2)
    r_rb = 1 - (2 * u_stat) / (n1 * n2)
    return r_rb

def epsilon_squared(groups):
    """
    Calculate epsilon squared effect size for Kruskal-Wallis H-test.
    """
    k_stat, _ = kruskal(*groups)
    n_total = sum([len(g) for g in groups])
    epsilon_sq = (k_stat - len(groups) + 1) / (n_total - len(groups))
    return epsilon_sq

# Example usage:
# For two groups:
# rrb = rank_biserial_effect_size(group1, group2)

# For multiple groups:
# epsilon2 = epsilon_squared([group1, group2, group3])
