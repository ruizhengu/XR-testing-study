import bibtexparser
from openpyxl import Workbook, load_workbook
import os
import glob


class Metadata:
    def __init__(self):
        # self.bib_files = glob.glob(os.path.join("iter-1/bib", '*.bib'))
        # self.bib_files = glob.glob(os.path.join("iter-1/bib", 'IEEE*.bib'))
        self.bib_files = glob.glob(os.path.join("iter-1/bib", 'scopus*.bib'))
        self.excel_file = "iter-1/XR Testing Literature.xlsx"
        self.headers = [
            "Title",
            "Author",
            "Year",
            "Publisher",
            "DOI",
            "Booktitle",
            "Keywords"
        ]
        # if os.path.exists(self.excel_file):
        #     self.workbook = load_workbook(self.excel_file)
        #     self.sheet = self.workbook["IEEE"]
        # else:
        #     self.workbook = Workbook()
        #     self.sheet = self.workbook.active
        # self.sheet.append(self.headers)

    def keyword_verification(self):
        count = 0
        for bib_file in self.bib_files:
            with open(bib_file) as file:
                bib_data = bibtexparser.load(file)
            for entry in bib_data.entries:
                title = entry.get("title", "N/A")
                if (
                        "virtual reality" in title or "augmented reality" in title or "mixed reality" or "extended reality" in title or "VR" in title or "AR" in title or "XR" in title or "MR" in title) and (
                        "test" in title or "validation" in title or "verification" in title or "bug" in title or "defect" in title or "fault" in title or "error" in title) and "usability" not in title:
                    count += 1
        print(count)

    def save_metadata(self):
        for bib_file in self.bib_files:
            with open(bib_file) as file:
                bib_data = bibtexparser.load(file)
            for entry in bib_data.entries:
                title = entry.get("title", "N/A")
                author = entry.get("author", "N/A")
                year = entry.get("year", "N/A")
                publisher = entry.get("publisher", "N/A")
                doi = entry.get("doi", "N/A")
                booktitle = entry.get("booktitle", "N/A")
                keywords = entry.get("keywords", "N/A")

                self.sheet.append([
                    title,
                    author,
                    year,
                    publisher,
                    doi,
                    booktitle,
                    keywords
                ])

            self.workbook.save(self.excel_file)


if __name__ == '__main__':
    m = Metadata()
    # m.save_metadata()
    m.keyword_verification()