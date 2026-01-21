# pip install PyPDF2
from PyPDF2 import PdfReader

input_path = "C:/Users/ZJendex/Downloads/imwut25b-sub7167-i26.pdf"

reader = PdfReader(input_path)
all_text = ""

# Extract text from each page
for page in reader.pages[0:-3]:
    all_text += page.extract_text() or ""

# Count words
word_list = all_text.split()
word_count = len(word_list)

print(f"Total word count: {word_count}")
