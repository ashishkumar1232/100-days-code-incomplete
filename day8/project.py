alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
from art import logo
print(logo)
direction=input("enter 'encode' to encrypt and 'decode' to decrypt \n ")
text=input("enter the message \n").lower()
shift=int(input("enter the number of shift \n"))
def caesar(start_text,shift_amount,cipher_direction):
    if cipher_direction=="decode":
            shift_amount *= -1
    end_text=""
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"the {cipher_direction}d text is {end_text}")
shift=shift%26
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
# def encrypt(plane_text,shift_amount):
#     cipher_text=""
#     for letter in plane_text:
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"the encoded word is {cipher_text}")

# def decrypt(cipher_text,shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         plain_text+=alphabet[new_position]
#     print(f"the decoded text is {plain_text}")
    
# if direction=="encode":
#     encrypt(plane_text=text,shift_amount=shift)
# elif direction=="decode":
#     decrypt(cipher_text=text,shift_amount=shift)