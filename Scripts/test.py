
try:
    text = []
    for filename in text_files:
        with open(filename, 'r+', encoding='utf-8') as f:
            text_obj = f.readlines()
            if text_obj != '':
                text.append(text_obj)

    if text != '':
        with open(write_path + '\\pdf_text.text', 'wb') as file_handle:
            # store the data as binary data stream
            pickle.dump(text, file_handle)

except FileNotFoundError:
    print('data load failed')



#------------------------

import textract
textract.process

pdf_text = []
for filename in pdf_files:
    pdf_file_obj = open(str(filename), 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    num_pages = pdf_reader.numPages
    count = 0
    pdf_textract = ""

    # The while loop will read each page
    while count < num_pages:
        page_obj = pdf_reader.getPage(count)
        count += 1
        pdf_textract = page_obj.extractText()

        if pdf_textract != '':
            pdf_text.append(pdf_textract)

if pdf_text != '':
    with open(write_path + '\\pdf_text.text', 'wb') as file_handle:
        # store the data as binary data stream
        pickle.dump(pdf_text, file_handle)


# - ----------


import io
import pickle
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


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


if __name__ == '__main__':
    pdf_text = extract_text_from_pdf('C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC\\august-2018.pdf')
    pdf_text_df = pd.DataFrame(pdf_text, columns=['sentence'])
    pdf_text_df.to_csv('C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\FSReports\\pdf_text.csv')
    print(pdf_text)


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


def concatenate_list_data(list):

    result = ''

    for element in list:
        result += str(element)

    return result

pdf_docs = get_pdf_files('C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC')
print(pdf_docs)
pdf_text = pdf_merger(pdf_docs, 'C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC')
pdf_text = remove_spaces(pdf_text)
pdf_text_df = pd.DataFrame(pdf_text, columns=['sentence'])
pdf_text_df.to_csv('C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\FSReports\\pdf_text.csv')

from spacy.lang.en import English
import textacy
nlp = English()

# Create the pipeline 'sentencizer' component
sbd = nlp.create_pipe('sentencizer')

# Add the component to the pipeline
nlp.add_pipe(sbd)



import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# Create our list of punctuation marks
punctuations = string.punctuation

# Create our list of stopwords
stop_words = nlp.Defaults.stop_words

# Load English tokenizer, tagger, parser, NER and word vectors
parser = English()

# Creating our tokenizer function
def spacy_tokenizer(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = parser(sentence)

    # Lemmatizing each token and converting each token into lowercase
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]

    # Removing stop words
    mytokens = [ word for word in mytokens if word not in stop_words and word not in punctuations ]

    # return preprocessed list of tokens
    return mytokens


bow_vector = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
tfidf_vector = TfidfVectorizer(tokenizer = spacy_tokenizer)