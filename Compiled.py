import random
import smtplib
import time
import schedule
import requests
import json

# I created this project in order to help assist my Malay language learning
# flashcards in Anki.

# The goal of This project was to create an automated emailing system that will
# send 20 random new english words to learn every day to the recipient email.

# The word bank of words that gets sent has to be filtered from words
# already in the anki deck of words in order to reduce redundancy


# Used to retrieve Card Deck information from Anki
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

    specific_deck_name = "Malay"

    if specific_deck_name in decks:
        # Get fields from the specific deck
        fields_list = get_fields_from_deck(specific_deck_name)

        # Print the fields
        # for fields in fields_list:
        #     print(fields)
    else:
        print(f"Deck '{specific_deck_name}' not found.")

# Turns the first word from every dictionary pair into a list of words
def process_data(list):

    x = []

    for fields in fields_list:
        if 'Front' in fields:
            x.append(fields['Front'])
    return x

# Our current word bank of words in Anki
unfiltered_word_bank = process_data(fields_list)


# Makes every word in the list to lower case
def lower_list(list):

    b = []

    for word in list:
        b.append(word.lower())
    return b

word_bank = lower_list(unfiltered_word_bank)


# Removes duplicate words from our current word bank to
# the bank of words we want to learn from
def remove_duplicate_words(x,y):
    for words in y:
        if words in x:
            x.remove(words)
        else:
            continue
    return x


# Opens a text file of list of words to learn from found on GitHub
with open('nounlist.txt', 'r') as file:
    lines = file.readlines()

def list_to_words(list):
    for word in list:
        print(word)

def list_to_words(list):
    string = "\n".join(list)
    return string


# Function that helps remove the parentheses that were in some
# currently existing words like "Love (Deep)"
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

word_bank_no_parantheses = remove_parentheses(word_bank)

final_words = remove_duplicate_words(words_to_learn,word_bank_no_parantheses)

# Gets a random sample of 20 words from our final words that have been completely processed

random_words = random.sample(final_words, 20)


# Function that runs the automated email sending

sender_email = 'bwong@student.dalat.org'
sender_password = 'uhqe nvef qoij wekp'
recipient_email = 'benjamin02615@gmail.com'

def send_email():
    subject = '20 Words of The Day!'
    body = list_to_words(random_words)

    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

schedule.every().day.at('14:20').do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
