import bibtexparser

bib_file = "bib/acm.bib"

with open(bib_file) as file:
    bib_data = bibtexparser.load(file)

for entry in bib_data.entries:
    title = entry.get("title")
    print(f"Title: {title}")
