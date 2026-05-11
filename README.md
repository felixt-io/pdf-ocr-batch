# PDF OCR Batch

A small Python tool that batch-OCRs a folder of scanned PDFs into fully searchable PDFs. Built around `ocrmypdf` and a short script that processes multiple files in parallel.

## Why I built this
I had a stack of old scanned PDFs sitting around as image-only files, and I wanted to make them searchable so I could actually find things in them. Doing each one by hand through a GUI was tedious, so this script runs the whole folder in parallel.

## What it does
- Runs OCR on every PDF in a folder
- Processes multiple PDFs at once for speed
- Lets you choose how to handle PDFs that already contain text

## Requirements
- Python 3.9+
- Tesseract OCR
- Ghostscript

macOS (Homebrew):
```
brew install tesseract ghostscript
```

Python packages:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick start
```
python scripts/pdf_ocr_batch.py --input ./input_pdfs --output ./output_pdfs
```

## Usage
```
python scripts/pdf_ocr_batch.py \
  --input ./input_pdfs \
  --output ./output_pdfs \
  --language eng \
  --workers 4
```

## Options
- `--skip-text` (default): skip pages that already contain text
- `--force-ocr`: re-run OCR even if text exists
- `--redo-ocr`: redo OCR only where text exists

## Notes and limitations
- OCR quality depends on scan quality (contrast, skew, resolution).
- Use the right language pack for better accuracy.
- Large batches can be CPU-intensive; adjust `--workers`.

## Troubleshooting
- Error: `gs could not be found` means Ghostscript is not installed or not on PATH.
- Error: `page already has text` can be handled with `--skip-text` (default), `--force-ocr`, or `--redo-ocr`.

## Repo layout
- `scripts/pdf_ocr_batch.py`: main batch OCR script
- `docs/notes.md`: short project notes

## License
MIT. See `LICENSE`.
