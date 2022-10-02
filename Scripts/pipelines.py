# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:23:48 2020

@author: 328576
"""

# --------------------------------------------------------------------------------------------------
# load libraries

from collections import Counter
import textacy
import en_core_web_sm
import pandas as pd
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

# --------------------------------------------------------------------------------------------------
# call functions

exec(open("Scripts/HelperFuns.py").read())
exec(open("Scripts/getData.py").read())

nlp = en_core_web_sm.load()
nlp.max_length = 10000000

# define wd for text extraction

myDir = 'C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC'

# --------------------------------------------------------------------------------------------------
# get pdf data

pdf_docs = get_pdf_files(myDir)
print(pdf_docs)  # print list of pdf files in directory

pdf_text = pdf_merger(pdf_docs, myDir)  # merger pdf txt into one list, outputs to myDir
print(pdf_text)  # check first 100 characters of string

pdf_text_df = pd.DataFrame(pdf_text, columns=['sentence'])  # convert to pandas DF and save as .csv file
pdf_text_df.to_csv(myDir + '\\pdf_text.csv')

if len(pdf_text) == len(pdf_docs):
    print('The data frame is of the correct length')
else:
    print('The data frame is not of the correct length, number of rows != ' + len(pdf_docs))


# --------------------------------------------------------------------------------------------------
# convert words into tokens

pdf_text_words = clean_corpus_words(pdf_text)
pdf_text_sentences = clean_corpus_sentences(pdf_text)

docWords = nlp(str(pdf_text_words))
docSentences = nlp(str(pdf_text_sentences))

words = [token.text for token in docWords]
words[1:20]  # view sample of the un-cleansed words

words = normalize_words(words)
words[1:20]  # view sample of the cleansed words

sentences = [sent.text for sent in docSentences.sents]
sentences[1:20]  # view sample of the un-cleansed sentences

sentences = normalize_sentences(sentences)
sentences[1:20]  # view sample of the cleansed words

twoGrams = list(textacy.extract.ngrams(docWords, 2, min_freq=2))
print(twoGrams)

twoGrams = normalize_words(twoGrams)
twoGrams[1:20]

threeGrams = list(textacy.extract.ngrams(docWords, 3, min_freq=2))
print(threeGrams)

threeGrams = normalize_words(threeGrams)
threeGrams[1:20]

# --------------------------------------------------------------------------------------------------
# display results for word tokens

#  most common word tokens
word_freq = Counter(words)
common_words = pd.DataFrame(word_freq.most_common(20), columns=['keywords', 'Count'])
print(common_words)

count = common_words.plot(kind='bar', x='keywords', y='Count', color='red')
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
plt.show()

fdist = FreqDist(words)
print(fdist)
fdist.most_common(20)
# Frequency Distribution Plot
frequency = fdist.plot(30,cumulative=False)
plt.show()

# --------------------------------------------------------------------------------------------------
# display results for bigram tokens

#  most common word tokens
bigram_freq = Counter(twoGrams)
common_bigram = pd.DataFrame(bigram_freq.most_common(20), columns=['keywords', 'Count'])
print(common_bigram)

count = common_bigram.plot(kind='bar', x='keywords', y='Count', color='red')
plt.show()

bigram_freq = Counter(threeGrams)
common_bigram = pd.DataFrame(bigram_freq.most_common(20), columns=['keywords', 'Count'])
print(common_bigram)

count = common_bigram.plot(kind='bar', x='keywords', y='Count', color='red')
plt.show()



# ----------------------------------------------------------------------------------------------------
