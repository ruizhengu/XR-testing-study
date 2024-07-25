import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the Excel file
file_path = '../primary study.xlsx'  # Update this to your file path
df = pd.read_excel(file_path)

# Step 2: Ensure the 'Year' column is treated as integer
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')  # Convert to numeric, coerce errors to NaN

# Step 3: Drop rows with NaN values in 'Year' column
df = df.dropna(subset=['Year'])

# Step 4: Count occurrences of each year
year_counts = df['Year'].value_counts()

# Step 5: Sort by year
sorted_year_counts = year_counts.sort_index()

# Step 6: Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_year_counts.index, sorted_year_counts.values, color='tab:brown')

all_years = range(2000, 2025)
plt.xticks(all_years)  # Set x-axis ticks

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Items by Year')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit everything nicely

# Step 7: Show the plot
plt.show()
