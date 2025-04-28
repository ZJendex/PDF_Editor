# PDF Utility Scripts

This repository provides a set of Python scripts to prepare and manipulate PDF files for USPTO submission workflows. The scripts cover:

- **cut.py**: Remove the problematic last page that triggers printing errors citeturn1file1.
- **merge.py**: Merge two or more PDF files into one citeturn1file2.
- **merge_normalized.py**: Normalize page sizes across PDFs by padding to a uniform canvas, then output a merged PDF citeturn1file3.
- **compress.py**: Compress and optimize an existing PDF by recompressing streams and removing unused objects citeturn1file0.

---

## Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/) for package installation

## Installation

Install the required libraries via pip:

```bash
python -m pip install PyPDF2 pikepdf
```

- **PyPDF2** (or its modern fork `pypdf`) is used for page manipulation.
- **pikepdf** is used for stream compression and resource cleanup.

## Usage

### 1. Remove Last Page (`cut.py`)

```bash
python cut.py <input.pdf> <output_cut.pdf>
```

Removes the last page from `input.pdf` (e.g., the error‐throwing page) and writes the result to `output_cut.pdf`. citeturn1file1

### 2. Merge PDFs (`merge.py`)

```bash
python merge.py <input1.pdf> <input2.pdf> [...] <output_merged.pdf>
```

Merges all specified input PDFs in order into a single file. citeturn1file2

### 3. Normalize & Merge Page Sizes (`merge_normalized.py`)

```bash
python merge_normalized.py <input1.pdf> <input2.pdf> [..] <output_normalized.pdf>
```

1. Scans all input PDFs to find the maximum page width and height.  
2. Pads each page’s `MediaBox`, `CropBox`, and `TrimBox` to that uniform size.  
3. Outputs the merged, uniform‐sized PDF. citeturn1file3

### 4. Compress / Optimize PDF (`compress.py`)

```bash
python compress.py <input.pdf> <output_compressed.pdf>
```

- Removes unreferenced resources.  
- Compresses and recompresses all streams (text, vector, images).  
- Drops unused objects for additional size savings. citeturn1file0


## Example Workflow

1. **Cut out** the error‐page:  
   ```bash
   python cut.py manuscript.pdf manuscript_cut.pdf
   ```  
2. **Merge** with Exhibit A:  
   ```bash
   python merge.py manuscript_cut.pdf ExhibitA.pdf merged.pdf
   ```  
3. (Optional) **Normalize** page sizes:  
   ```bash
   python merge_normalized.py manuscript_cut.pdf ExhibitA.pdf merged_norm.pdf
   ```  
4. **Compress** the final PDF:  
   ```bash
   python compress.py merged_norm.pdf merged_final.pdf
   ```  

The resulting `merged_final.pdf` should be under the USPTO file-size limits and free of PostScript tiling errors when printed via CutePDF.

---

## License

MIT License. Feel free to adapt these scripts for your own workflows.

