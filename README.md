# Huffman Compression

This script compresses text from a file using Huffman coding and saves the result with statistics.

## Description

- Reads input from `files/base_file.txt`
- Calculates character frequencies
- Generates Huffman codes
- Encodes the file contents using the codes
- Saves the encoded text and compression stats to `files/compressed_text.txt`

## Files

- `base_file.txt`: Input file with the original text
- `compressed_text.txt`: Output file with encoded data and compression information

## Output Format

Includes:
- Huffman table (char, frequency, code)
- Encoded text
- Size before and after compression (in bits)

## How to Run

Just run the script directly:

```bash
python your_script_name.py
```

Ensure the input file exists in the `files/` directory.
