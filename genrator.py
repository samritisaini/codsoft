import random
import string

def generate_password(length):
    # Define characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    # Take user input for desired password length
    length = int(input("Enter the desired length for your password: "))

    # Generate password
    password = generate_password(length)

    # Display the generated password
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
