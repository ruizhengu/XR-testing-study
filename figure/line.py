import pandas as pd
import matplotlib.pyplot as plt

file_path = '../primary study.xlsx'  # Update this to your file path
df = pd.read_excel(file_path)

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')  # Convert to numeric, coerce errors to NaN
df = df.dropna(subset=['Year'])

year_counts = df['Year'].value_counts().sort_index()
all_years = pd.DataFrame({'Year': range(2000, 2025)})
year_counts_full = all_years.merge(year_counts, how='left', left_on='Year', right_index=True).fillna(0)
year_counts_full.columns = ['Year', 'Count']

plt.figure(figsize=(10, 6))
plt.plot(year_counts_full['Year'], year_counts_full['Count'], linestyle='-', color='tab:brown')

for i, row in year_counts_full.iterrows():
    if int(row['Count']) > 0:
        plt.text(row['Year'], row['Count'], str(int(row['Count'])), ha='center', va='center',
                 bbox=dict(facecolor='xkcd:sky blue', edgecolor='none', boxstyle='square,pad=0.4'))

plt.xticks(range(2000, 2025))
plt.xlabel('Year')
plt.ylabel('Number of Primary Studies')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
