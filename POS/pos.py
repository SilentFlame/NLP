#!/usr/bin/env python


import nltk, string

# Set of all available punctuations. Set because don't want repitions. 
punctuation = set(string.punctuation)
            

def pos_tag(text):

    '''
    
    Function for returning parts of speech for the text provided. 
    Steps:
        1. First word tokenize the text. 
        2. Then check for punctuation.
        3. Lowercase the words obtained after removing punctuation
        4. Now pos_tag the subset of words thus obtained. 
    '''
    pos = nltk.pos_tag([word.lower() for word in nltk.wordpunct_tokenize(text) if word not in punctuation])
    return pos


