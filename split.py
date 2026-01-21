# pip install PyPDF2
from PyPDF2 import PdfReader, PdfWriter

input_path = "C:\\Users\\ZJendex\\Downloads\\PolyPosePosters.pdf"

# Read the original PDF
reader = PdfReader(input_path)

# Loop through all pages
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)

    # Create a file name based on the page number (starting from 1)
    output_filename = f"{i + 1}.pdf"
    
    # Write the single-page PDF
    with open(output_filename, "wb") as f:
        writer.write(f)

    print(f"Saved page {i + 1} → {output_filename}")
