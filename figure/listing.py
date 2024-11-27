import pandas as pd


def listing_venue():
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    grouped_venues = df.groupby(['venue', 'venue type', 'venue topic']).size().reset_index(name='Count')
    grouped_venues = grouped_venues.sort_values(by='Count', ascending=False)

    no = 1
    for index, row in grouped_venues.iterrows():
        venue = row['venue']
        venue_type = row['venue type']
        venue_domain = row['venue topic']
        count = row['Count']
        print(f"{no} & {venue} & {venue_type} & {venue_domain} & {count} \\\\")
        no += 1

def listing_research_type():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    research_type_counts = df['research type - final'].value_counts()
    for research_type, count in research_type_counts.items():
        print(f"{research_type}: {count}")

def listing_tool():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    research_type_counts = df['used/proposed tool'].value_counts()
    for research_type, count in research_type_counts.items():
        print(f"{research_type}: {count}")

def listing_dataset():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    research_type_counts = df['proposed dataset'].value_counts()
    for research_type, count in research_type_counts.items():
        print(f"{research_type}: {count}")


# listing_venue()
# listing_research_type()
listing_tool()
# listing_dataset()