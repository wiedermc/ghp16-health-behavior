
# GHP-16 Language Group Analysis – South Tyrol Health Behavior Survey

This repository contains the Python script and data structure used to reproduce Figure 3 and Table S3 from the analysis of health-promoting behaviors (GHP-16) in South Tyrol, stratified by language group (German vs. Italian).

## Files Included

- `fig3_tableS3_analysis_script.py` – Python script to generate:
  - Figure 3: GHP-16 item scores by language (weighted, with p-values and Cliff’s delta)
  - Table S3: Linear regression adjusted for sociodemographic and psychosocial covariates
- (Optional) `gesundheitskompetenz_final_GHP16_PAM_levels_with_GHP16_total.xlsx` – Source data file (not included for privacy)

## Analysis Details

- Weighted linear regression using `statsmodels.OLS`
- Covariates include:
  - Age, gender, education, living situation, employment in health/social sector
  - Health literacy (HLS-EU-Q16), patient activation (PAM-10)
  - Language group (Italian vs. German)
- p-values from Mann–Whitney U tests
- Effect sizes via Cliff’s delta with interpretation categories (negligible, small, medium, large)

## Requirements

- Python 3.9+
- pandas, numpy, matplotlib, scipy, statsmodels

Install dependencies via:
```bash
pip install pandas numpy matplotlib scipy statsmodels
```

## How to Run

1. Place the Excel file in the working directory.
2. Run the script in your Python environment or Google Colab.
3. Outputs will include:
   - `Figure3_GHP16_by_Language.png`
   - `Table_S3_Regression_Adjusted_LanguageGroup.xlsx`
   - `Table_S3a_VIF_Adjusted_LanguageGroup.xlsx`

## Citation

This analysis is part of a population-based health behavior study conducted in South Tyrol, 2024–2025. Please cite accordingly.
