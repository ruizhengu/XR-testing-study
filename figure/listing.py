import pandas as pd

def listing_venue():
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    file_path = '../XR_Study.xlsx'  # Update this to your file path
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    grouped_venues = df.groupby(['venue', 'venue type', 'venue topic']).size().reset_index(name='Count')

    # Sort the results by count in descending order
    grouped_venues = grouped_venues.sort_values(by='Count', ascending=False)

    no = 1
    for index, row in grouped_venues.iterrows():
        venue = row['venue']
        venue_type = row['venue type']
        venue_domain = row['venue topic']
        count = row['Count']
        # percentage = row['Count'] / 45
        print(f"{no} & {venue} & {venue_type} & {venue_domain} & {count} \\\\")
        no += 1

listing_venue()