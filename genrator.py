import random
import string

def generate_password(length):
    # Define characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length for your password (min 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
            else:
                return length
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the Password Generator!")

    # Get desired password length from the user
    length = get_password_length()

    # Generate password
    password = generate_password(length)

    # Display the generated password
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
