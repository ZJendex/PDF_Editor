from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import RectangleObject

def normalize_page_sizes(input_paths, output_path):
    # 1) Read all pages and record their sizes
    all_pages = []
    sizes = []
    for path in input_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            # page.media_box gives [llx, lly, urx, ury]
            width  = float(page.mediabox.width)
            height = float(page.mediabox.height)
            sizes.append((width, height))
            all_pages.append(page)

    # 2) Compute the target canvas size (max width & height)
    max_w = max(w for w, h in sizes)
    max_h = max(h for w, h in sizes)

    # 3) Create a writer and “pad” each page
    writer = PdfWriter()
    for page in all_pages:
        # Reset origin to (0,0)
        page.mediabox.lower_left = (0, 0)
        # Set upper right to (max_w, max_h)
        page.mediabox.upper_right = (max_w, max_h)
        # (Optionally also adjust cropBox / trimBox if present)
        page.trimbox = RectangleObject([0, 0, max_w, max_h])
        page.cropbox = RectangleObject([0, 0, max_w, max_h])
        writer.add_page(page)

    # 4) Write out the normalized PDF
    with open(output_path, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    inputs = ["2025_221_PPA_Spec_Kumar_CL ERROR_cut.pdf", "2025_221_PPA_ExhibitA_Kumar_CL 24APR2025.pdf"]
    normalize_page_sizes(inputs, "merged_normalized.pdf")
    print("Saved → merged_normalized.pdf")
