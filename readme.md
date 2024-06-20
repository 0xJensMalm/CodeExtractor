# Folder Code Extractor

Folder Code Extractor is a command-line tool for extracting and displaying the structure and content of code files from a specified folder. It supports multiple file types and provides an interactive interface for easy navigation and selection.

## Features

- Display the structure of a specified folder.
- Select specific file types to include in the output.
- Output the folder structure and content of selected files.
- Option to copy the output to the clipboard.

## Installation

1. Clone the repository or download the script file `code_extract.py`.

2. Install the required dependencies using pip:
   ```bash
   pip install inquirer pyperclip
   ```

## Usage

1. Run the script:

   ```bash
   python file_combiner_cli.py
   ```

2. Enter the folder path when prompted:

   ```
   Input folder path: /path/to/your/folder
   ```

3. Select the file types to include in the output. Use the arrow keys to navigate, the Spacebar to select/deselect, and Enter to confirm:

   ```
   Select file types
   ( ) html
   ( ) css
   ( ) js
   ( ) py
   ```

4. The script will display the structure and content of the selected files in the terminal.

5. After displaying the output, you will be prompted to copy the output to the clipboard. Confirm with 'y' or 'n':
   ```
   Copy to clipboard? [y/N]: y
   ```

## Example
