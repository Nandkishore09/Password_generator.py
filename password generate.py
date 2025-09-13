import random
import string

def generate_password(length): 
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    i = 0
    while i < length:   # conditional loop
        password += random.choice(chars)
        i += 1
    return password

while True:
    try:
        length = input("\nEnter password length (0 to exit): ")
                
        length = int(length)

        if length == 0:
            print("Exiting program... Goodbye!")
            break
        elif length < 8:
            print("Password length should be at least 8 characters!")
        else:
            print("Generated Password:", generate_password(length))

    except ValueError :
        print("Invalid choice! Please choose digit no:" )

