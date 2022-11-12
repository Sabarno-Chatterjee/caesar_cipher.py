import art

print(art.logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
encrypt_more = True

def caesar_cipher(text, shift, direction):
  shift = shift % 26
  crypted_msg = ""
  if (direction == "decode"): shift *= -1 
  for char in text:
    if char in alphabet:
        crypted_msg+= alphabet[alphabet.index(char) + shift]
    else:
      crypted_msg += char
  print(f"\nThe {direction}ed message is: {crypted_msg}.")

while encrypt_more:
  
    direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n\n")
    text = input("\nType your message:\n\n").lower()
    shift = int(input("\nType the shift number:\n\n"))
    
    caesar_cipher(text, shift, direction)
    play_again = input(("\nDo you want to decode/encode more messages? (Y/N)\n\n").lower())
    
    if play_again == "n":
      encrypt_more = False
      print("\n\nSee you later, have a nice day!")
    else:
      encrypt_more = True