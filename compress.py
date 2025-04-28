# pip install pikepdf
import pikepdf

src  = "merged_normalized.pdf"
dest = "merged_normalized_compressed.pdf"


with pikepdf.open(src) as pdf:
    pdf.remove_unreferenced_resources()             # optional cleanup
    pdf.save(
        dest,
        compress_streams=True,                      # compress any uncompressed streams
        )

print(f"Saved pikepdf-optimized PDF → {dest}")
