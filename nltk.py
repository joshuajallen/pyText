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


from nltk.tokenize import sent_tokenize, word_tokenize

nltk_words = word_tokenize(str(pdf_text))
print(len(nltk_words))
display(f"Tokenized words: {nltk_words}")

import numpy as np
import multiprocessing as mp

import string
import en_core_web_sm
from sklearn.base import TransformerMixin, BaseEstimator
from normalise import normalise

nlp = en_core_web_sm.load()


class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self,
                 variety="BrE",
                 user_abbrevs={},
                 n_jobs=1):
        """
        Text preprocessing transformer includes steps:
            1. Text normalization
            2. Punctuation removal
            3. Stop words removal
            4. Lemmatization

        variety - format of date (AmE - american type, BrE - british format)
        user_abbrevs - dict of user abbreviations mappings (from normalise package)
        n_jobs - parallel jobs to run
        """
        self.variety = variety
        self.user_abbrevs = user_abbrevs
        self.n_jobs = n_jobs

    def fit(self, X, y=None):
        return self

    def transform(self, X, *_):
        X_copy = X.copy()

        partitions = 1
        cores = mp.cpu_count()
        if self.n_jobs <= -1:
            partitions = cores
        elif self.n_jobs <= 0:
            return X_copy.apply(self._preprocess_text)
        else:
            partitions = min(self.n_jobs, cores)

        data_split = np.array_split(X_copy, partitions)
        pool = mp.Pool(cores)
        data = pd.concat(pool.map(self._preprocess_part, data_split))
        pool.close()
        pool.join()

        return data

    def _preprocess_part(self, part):
        return part.apply(self._preprocess_text)

    def _preprocess_text(self, text):
        normalized_text = self._normalize(text)
        doc = nlp(normalized_text)
        removed_punct = self._remove_punct(doc)
        removed_stop_words = self._remove_stop_words(removed_punct)
        return self._lemmatize(removed_stop_words)

    def _normalize(self, text):
        # some issues in normalise package
        try:
            return ' '.join(normalise(text, variety=self.variety, user_abbrevs=self.user_abbrevs, verbose=False))
        except:
            return text

    def _remove_punct(self, doc):
        return [t for t in doc if t.text not in string.punctuation]

    def _remove_stop_words(self, doc):
        return [t for t in doc if not t.is_stop]

    def _lemmatize(self, doc):
        return ' '.join([t.lemma_ for t in doc])


text = TextPreprocessor()
TextPreprocessor(n_jobs=-1).transform(pdf_text)

import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.base import TransformerMixin, BaseEstimator
from normalise import normalise