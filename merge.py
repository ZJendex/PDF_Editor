from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_paths, output_path):
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        # append all pages from this reader
        for page in reader.pages:
            writer.add_page(page)

    # write out the merged PDF
    with open(output_path, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    inputs  = ["2025_221_PPA_Spec_Kumar_CL ERROR_cut.pdf", "2025_221_PPA_ExhibitA_Kumar_CL 24APR2025.pdf"]           # your two (or more) PDFs
    output  = "merged_output.pdf"
    merge_pdfs(inputs, output)
    print(f"Merged {inputs} → {output}")
