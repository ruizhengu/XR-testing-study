import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

primary_studies_xlsx = '../primary study.xlsx'
df = pd.read_excel(primary_studies_xlsx)

venue_types = ["Journal", "Conference", "Workshop", "Symposium"]

venue_counts = df["Venue Type"].value_counts()

filtered_counts = venue_counts[venue_types].reset_index()
filtered_counts.columns = ['Venue Type', 'Count']

num_slices = len(filtered_counts['Count'])

# Extract colors from the colormap
cmap = plt.get_cmap('Set2')
colors = cmap(np.linspace(0, 1, len(filtered_counts['Count'])))

fig, ax = plt.subplots()
ax.pie(filtered_counts['Count'], labels=filtered_counts['Venue Type'], autopct='%1.1f%%', startangle=90,
       colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.show()
