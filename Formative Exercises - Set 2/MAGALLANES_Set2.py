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

# Vigenere Cipher Problem

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

# Scytale Cipher Problem

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

