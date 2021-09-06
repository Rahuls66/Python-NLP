import pandas as pd
import string
from nltk.tokenize import word_tokenize

def digit_perc(sentence: str) -> float:
    
    new_sentence = []
    for word in word_tokenize(sentence):
        for p in list(string.punctuation):
            word = word.replace(p, '')
        new_sentence.append(word)
    
    count = 0
    for i in new_sentence:
        if i.isdigit():
            count += 1
    return round((count / len(new_sentence)) * 100, 2)
  
def freq_bar(corpus):
    freq_dict = {}

    for i, sent in enumerate(tokens):
        freq_dict[i] = digit_perc(sent)
        

pd.DataFrame(freq_dict.values()).plot.bar()
