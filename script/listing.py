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

def listing_topic():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    grouped_data = df.groupby('topic')['ID'].apply(list).sort_index()

    for topic, ids in grouped_data.items():
        sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Assumes IDs are in the format PS<number>
        print(f"{topic}: {', '.join(sorted_ids)}; total: {len(sorted_ids)}")

def listing_objective():
    file_path = '../XR_Study.xlsx'
    df = pd.read_excel(file_path, sheet_name="Data Extraction")
    grouped_data = df.groupby('test objective')['ID'].apply(list).sort_index()

    for objective, ids in grouped_data.items():
        sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Assumes IDs are in the format PS<number>
        print(f"{objective}: {', '.join(sorted_ids)}; total: {len(sorted_ids)}")

    # category = {}
    # for topic, ids in grouped_data.items():
    #     topic_indi = topic.split(", ")
    #     for indi in topic_indi:
    #         if indi not in category:
    #             category[indi] = []
    #         category[indi].extend(ids)
    # for indi, ids in category.items():
    #     category[indi] = sorted(ids, key=lambda x: int(x[2:]))
    # for indi, ids in sorted(category.items()):
    #     print(f"{indi}: {', '.join(ids)}; total: {len(ids)}")

def check_lines():
    file_path = "/Users/ruizhengu/Downloads/ISSTA2023-VRTesting-ReplPackage/ReplicationPackage/VR_Project_List.txt"
    with open(file_path, 'r', encoding='utf-8') as file:
        print(sum(1 for _ in file))


# listing_venue()
# listing_research_type()
# listing_tool()
# listing_dataset()
# listing_topic()
listing_objective()