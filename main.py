import argparse
from pypdf import PdfReader, PdfWriter
import getpass

def argument_parser():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(description='PDF utility to read, fetch metadata, and lock a PDF file.')
    parser.add_argument('file', help='PDF file name')
    parser.add_argument('-r', '--read', action='store_true', help='Read and print the file')
    parser.add_argument('-m', '--metadata', action='store_true', help='Display file metadata')
    parser.add_argument('-l', '--lock', action='store_true', help='Lock the file with a password')
    args = parser.parse_args()
    return args.file, args.read, args.metadata, args.lock

def read_file(file_name):
    """Read and return the content of a PDF file."""
    try:
        with open(file_name, 'rb') as file:
            reader = PdfReader(file)
            return "\n".join(page.extract_text() for page in reader.pages)
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None

def get_metadata(file_name):
    """Return metadata of the PDF file."""
    try:
        reader = PdfReader(file_name)
        return reader.info.author, reader.info.title, reader.info.subject
    except Exception as e:
        print(f"An error occurred while fetching metadata: {str(e)}")
        return None, None, None

def lock_file(file_name, password):
    """Encrypt and lock the PDF file with a password."""
    try:
        reader = PdfReader(file_name)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        with open(file_name, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(f"An error occurred while locking the file: {str(e)}")

if __name__ == "__main__":
    file_name, read_mode, fetch_metadata, lock_mode = argument_parser()
    
    try:
        if read_mode:
            print(read_file(file_name) or "Unable to read file.")
        elif fetch_metadata:
            author, title, subject = get_metadata(file_name)
            if author and title and subject:
                print(f"Author: {author}, Title: {title}, Subject: {subject}")
            else:
                print("Unable to fetch metadata.")
        elif lock_mode:
            password = getpass.getpass('Enter a password: ')
            lock_file(file_name, password)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
