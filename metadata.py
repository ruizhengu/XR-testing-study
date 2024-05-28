import re
from pathlib import Path

import bibtexparser
from openpyxl import Workbook, load_workbook
import os
import glob


class Metadata:
    def __init__(self):
        self.dl_dict = {
            "ACM": {"files": "acm*.bib", "sheet": "ACM"},
            "IEEE": {"files": "IEEE*.bib", "sheet": "IEEE"},
            "Scopus": {"files": "scopus*.bib", "sheet": "Scopus"}
        }
        self.dl = self.dl_dict["Scopus"]
        self.iter_root = Path("iter-1")

        self.bib_folder = self.iter_root / "bib"
        self.bib_files = glob.glob(os.path.join(self.bib_folder, self.dl["files"]))
        self.excel_file = self.iter_root / "XR Testing Literature.xlsx"
        self.headers = [
            "Title",
            "Author",
            "Year",
            "Publisher",
            "DOI",
            "Booktitle",
            "Journal",
            "Keywords"
        ]
        if os.path.exists(self.excel_file):
            self.workbook = load_workbook(self.excel_file)
            self.sheet = self.workbook[self.dl["sheet"]]
        else:
            self.workbook = Workbook()
            self.sheet = self.workbook.active
        self.sheet.append(self.headers)

    def keyword_verification(self):
        count_search_results = 0
        count_keyword_verification = 0
        for bib_file in self.bib_files:
            with open(bib_file) as file:
                bib_data = bibtexparser.load(file)
            for entry in bib_data.entries:
                count_search_results += 1
                title = entry.get("title", "N/A")
                if (
                        re.search(r'virtual reality', title, re.IGNORECASE) or
                        re.search(r'augmented reality', title, re.IGNORECASE) or
                        re.search(r'mixed reality', title, re.IGNORECASE) or
                        re.search(r'extended reality', title, re.IGNORECASE) or
                        re.search(r'\bVR\b', title) or
                        re.search(r'\bAR\b', title) or
                        re.search(r'\bXR\b', title) or
                        re.search(r'\bMR\b', title)
                ) and (
                        re.search(r'test', title, re.IGNORECASE) or
                        re.search(r'validat', title, re.IGNORECASE) or
                        re.search(r'verifi', title, re.IGNORECASE) or
                        re.search(r'bug', title, re.IGNORECASE) or
                        re.search(r'defect', title, re.IGNORECASE) or
                        re.search(r'fault', title, re.IGNORECASE) or
                        re.search(r'error', title, re.IGNORECASE)
                ) and not re.search(r'usability', title, re.IGNORECASE):
                    count_keyword_verification += 1
                    self.save_metadata(entry)
        print("count_search_results", count_search_results)
        print("count_keyword_verification", count_keyword_verification)

    def save_metadata(self, entry):
        title = entry.get("title", "N/A")
        author = entry.get("author", "N/A")
        year = entry.get("year", "N/A")
        publisher = entry.get("publisher", "N/A")
        doi = entry.get("doi", "N/A")
        booktitle = entry.get("booktitle", "N/A")
        journal = entry.get("journal", "N/A")
        keywords = entry.get("keywords", "N/A")
        self.sheet.append([
            title,
            author,
            year,
            publisher,
            doi,
            booktitle,
            journal,
            keywords
        ])
        self.workbook.save(self.excel_file)


if __name__ == '__main__':
    m = Metadata()
    # m.save_metadata()
    m.keyword_verification()
