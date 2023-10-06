import argparse
from pypdf import PdfReader, PdfWriter

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file',help='pdf file name')
    parser.add_argument('-r','--read',action='store_true',help='read and print the file')
    parser.add_argument('-m','--filedata',action='store_true')
    parser.add_argument('-l','--lock',action='store_true')
    args = parser.parse_args()
    #access to the args
    read_mode = args.read
    file_name = args.file
    file_data = args.filedata
    file_lock = args.lock
    return file_name,read_mode,file_data, file_lock


def read_file(file_name):
    file = open(file_name,'r')
    content = file.read()
    return(content)#.replace("\n",""))

def metadata(file_name):
    reader = PdfReader(file_name)
    meta = reader.metadata
    author = meta.author
    title = meta.title
    subject = meta.subject
    return author,title,subject

def lock(file_name,pwd):
        reader = PdfReader(file_name)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(pwd)
        with open(file_name,"wb") as f:
            writer.write(f)
if __name__ == "__main__":
    file_name, read_mode,file_data, file_lock= argument_parser()
    #print(file_name)
    #print(read_mode)

    if read_mode:
        #print(f"Reading {file_name}...")
        print(read_file(file_name))

    elif file_data:
        print(metadata(file_name))

    elif file_lock:
        password = input('saisie un mot de passe: ')
        (lock(file_name,password))


