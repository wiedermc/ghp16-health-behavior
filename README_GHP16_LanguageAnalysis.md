# GHP-16 Language Group Analysis – South Tyrol Health Behavior Survey

This repository contains the Python script and data structure used to reproduce **Figure 3** and **Table S3** from the analysis of health-promoting behaviors (GHP-16) in South Tyrol, stratified by language group (German vs. Italian).

## Files Included

- `fig3_tableS3_analysis_script.py`  
  Python script to generate:
  - **Figure 3**: GHP-16 item scores by language (weighted, with p-values and Cliff’s delta)
  - **Table S3**: Weighted linear regression adjusted for sociodemographic and psychosocial covariates

## Analysis Details

- Weighted linear regression using `statsmodels.OLS`
- Covariates:
  - Age
  - Gender
  - Education
  - Living situation
  - Employment in health/social sector
  - Health literacy (HLS-EU-Q16)
  - Patient activation (PAM-10)
  - Language group (Italian vs. German)
- Group comparisons:
  - p-values from Mann–Whitney U tests
  - Effect sizes via **Cliff’s delta** with interpretation thresholds:
    - negligible (|d| < 0.147)
    - small (0.147 ≤ |d| < 0.33)
    - medium (0.33 ≤ |d| < 0.474)
    - large (|d| ≥ 0.474)

## Requirements

- Python 3.9+
- Required packages:
  ```bash
  pip install pandas numpy matplotlib scipy statsmodels
