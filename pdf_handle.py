import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os, sys, PyPDF2, docx, subprocess, uuid

root = tk.Tk()
root.withdraw()

#------------------------------------------------------------------------------------#
#                                    File Dialogs                                    #
#------------------------------------------------------------------------------------#

def open_pdf(dialog_title):
    file_path = filedialog.askopenfilename(title=dialog_title, filetypes=[('PDF file', ('.pdf'))])
    if file_path.strip() == '':
        sys.exit()
    pdf_file = open(file_path, 'rb')
    return pdf_file

def open_word(dialog_title):
    file_path = filedialog.askopenfilename(title=dialog_title, filetypes=[('Word file', ('.doc','.docx'))])
    if file_path.strip() == '':
        sys.exit()
    word_file = open(file_path, 'rb')
    return word_file

def open_multiple_pdfs(dialog_title):
    files_path = filedialog.askopenfilenames(title=dialog_title, filetypes=[('PDF file', ('.pdf'))])
    pdf_files = []
    for files in files_path:
        pdf_files.append(files)
    pdf_files.sort()
    return pdf_files

def save_this_file(dialog_title, dialog_ext):
    file_output = filedialog.asksaveasfile(mode='wb', defaultextension=dialog_ext, title=dialog_title)
    if file_output is None:
        messagebox.showinfo('Error', 'Location Undefined!')
        sys.exit()
    return file_output

#------------------------------------------------------------------------------------#

def pdf_to_word():
    pdf_file = open_pdf('Choose a PDF file for conversion')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = []
    for pages in range(pdf_reader.numPages):
        page_object = pdf_reader.getPage(pages)
        text.append(page_object.extractText())
        print(text)
    word_file = save_this_file('Choose the location to Save output Word Document', '.docx')
    doc = docx.Document()
    doc.add_paragraph('\n'.join(text))
    doc.save(word_file)
    pdf_file.close()
    messagebox.showinfo('Success', 'PDF to Word Conversion Successful!')

def word_to_pdf():
    word_file = open_word('Choose a Word file for processing..')
    # pdf_output = save_this_pdf()
    word_file.close()
    # pdf_output.close()
    messagebox.showinfo('Success', 'Word to PDF Conversion Successful!')

def decrypt_pdf():
    pdf_file = open_pdf('Choose a PDF file to Decrypt..')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    password = simpledialog.askstring(title='Decrypting PDF', prompt='Enter Password', show='\u2022')
    pdf_reader.decrypt(password)
    pdf_writer = PyPDF2.PdfFileWriter()
    for pages in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(pages))
    pdf_output = save_this_file('Choose the location to Save output PDF', '.pdf')
    pdf_writer.write(pdf_output)
    pdf_output.close()
    pdf_file.close()
    messagebox.showinfo('Success', 'PDF Decryption Successful!')

def encrypt_pdf():
    pdf_file = open_pdf('Choose a PDF file to Encrypt..')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    for pages in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(pages))
    password = simpledialog.askstring(title='Encrypting PDF', prompt='Enter Password', show='\u2022')
    pdf_writer.encrypt(password)
    pdf_output = save_this_file('Choose the location to Save output PDF', '.pdf')
    pdf_writer.write(pdf_output)
    pdf_output.close()
    pdf_file.close()
    messagebox.showinfo('Success', 'PDF Encryption Successful!')

def pdf_merge():
    pdf_files = open_multiple_pdfs('Choose multiple PDF files for processing..')
    pdf_writer = PyPDF2.PdfFileWriter()
    for filename in pdf_files:
        pdfFileObj = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(0, pdf_reader.numPages):
            pageObj = pdf_reader.getPage(pageNum)
            pdf_writer.addPage(pageObj)
    pdf_output = save_this_file('Choose the location to Save output PDF', '.pdf')
    pdf_writer.write(pdf_output)
    pdf_output.close()
    pdfFileObj.close()
    messagebox.showinfo('Success', 'PDF Merge Successful!')

def rotate_pdf():
    root = tk.Tk()
    root.withdraw()

def split_pdf():
    pdf_file = open_pdf('Choose a PDF file to Split..')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    file_name = os.path.splitext(os.path.basename(pdf_reader))[0]
    print(str(file_name))
    # for pages in range(pdf_reader.numPages):
    #     pdf_writer = PyPDF2.PdfFileWriter()
    #     pdf_writer.addPage(pdf_reader.getPage(pages))
    #     output_filename = 'pdf_directory/{}_page_{}.pdf'.format(file_name, pages+1)
    # pdf_output = save_this_file('Choose the location to Save output PDF', '.pdf')
    # pdf_writer.write(pdf_output)
    # pdf_output.close()
    # pdf_file.close()
    # messagebox.showinfo('Success', 'PDF Encryption Successful!')

def pdf_compressor():
    root = tk.Tk()
    root.withdraw()

def pdf_to_html():
    pdf_filepath = open_pdf('Choose a PDF file to convert to HTML..').name
    main_path = os.path.split(pdf_filepath)[0]
    tmp = '/tmp'
    guid = str(uuid.uuid1())
    command = 'abiword -t %(tmp)s/%(guid)s.html %(pdf_filepath)s; cat %(tmp)s/%(guid)s.html' % locals()
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=os.path.join(main_path,'website/templates'))
    error = p.stderr.readlines()
    if error:
        raise Exception(''.join(error))
    html = p.stdout.readlines
    return ''.join(html)

# pdf_to_word()
# decrypt_pdf()
# pdf_merge()
encrypt_pdf()
# word_to_pdf()
# split_pdf()
# pdf_to_html()