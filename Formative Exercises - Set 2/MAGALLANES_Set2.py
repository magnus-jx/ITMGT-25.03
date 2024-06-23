#!/usr/bin/env python
# coding: utf-8

# ### Exercise 1: Shift Letter Problem

# In[42]:


letter = str(input("Enter a letter you want to shift: "))
shift = int(input("Enter a value you want to shift the letter with: "))

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
        
print(shift_letter(letter, shift))


# ### Exercise 2: Caesar Cipher Problem

# In[52]:


message = str(input("Enter a string you want to shift: "))
shift = int(input("Enter a value you want to shift the string with: "))

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

print(caesar_cipher(message, shift))


# ### Exercise 3: Shift by Letter Problem

# In[61]:


letter = str(input("Enter a letter you want to shift: "))
letter_shift = str(input("Enter a letter representing the number you want to shift the letter with: "))

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
        
print(shift_by_letter(letter, letter_shift))


# ### Exercise 4: Vigenere Cipher

# In[23]:


message = str(input("Enter a string you want to shift: "))
key = str(input("Enter a string you want to shift the earlier string with: "))

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

print(vigenere_cipher(message, key))


# ### Exercise 5: Scytale Cipher

# In[47]:


message = str(input("Enter a string you want to shift: "))
shift = int(input("Enter a value you want to shift the string with: "))

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

print(scytale_cipher(message, shift))


# ### Exercise 6: Scytale Decipher

# In[105]:


message = str(input("Enter a string you want to decipher: "))
shift = int(input("Enter a value you want to shift the string back to: "))

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

print(scytale_decipher(message, shift))

