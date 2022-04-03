alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'w', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'w', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input('Type your message:\n').lower()
shift = int(input("Enter the shift number:\n"))

# Todo-1: Create a function called 'encrypt' that takes the text and shifts as inputs
def encrypt(action, message, shifting):
    ceasar_cipher = ""
    for letter in text:  #loop through each of the letters in text
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        ceasar_cipher += new_letter
    print(f"The encoded text is {ceasar_cipher}")
    

# Todo-2: Inside the encrypt function , shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text
# e.g 
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print_output = "The encrpted text is mjqqt"


def decrypt(message, shifting):
    ceasar_cipher = ""
    for letter in text:  #loop through each of the letters in text
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        ceasar_cipher += new_letter
    print(f"The decoded text is {ceasar_cipher}")
    


if direction == "encode":
    encrypt(message=text, shifting=shift)

elif direction == "decode":
    decrypt(message=text, shifting=shift)

else:
    print("invalid input, Pls try again")




# cobining encrypt and decrypt function into one funtion called caesar
def caesar(message, shift_amount):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    final_text += alphabet[new_position]
print(f"the {direction}d text is {final_text}")
