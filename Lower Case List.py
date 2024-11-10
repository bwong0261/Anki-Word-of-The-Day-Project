def lower_case(word):
    return word.lower()

x = []
def lower_list(list):
    for word in list:
        x.append(lower_case(word))
    return x

print(lower_list(['HEOO', "HeeoO"]))

