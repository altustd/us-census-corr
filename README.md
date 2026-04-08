# us-census-corr

**Data mining project** that uses the US Census Bureau ACS 5-Year API to explore correlations among key socioeconomic variables (median income, poverty rate, education attainment, unemployment, housing costs) at the **county level** across the entire United States.

### 📊 Live Interactive Report

**[View the Full Correlation Analysis →](https://altustd.github.io/us-census-corr/census-correlation-analysis.html)**

- Correlation heatmap  
- Pairwise scatter plots  
- Summary statistics  
- All generated from real 2022 ACS data

### Quick Start (for developers)

1. Get a free Census API key → [api.census.gov](https://api.census.gov/data/key_signup.html)
2. `cp .env.example .env` and add your key
3. `pip install -r requirements.txt`
4. `python scripts/fetch_census_data.py`
5. `quarto render`

Repo: https://github.com/altustd/us-census-corr
