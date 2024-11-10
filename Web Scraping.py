with open('nounlist.txt', 'r') as file:
    lines = file.readlines()

words_to_learn = [line.strip() for line in lines]

print(words_to_learn)