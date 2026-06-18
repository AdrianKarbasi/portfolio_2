import sys
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print('PyPDF2 not installed', file=sys.stderr)
    raise

def extract_text(pdf_path, out_path):
    reader = PyPDF2.PdfReader(pdf_path)
    texts = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            texts.append(f"=== PAGE {i} ===\n")
            texts.append(page.extract_text() or "")
            texts.append("\n\n")
        except Exception as e:
            texts.append(f"[Error extracting page {i}: {e}]\n")

    out_path.write_text("".join(texts), encoding='utf-8')

def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('Lebenslauf Adrian Karbasi.pdf')
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('extracted_text.txt')
    if not pdf.exists():
        print(f'PDF not found: {pdf}', file=sys.stderr)
        sys.exit(2)
    extract_text(pdf, out)
    print(f'Wrote extracted text to {out}')

if __name__ == '__main__':
    main()
