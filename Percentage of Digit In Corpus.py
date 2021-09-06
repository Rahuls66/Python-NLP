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
