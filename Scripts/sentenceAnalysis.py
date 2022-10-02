# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:23:48 2020

@author: 328576
"""

import en_core_web_sm
import pandas as pd
import spacy
from spacy.symbols import nsubj, VERB
from spacy import displacy
exec(open("Scripts/HelperFuns.py").read())
exec(open("Scripts/getData.py").read())

nlp = en_core_web_sm.load()
nlp.max_length = 10000000

pdf_docs = get_pdf_files('C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC')
pdf_text = pdf_merger(pdf_docs, 'C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC')
pdf_text = remove_spaces(pdf_text)
pdf_text_df = pd.DataFrame(pdf_text, columns=['sentence'])
pdf_text_df.to_csv('C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\FSReports\\pdf_text.csv')

#------------------------------------------------------------------------------------------------------------------
doc = nlp(str(pdf_text))

# sentence analysis
sentences = list(doc.sents)
for sentence in sentences:
    print(sentence)

for sent in doc.sents:
    print(sent.text)


sentenceClean = to_lowercase(sentences)
sentenceClean = remove_stopwords(sentenceClean)
sentenceClean = remove_n_character(sentenceClean)
sentenceClean = remove_punctuation(sentenceClean)
len(sentenceClean)

sentences_df = pd.DataFrame(sentenceClean, columns=['sentence'])
sentences_df.to_csv('C:\\Users\\328576\\PycharmProjects\\pyText\\FSReports\\sentence.csv')

sentence_data = normalize_sentences(sentences)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char,
          ent.label_, spacy.explain(ent.label_))

nouns = []
adjectives = []
for token in doc:
    if token.pos_ == 'NOUN':
        nouns.append(token)
    if token.pos_ == 'ADJ':
        adjectives.append(token)

nouns
adjectives

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Finding a verb with a subject from below — good
verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)

print(verbs)

displacy.serve(doc, style="dep")