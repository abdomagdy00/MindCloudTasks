import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

# Combine all character sets into a single pool for random selection
all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# ----------------------------------------------------
# 2. The Function Responsible for Generating the Password
# ----------------------------------------------------
def generate_secure_password(length):
    # The password must be at least 4 characters long to ensure one of each type is included
    if length < 4:
        return "Password length must be at least 4 characters."

    # Ensure at least one character from each type is included in the password
    password_list = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password's length with random characters from the combined pool
    for _ in range(length - 4):
        password_list.append(random.choice(all_characters))
        
    # Shuffle the list of characters to randomize their order
    random.shuffle(password_list)

    # Join the list into a single string and return it
    return "".join(password_list)

# ----------------------------------------------------
# 3. Main Program Part (User Interaction)
# ----------------------------------------------------
if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired password length (at least 4): "))
            
            # Check if the length is valid
            if password_length >= 4:
                # Call the function to generate the password and print it
                password = generate_secure_password(password_length)
                print("-" * 50)
                print(f"Successfully generated password: {password}")
                print("-" * 50)
                break  # Exit the loop after successful generation
            else:
                print("Error: Length must be an integer greater than or equal to 4.")
        except ValueError:
            print("Error: Please enter an integer.")