from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib.ticker import MaxNLocator


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

def publication_year():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    df['year'] = pd.to_numeric(df['year'], errors='coerce')  # Convert to numeric, coerce errors to NaN

    df = df.dropna(subset=['year'])
    year_counts = df['year'].value_counts().sort_index()
    sorted_year_counts = year_counts.sort_index()

    plt.figure(figsize=(10, 6))
    plt.bar(sorted_year_counts.index, sorted_year_counts.values, color=colors["cadetblue"])

    for year, count in sorted_year_counts.items():
        plt.text(year, count, str(count), ha='center', va='bottom', fontsize=12)

    all_years = range(2000, 2025)
    plt.xticks(all_years)

    plt.ylabel('Number of Studies', fontsize=14)
    plt.xticks(rotation=45)
    plt.yticks(fontsize=12)
    plt.tight_layout()

    plt.show()

def venue_type():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    venue_types = ["Journal", "Conference", "Workshop", "Symposium"]
    venue_counts = df["venue type"].value_counts()
    filtered_counts = venue_counts[venue_types].reset_index()
    filtered_counts.columns = ['Venue Type', 'Count']

    plt.figure(figsize=(6, 4))
    plt.bar(filtered_counts['Venue Type'], filtered_counts['Count'], width=0.5, color=colors["cadetblue"])

    for i, count in enumerate(filtered_counts['Count']):
        plt.text(i, count + 0.15, str(count), ha='center', fontsize=10)

    plt.ylabel('Frequency')
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure y-ticks are integers
    plt.tight_layout()
    plt.show()


def venue_domain():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    venue_domains = ["HCI", "XR", "SWE", "CG", "SP", "General", "XR, SP", "XR, SWE"]
    venue_counts = df["venue topic"].value_counts()
    filtered_counts = venue_counts[venue_domains].reset_index()
    filtered_counts.columns = ['Venue Domain', 'Count']

    filtered_counts['Venue Domain'] = filtered_counts['Venue Domain'].replace({
        "XR, SP": "XR+SP",
        "XR, SWE": "XR+SWE"
    })

    plt.figure(figsize=(6, 4))
    plt.bar(filtered_counts['Venue Domain'], filtered_counts['Count'], width=0.5, color=colors["cadetblue"])

    for i, count in enumerate(filtered_counts['Count']):
        plt.text(i, count + 0.15, str(count), ha='center', fontsize=10)

    plt.ylabel('Frequency')
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure y-ticks are integers
    plt.tight_layout()
    plt.show()

def technology():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    technology_type = ["XR", "VR", "AR", "MR", "VR, AR"]
    technology_counts = df["technology"].value_counts()
    filtered_counts = technology_counts[technology_type].reset_index()
    filtered_counts.columns = ['Technology', 'Count']

    filtered_counts['Technology'] = filtered_counts['Technology'].replace({
        "VR, AR": "VR/AR",
    })


    plt.figure(figsize=(6, 4))
    plt.bar(filtered_counts['Technology'], filtered_counts['Count'], width=0.5, color=colors["cadetblue"])

    for i, count in enumerate(filtered_counts['Count']):
        plt.text(i, count + 0.15, str(count), ha='center', fontsize=10)

    plt.ylabel('Frequency')
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Ensure y-ticks are integers
    plt.tight_layout()
    plt.show()

def platform_engine():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    data = df["dataset or tool - platform & engine & SDK"].dropna().str.strip()
    non_empty_count = len(data)
    print(non_empty_count)
    all_items = [item.strip() for cell in data for item in cell.split(',')]
    item_counts = Counter(all_items)
    print(item_counts)


# publication_year()
# venue_type()
# venue_domain()
technology()
# platform_engine()