# pip install PyPDF2
from PyPDF2 import PdfReader, PdfWriter

input_path  = "2025_221_PPA_Spec_Kumar_CL ERROR.pdf"
output_path = "2025_221_PPA_Spec_Kumar_CL ERROR_cut.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Copy every page except the last one
for page in reader.pages[:6]:
    writer.add_page(page)

with open(output_path, "wb") as f:
    writer.write(f)

print(f"Saved cut PDF without last page → {output_path}")
