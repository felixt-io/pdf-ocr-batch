# Project notes

## Mixed page orientation
`ocrmypdf` can handle PDFs with pages in different orientations (portrait and landscape). It uses Tesseract orientation detection to rotate pages before OCR.

## Batch OCR approach
The script runs one OCR job per PDF using a thread pool. This keeps each file isolated and makes it easy to scale up or down based on CPU capacity.

## Dependencies
- `ocrmypdf` (Python)
- Tesseract OCR
- Ghostscript

## Common issues
- `gs could not be found`: install Ghostscript and ensure it is on PATH.
- `page already has text`: use `--skip-text` (default), `--force-ocr`, or `--redo-ocr` depending on your goal.
