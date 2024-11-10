words_to_learn = ['the', 'how', 'can', 'first', 'second']
current_word_bank = ['the', 'how', 'believe', 'first']

def remove_duplicate_words(x,y):
    for words in y:
        if words in x:
            x.remove(words)
        else:
            continue
    return x

filtered = remove_duplicate_words(words_to_learn,current_word_bank)

print(filtered)

