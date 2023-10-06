import argparse

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file',help='pdf file name')
    parser.add_argument('-r','--read',action='store_true',help='read and print the file')
    parser.add_argument('-m','--filedata',action='store_true')
    args = parser.parse_args()
    #access to the args
    read_mode = args.read
    file_name = args.file
    file_data = args.filedata
    return file_name,read_mode,file_data 


def read_file(file_name):
    file = open(file_name,'r')
    content = file.read()
    return(content)#.replace("\n",""))

def metadata(file_name):
    from pypdf import PdfReader
    reader = PdfReader(file_name)
    meta = reader.metadata
    #with open(file_name, 'rb') as f:
     #   content = f.read()
    author = meta.author
    title = meta.title
    subject = meta.subject
    return author,title,subject


if __name__ == "__main__":
    file_name, read_mode,file_data= argument_parser()
    #print(file_name)
    #print(read_mode)

    if read_mode:
        #print(f"Reading {file_name}...")
        print(read_file(file_name))

    elif file_data:
        print(metadata(file_name))

