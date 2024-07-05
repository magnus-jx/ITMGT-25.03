#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Shift Letter Problem

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    elif not letter.isalpha():
        return "The input is not an alphabetical letter."
    else:
        letter = letter.upper()
        for char in letter:
            if 'A' <= char <= 'Z':
                shifted_letter = chr(ord("A") + (ord(char) - ord("A") + shift) % 26)
        return shifted_letter

# Caesar Cipher Problem

def caesar_cipher(message, shift):
    message = message.upper()
    output = ""
   
    for char in message:
        if not char.isalpha():
            output += char
            continue
        shifted_letter = chr(ord("A") + (ord(char) - ord("A") + shift) % 26)
        output += shifted_letter
    
    return output

# Shift by Letter Problem

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    elif not letter.isalpha():
        return "The input is not an alphabetical letter."
    else:
        letter = letter.upper()
        letter_shift = ord(letter_shift.upper()) - ord("A")
        for char in letter:
            if 'A' <= char <= 'Z':
                shifted_letter = chr(ord("A") + (ord(char) - ord("A") + letter_shift) % 26)
        return shifted_letter

# Vigenere Cipher Problem

def vigenere_cipher(message, key):
    message = message.upper()
    key = key.upper()
    output = ""
    key_index = 0
    key_length = len(key)
    
    for real_char in message:
        if not real_char.isalpha():
            output += real_char
            key_index = (key_index + 1) % key_length
            continue
        transformed_char = chr(ord("A") + (ord(real_char) + ord(key[key_index]) - (2 * ord("A"))) % 26)
        output += transformed_char
        key_index = (key_index + 1) % key_length
        
    return output

# Scytale Cipher Problem

def scytale_cipher(message, shift):
    message = message.upper()
    message_index = 0
    message_length = len(message)
    output = ""
    
    while message_length % shift != 0:
        message += "_"
        message_length = len(message)
    
    while message_index < message_length:
        transformed_char = message[((message_index // shift) + (message_length // shift) * (message_index % shift))]
        output += transformed_char
        message_index += 1
        
    return output

# Syctale Decipher Problem

def scytale_decipher(message, shift):
    message = message.upper()
    message_index = 0
    message_length = len(message)
    output = ""
    
    while message_index < message_length:
        transformed_char = message[(message_index // (message_length // shift) + (message_index % (message_length // shift)) * shift)]
        output += transformed_char
        message_index += 1
        
    return output

