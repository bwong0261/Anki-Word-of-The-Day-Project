import requests
import json
import random


def invoke(action, **params):
    response = requests.post('http://localhost:8765', json={
        'action': action,
        'version': 6,
        'params': params
    }).json()
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


def get_deck_names():
    return invoke('deckNames')


def get_cards(deck_name):
    card_ids = invoke('findCards', query=f'deck:"{deck_name}"')
    return invoke('cardsInfo', cards=card_ids)


def get_fields_from_deck(deck_name):
    cards = get_cards(deck_name)
    fields_list = []
    for card in cards:
        fields = card['fields']
        fields_list.append({field_name: field['value'] for field_name, field in fields.items()})
    return fields_list


if __name__ == "__main__":
    # Get the list of deck names
    decks = get_deck_names()
    #print(f"Available decks: {decks}")

    # Specify the name of the deck you want to fetch data from
    specific_deck_name = "Malay"  # Replace with the actual deck name

    if specific_deck_name in decks:
        # Get fields from the specific deck
        fields_list = get_fields_from_deck(specific_deck_name)

        # Print the fields
        # for fields in fields_list:
        #     print(fields)
    else:
        print(f"Deck '{specific_deck_name}' not found.")

x = []
def process_data(list):
    for fields in fields_list:
        if 'Front' in fields:
            x.append(fields['Front'])
    return x


current_word_bank = process_data(fields_list)

def lower_case(word):
    return word.lower()

def lower_list(list):
    b = []
    for word in list:
        b.append(lower_case(word))
    return b

word_bank = lower_list(current_word_bank)

def remove_duplicate_words(x,y):
    for words in y:
        if words in x:
            x.remove(words)
        else:
            continue
    return x

with open('nounlist.txt', 'r') as file:
    lines = file.readlines()

def list_to_words(list):
    string = ",".join(list)
    return string


def remove_parentheses(list):
    x = []
    for word in list:
        if "(" in word:
            x.append(remove(word))
        else:
            x.append(word)
    return x


def remove(word):
    x = word.find("(")
    y = word[:(x-1)]
    return y


words_to_learn = [line.strip() for line in lines]

final_words = remove_duplicate_words(words_to_learn,word_bank)

random_words = random.sample(final_words, 20)



print(final_words)




