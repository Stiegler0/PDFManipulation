# PDF Tool

PDF Tool is a simple Python command-line utility that allows you to perform various operations on PDF files, including reading, extracting metadata, and locking with a password.

## Features

- Read and print the contents of a PDF file.
- Display metadata information such as author, title, and subject.
- Lock a PDF file with a password for added security.

## Prerequisites

Before using this tool, make sure you have the following installed:

- Python (3.x)
- pypdf library (install using `pip install pypdf2`)

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pdf-tool.git
   cd pdf-tool
   
2. Run the tool with the following command:
   ```bash
   python pdf_tool.py [options] file.pdf
3. Replace [options] with one of the following:
   -r or --read: Read and print the contents of the PDF file.
   -m or --filedata: Display metadata information for the PDF file.
   -l or --lock: Lock the PDF file with a password.
   
## Example usages:
1. Read the contents of a PDF file:
   ```bash
   python pdf_tool.py -r mydocument.pdf

2. Display metadata information:
   ```bash
   python pdf_tool.py -m mydocument.pdf
   
3. Lock a PDF with a password:
   ```bash
   python pdf_tool.py -l mydocument.pdf
You will be prompted to enter a password for locking the PDF.

## Security Considerations
When using the -l or --lock option to lock a PDF with a password, consider the following security best practices:

Use strong and unique passwords.
Store passwords securely.
Be cautious when sharing password-protected PDFs, and only share passwords with trusted individuals

## Contribution
If you have any suggestions, bug reports, or would like to contribute to this project, please open an issue or a pull request on GitHub.

Happy PDF processing!
