import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

primary_studies_xlsx = '../primary study.xlsx'
df = pd.read_excel(primary_studies_xlsx)


def venue_type_distribution():
    venue_types = ["Journal", "Conference", "Workshop", "Symposium"]
    venue_counts = df["Venue Type"].value_counts()

    filtered_counts = venue_counts[venue_types].reset_index()
    filtered_counts.columns = ['Venue Type', 'Count']

    cmap = plt.get_cmap('Set2')
    colors = cmap(np.linspace(0, 1, len(filtered_counts['Count'])))

    fig, ax = plt.subplots()
    ax.pie(filtered_counts['Count'], labels=filtered_counts['Venue Type'], autopct='%1.1f%%', startangle=90,
           colors=colors)
    ax.axis('equal')

    plt.tight_layout()
    plt.show()


def venue_topic_distribution():
    venue_topics = ["HCI", "XR", "Testing / Engineering", "General"]
    topic_counts = df["Venue Topic"].value_counts()

    filtered_counts = topic_counts[venue_topics].reset_index()
    filtered_counts.columns = ['Venue Topic', 'Count']

    cmap = plt.get_cmap('Set2')
    colors = cmap(np.linspace(0, 1, len(filtered_counts['Count'])))

    fig, ax = plt.subplots()
    ax.pie(filtered_counts['Count'], labels=filtered_counts['Venue Topic'], autopct='%1.1f%%', startangle=90,
           colors=colors)
    ax.axis('equal')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    venue_topic_distribution()
