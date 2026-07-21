import random
import string

# Characters to use in the password
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

def generate_password(length=12):
    # Combine all character types
    all_chars = letters + numbers + symbols

    # Ensure at least one character from each category is included
    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))

        if length < 3:
            print("Password length must be at least 3.")
        else:
            pwd = generate_password(length)
            print(f"\nGenerated Password: {pwd}")
            print("Strength Tip: Use 12+ characters for better security.")

    except ValueError:
        print("Please enter a valid number.")