#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Binary to Base-10 Conversion Problem

def bin_to_dec(binary_str):

    text_str = str(binary_str)
    converted_number = 0
    
    for i in range(len(text_str)):
        converted_number += int(text_str[-(i + 1)]) * (2 ** i)

    return converted_number

# Base-10 to Binary Conversion Problem

def dec_to_bin(number):

    converted_number = ""
    
    while number > 0:
        remainder = number % 2
        converted_number += str(remainder)
        number //= 2

    return converted_number[::-1]

# Telephone Cipher Problem
    
def telephone_cipher(message):

    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
    
    encoded_string = ""
    
    for i in range(len(message)):
        
        current_char = message[i]

        encoded_string += encoder_dict[current_char]
        
        if i + 1 < len(message):
            next_char = message[i + 1]

            if next_char in encoder_dict and encoder_dict[current_char][0] == encoder_dict[next_char][0]:
                encoded_string += "_"

    return encoded_string

# Telephone Decipher Problem

def telephone_decipher(message):

    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    
    decoded_string = ""
    encoded_character = ""

    for i in range(len(message)):
        if message[i] == '_':
            if encoded_character:
                decoded_string += decipher_dict[encoded_character]
                encoded_character = ""
        else:
            if encoded_character and message[i] != encoded_character[-1]:
                decoded_string += decipher_dict[encoded_character]
                encoded_character = message[i]
            else:
                encoded_character += message[i]

    if encoded_character:
        decoded_string += decipher_dict[encoded_character]

    return decoded_string

