import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import ocrmypdf


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run OCR on all PDFs in a folder using ocrmypdf.",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Folder containing input PDF files",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Folder to write OCR output PDFs",
    )
    parser.add_argument(
        "--language",
        default="eng",
        help="OCR language (e.g. eng, eng+fra)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of PDFs to process in parallel",
    )

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--skip-text",
        action="store_true",
        help="Skip pages that already contain text (default)",
    )
    mode.add_argument(
        "--force-ocr",
        action="store_true",
        help="Force OCR even if text already exists",
    )
    mode.add_argument(
        "--redo-ocr",
        action="store_true",
        help="Redo OCR only on pages that already contain text",
    )

    return parser.parse_args()


def resolve_mode(args):
    if args.force_ocr:
        return "force_ocr"
    if args.redo_ocr:
        return "redo_ocr"
    if args.skip_text:
        return "skip_text"
    return "skip_text"


def ocr_pdf(file_name, input_folder, output_folder, language, mode):
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, f"ocr_{file_name}")

    options = {
        "language": language,
        "use_threads": True,
        "progress_bar": False,
    }
    if mode == "skip_text":
        options["skip_text"] = True
    elif mode == "force_ocr":
        options["force_ocr"] = True
    elif mode == "redo_ocr":
        options["redo_ocr"] = True

    try:
        ocrmypdf.ocr(input_path, output_path, **options)
        return f"OK: {file_name}"
    except Exception as exc:
        return f"FAIL: {file_name} ({exc})"


def main():
    args = parse_args()
    input_folder = os.path.abspath(args.input)
    output_folder = os.path.abspath(args.output)
    os.makedirs(output_folder, exist_ok=True)

    if not os.path.isdir(input_folder):
        raise SystemExit(f"Input folder not found: {input_folder}")

    mode = resolve_mode(args)
    workers = max(1, args.workers)

    pdf_files = sorted(
        f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")
    )
    if not pdf_files:
        raise SystemExit("No PDF files found in the input folder.")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                ocr_pdf,
                pdf,
                input_folder,
                output_folder,
                args.language,
                mode,
            )
            for pdf in pdf_files
        ]
        for future in as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    main()
