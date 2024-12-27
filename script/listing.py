from tabnanny import check

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

def listing_data():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    # data = df.groupby('research type - final')['ID'].apply(list).sort_index() # research type
    # data = df.groupby('used/proposed tool')['ID'].apply(list).sort_index()  # tool
    # data = df.groupby('proposed dataset')['ID'].apply(list).sort_index()  # proposed dataset
    # data = df.groupby('topic')['ID'].apply(list).sort_index() # topic
    # data = df.groupby('test objective')['ID'].apply(list).sort_index() # test objective
    data = df.groupby('test level')['ID'].apply(list).sort_index() # test level

    for study, ids in data.items():
        sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Assumes IDs are in the format PS<number>
        print(f"{study}: {', '.join(sorted_ids)}; total: {len(sorted_ids)}")

def listing_data_grouped():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")

    # data = df.groupby('test objective')['ID'].apply(list).sort_index() # test objective
    data = df.groupby('test level')['ID'].apply(list).sort_index()  # test level

    category = {}
    for studies, ids in data.items():
        # study = studies.split(", ")
        for study in studies.split(", "):
            if study not in category:
                category[study] = []
            category[study].extend(ids)
    for study, ids in category.items():
        category[study] = sorted(ids, key=lambda x: int(x[2:]))
    for study, ids in sorted(category.items()):
        print(f"{study}: {', '.join(ids)}; total: {len(ids)}")

# listing_data()
listing_data_grouped()