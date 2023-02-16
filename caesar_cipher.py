alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    # Initialize an empty string to store the encrypted text
    cipher_text = ""
    for letter in text:
        # Check if the letter is in the alphabet
        if letter in alphabet:
            # Get the index of the letter in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position after shifting by the given amount
            new_position = (position + shift) % len(alphabet)
            # Add the shifted letter to the cipher text
            cipher_text += alphabet[new_position]
        else:
            # Add non-letter characters to the cipher text as is
            cipher_text += letter
    # Return the encrypted text
    return cipher_text

#creating a decipher function

def decrypt(plain_text, shift_amount):
    # Initialize an empty string to store the encrypted text
    decipher_text = ""
    for letter in text:
        # Check if the letter is in the alphabet
        if letter in alphabet:
            # Get the index of the letter in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position after shifting by the given amount
            new_position = (position - shift) % len(alphabet)
            # Add the shifted letter to the cipher text
            decipher_text += alphabet[new_position]
        else:
            # Add non-letter characters to the cipher text as is
            decipher_text += letter
    # Return the encrypted text
    return decipher_text

#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable.
if direction == "encode":
  print(f"your encoded message is:\n{encrypt(plain_text=text, shift_amount=shift)}")
elif direction == "decode":
  print(f"your decoded message is:\n{decrypt(plain_text=text, shift_amount=shift)}")
else:
  print("Please enter a valid form of operation by typing wither encode or decode")
