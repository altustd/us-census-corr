import os
import pandas as pd
from census import Census
from us import states
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('CENSUS_API_KEY')
if not API_KEY or API_KEY == "your_api_key_here":
    raise ValueError("❌ Missing or placeholder Census API key.\n"
                     "   → Open .env and replace 'your_api_key_here' with your real key\n"
                     "   → Get one free at: https://api.census.gov/data/key_signup.html")

c = Census(API_KEY)

variables = {
    'B01003_001E': 'total_population',
    'B19013_001E': 'median_household_income',
    'B17001_002E': 'poverty_count',
    'B23025_005E': 'unemployed_count',
    'B23025_001E': 'labor_force',
    'B15003_022E': 'bachelors_deg',
    'B15003_023E': 'masters_deg',
    'B15003_024E': 'professional_deg',
    'B15003_025E': 'doctorate_deg',
    'B25077_001E': 'median_home_value',
}

data = []
print("🔄 Downloading county-level ACS data (this may take 1–2 minutes)...")

for state in states.STATES:
    try:
        county_data = c.acs5.state_county(
            list(variables.keys()),
            state.fips,
            Census.ALL,
            year=2022
        )
        for item in county_data:
            item['state_name'] = state.name
            data.append(item)
        print(f"✓ {state.name}")
    except Exception as e:
        print(f"✗ {state.name}: {e}")

if len(data) == 0:
    raise ValueError("❌ No data was downloaded. Please check your API key in .env")

df = pd.DataFrame(data)
df = df.rename(columns=variables)

# Derived metrics
df['poverty_rate'] = (df['poverty_count'] / df['total_population']) * 100
df['unemployment_rate'] = (df['unemployed_count'] / df['labor_force']) * 100
df['bachelors_or_higher'] = (
    (df['bachelors_deg'] + df['masters_deg'] + df['professional_deg'] + df['doctorate_deg'])
    / df['total_population'] * 100
)

df.to_csv('data/raw/census_county_data_2022.csv', index=False)
print(f"\n✅ SUCCESS! Data saved! Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print("Ready for Quarto report.")
