from pathlib import Path

import bibtexparser


def return_entries(files):
    entries = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            bib_data = bibtexparser.load(f)
        for entry in bib_data.entries:
            title = entry.get("title", "N/A")
            entries.append(title)
    return entries


def compare():
    files_1 = [
        Path("/Users/ruizhengu/Downloads/acm_1.bib"),
        Path("/Users/ruizhengu/Downloads/acm_2.bib")
    ]
    files_2 = [
        Path("/Users/ruizhengu/Downloads/acm.bib")
    ]
    entries_1 = return_entries(files_1)
    entries_2 = return_entries(files_2)
    for entry in entries_1:
        if entry not in entries_2:
            print("Not in entries_2: " + entry)
    for entry in entries_2:
        if entry not in entries_1:
            print("Not in entries_1: " + entry)


compare()
