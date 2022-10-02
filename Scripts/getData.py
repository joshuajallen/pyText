# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:33:33 2020

@author: 328576
"""

import os
import io
import pickle
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

# directory = 'C:\\Users\\328576\\PycharmProjects\\TextAnalytics\\FSReports'


def get_pdf_files(directory):
    """
    # Function: get_pdf_files
    #
    #   Description:
    #       Function to run get list of pdf_files from a user defined directory
    #   Input:
    #       directory[string]: file path in string format e.g. 'C:\\Users\\...\\FSReports'
    #   Output:
    #       pdf files [list]: list of pdf_files
    #
    """
    try:
        pdf_files = []

        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                pdf_files.append(directory + '//' + filename)
                pdf_files.sort(key=str.lower)
                pdf_files = list(map(lambda x: str.replace(x, "//", "\\"), pdf_files))

    except FileNotFoundError:
        print('data load failed')

    return pdf_files


def pdf_merger(pdf_files, write_path):
    """
    # Function: pdf_merger
    #
    #   Description:
    #       Function to merge a corpus of pdf documents into text file
    #   Input:
    #       pdf_files[list]: file path(s) in string format as a list e.g. 'C:\\Users\\...\\.my_pdf.pdf'
    #       write_path[string]: file path indicating location to write text file of documents to
    #   Output:
    #       pdf text [list]: list of pdf text extracted from the corpus of documents
    #
    """
    try:
        pdf_text = []

        for filename in pdf_files:

            resource_manager = PDFResourceManager()
            file_handle = io.StringIO()
            converter = TextConverter(resource_manager, file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)

            with open(filename, 'rb') as fh:
                for page in PDFPage.get_pages(fh,
                                              caching=True,
                                              check_extractable=True):
                    page_interpreter.process_page(page)

                text = file_handle.getvalue()
                # close open handles
                converter.close()
                file_handle.close()

                if text:
                    pdf_text.append(text.split(maxsplit=0))

        if pdf_text != '':
            with open(write_path + '\\pdf_text.text', 'wb') as file:
                # store the data as binary data stream
                pickle.dump(pdf_text, file)

    except FileNotFoundError:
        print('data load failed')

    return pdf_text



def get_text_files(directory):
    """
    # Function: get_text_files
    #
    #   Description:
    #       Function to run get list of text_files from a user defined directory
    #   Input:
    #       directory[string]: file path in string format e.g. 'C:\\Users\\...\\FSReports'
    #   Output:
    #       text files [list]: list of text_files
    #
    """
    try:
        text_files = []

        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                text_files.append(directory + '//' + filename)
                text_files.sort(key=str.lower)
                text_files = list(map(lambda x: str.replace(x, "//", "\\"), text_files))

    except FileNotFoundError:
        print('data load failed')

    return text_files


def text_merger(text_files, write_path):
    """
    # Function: pdf_merger
    #
    #   Description:
    #       Function to merge a corpus of pdf documents into text file
    #   Input:
    #       pdf_files[list]: file path(s) in string format as a list e.g. 'C:\\Users\\...\\.my_pdf.pdf'
    #       write_path[string]: file path indicating location to write text file of documents to
    #   Output:
    #       pdf text [list]: list of pdf text extracted from the corpus of documents
    #
    """
    try:
        text = []
        for filename in text_files:
            with open(filename, 'r+', encoding='utf-8') as f:
                text_obj = f.readlines()
                if text_obj != '':
                    text.append(str(text_obj))

        if text != '':
            with open(write_path + '\\pdf_text.text', 'wb') as file:
                # store the data as binary data stream
                pickle.dump(text, file)

    except FileNotFoundError:
        print('data load failed')

    return text


def extract_text_from_pdf(pdf_path):

    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text.split(maxsplit=0)


#if __name__ == '__main__':
#    paths = glob.glob('pdf_files_path/I*.pdf')
#    # Retrieve all pdfs start with I
#    pdfFiles.sort()
#    merger('C:\\Users\\328576\\PycharmProjects\\TextAnalytics\\FSReports\\pdf_merger.pdf', pdfFiles)
