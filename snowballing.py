import fitz
import pdfx

# try:
pdf = pdfx.PDFx("/Users/ruizhengu/Experiments/XR_PS/kaminska2022UsabilityTestingVirtual.pdf")
# pdf_path = "/Users/ruizhengu/Experiments/XR_PS/kaminska2022UsabilityTestingVirtual.pdf"
# tmp_path = "/Users/ruizhengu/Experiments/XR_PS/ref_kaminska2022UsabilityTestingVirtual/tmp.txt"

references_list = pdf.get_references()

# print(pdf.get_references_count())


# print(references_list)

# with fitz.open(pdf_path) as doc:
#     text_content = ""
#     for page in doc:
#         text_content += page.get_text("text")
#
# with open(tmp_path, "w", encoding="utf-8") as tmp_file:
#     tmp_file.write(text_content)
#
# pdf = pdfx.PDFx(tmp_path)
# references_list = pdf.get_references()
# print(references_list)