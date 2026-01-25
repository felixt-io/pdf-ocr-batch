# PDF OCR Batch Automation

This repo shows a simple, practical automation workflow I use in construction and real estate work: batch OCR for scanned PDFs. It is built around `ocrmypdf` and a small Python script that runs multiple files in parallel.

I am a construction and real estate professional who builds practical tools to cut down admin time. This project batch-OCRs scanned PDFs so they are searchable and easier to review, freeing up time and resources for the critical work that moves a project forward.

## Why this matters
Construction and real estate work generates large volumes of scanned documents (contracts, invoices, reports, permits). OCR makes them searchable and easier to review, share, and audit.

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
