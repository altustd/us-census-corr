# us-census-corr

**Data mining project** that uses the US Census Bureau ACS 5-Year API to explore correlations among socioeconomic variables (median income, poverty, education, unemployment, housing costs) at the **county level** across the United States.

### Quick start
1. Get free Census API key → https://api.census.gov/data/key_signup.html
2. `cp .env.example .env` and add your key
3. `python scripts/fetch_census_data.py`
4. `quarto render`

Repo: https://github.com/altustd/us-census-corr
