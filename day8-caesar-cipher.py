# today we will be building an encripter, that will allow us to encrypt and decrypt our messages

# defining some variables

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# create the funcions that will allow us to encode and decode the message

def encrypt(text, shift):
    
    encrypted_text = ""

    for char in text:
        if alphabet.count(char) == 0:
            encrypted_text += char

        else:    
            index = alphabet.index(char)
            index += shift
            encrypted_text += alphabet[index]

    print(f"Your encrypted text is:\n{encrypted_text}")

def decrypt(text, shift):
    
    decrypted_text = ""

    for char in text:
        if alphabet.count(char) == 0:
            decrypted_text += char

        else:    
            index = alphabet.index(char)
            index -= shift
            decrypted_text += alphabet[index]

    print(f"Your decrypted text is:\n{decrypted_text}")

# execute the cipher; we will do it in a way that the customer decide when to leave the program

keep_using = "yes"

print("Welcome to the Ceaser Cipher encrypter, your solution to share secret war information!")

while keep_using == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while direction != "encode" and direction != "decode":
        direction = input("Please, introduce a valid word. Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        print(direction)

    if direction == "encode":

        text = input("Type your message to encode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        encrypt(text, shift)

    else:

        text = input("Type your message to decode:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        decrypt(text, shift)

    keep_using = input("Type 'yes' if you want to encrypt or decrypt other message:\n").lower()

print("Thanks for using this revolutionary method, I will be ready to encrypt your next conspiration plans! :)")





    
