def remove_parentheses(list):
    x = []
    for word in list:
        if "(" in word:
            x.append(remove(word))
        else:
            continue
    return x


def remove(word):
    x = word.find("(")
    y = word[:(x-1)]
    return y


