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

from pathlib import Path

def merge_all_pdfs_pathlib(directory_path, output_filename="merged_output.pdf"):
    """
    Merge all PDF files in a directory using pathlib
    """
    # Convert to Path object
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"Directory does not exist: {directory_path}")
        return
    
    # Find all PDF files
    pdf_files = list(dir_path.glob("*.pdf"))
    
    # # Sort the files alphabetically
    # pdf_files.sort()
    
    if not pdf_files:
        print(f"No PDF files found in directory: {directory_path}")
        return
    
    print(f"Found {len(pdf_files)} PDF files:")
    for pdf in pdf_files:
        print(f"  - {pdf.name}")
    
    # Convert Path objects to strings for compatibility
    pdf_file_paths = [str(pdf) for pdf in pdf_files]
    
    # Create output path
    output_path = dir_path / output_filename
    
    # Merge PDFs
    merge_pdfs(pdf_file_paths, str(output_path))
    print(f"Merged {len(pdf_files)} PDFs → {output_filename}")

if __name__ == "__main__":
    # inputs  = ["2025_221_PPA_Spec_Kumar_CL ERROR_cut.pdf", "2025_221_PPA_ExhibitA_Kumar_CL 24APR2025.pdf"]           # your two (or more) PDFs
    # output  = "merged_output.pdf"
    # merge_pdfs(inputs, output)
    # print(f"Merged {inputs} → {output}")

    directory_path = "G:\\My Drive\\Lab shopping\\25Nov\\counted"  # e.g., "/path/to/your/pdfs" or "C:\\path\\to\\your\\pdfs"
    
    # Option 1: Basic merge (recommended)
    merge_all_pdfs_pathlib(directory_path, "Receips.pdf")
