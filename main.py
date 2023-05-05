import art

# Print the logo
print(art.logo)

# Define the alphabet list
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Define the function for the Caesar Cipher
def caesar_cipher(text, shift, direction):
  shift = shift % 26 # Shift should always be in the range of 0-25
  crypted_msg = ""
  if (direction == "decode"): shift *= -1 # If decoding, shift in the opposite direction
  for char in text:
    if char in alphabet:
        crypted_msg+= alphabet[alphabet.index(char) + shift] # Shift the character and add to the result
    else:
      crypted_msg += char # If not a character, don't shift and add to the result
  print(f"\nThe {direction}ed message is: {crypted_msg}.")

# Loop until the user no longer wants to encrypt/decrypt messages
encrypt_more = True
while encrypt_more:
  
    # Get user input for direction, text, and shift
    direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n\n")
    text = input("\nType your message:\n\n").lower()
    shift = int(input("\nType the shift number:\n\n"))
    
    # Call the caesar_cipher function with the user input and print the result
    caesar_cipher(text, shift, direction)
    
    # Ask the user if they want to encrypt/decrypt more messages
    play_again = input(("\nDo you want to decode/encode more messages? (Y/N)\n\n").lower())
    
    # If user does not want to encrypt/decrypt more messages, exit the loop and print a goodbye message
    if play_again == "n":
      encrypt_more = False
      print("\n\nSee you later, have a nice day!")
    else:
      encrypt_more = True # Otherwise, continue looping
