alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
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
    
print(encrypt(text, shift))
