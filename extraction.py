from collections import Counter

import pandas as pd

class DataExtraction:
    def __init__(self):
        self.data = pd.read_excel("XR_Study.xlsx", sheet_name="Data Extraction")
        self.authors = self.data["authors"].tolist()

    def rank_authors(self):
        author_rank = Counter()
        for authors in self.authors:
            if pd.notna(authors):
                individual_authors = [author.strip() for author in authors.split(";")]
                author_rank.update(individual_authors)
        ranked_authors = dict(author_rank.most_common())
        return ranked_authors

extraction = DataExtraction()
print(extraction.rank_authors())
