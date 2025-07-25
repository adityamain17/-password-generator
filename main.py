import random
import string

# Function to generate password
def generate_password(length=12, include_digit=True, include_symbol=True):
    # Start with letters
    characters = string.ascii_letters
    
    # Add digits if user wants
    if include_digit:
        characters += string.digits
    
    # Add symbols if user wants
    if include_symbol:
        characters += string.punctuation
    
    # Generate password using random characters
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Main function to interact with user
def main():
    print("Welcome to Advanced Password Generator!")
    
    # Ask user for password length
    length = int(input("Enter the length of password (e.g., 10): "))
    
    # Ask if digits should be included
    include_digit = input("Do you want to include digits? (yes/no): ").lower() == "yes"
    
    # Ask if symbols should be included
    include_symbol = input("Do you want to include symbols? (yes/no): ").lower() == "yes"
    
    # Generate the password
    password = generate_password(length, include_digit, include_symbol)
    
    # Show the password
    print("Generated Password:", password)

# Run main only if this file is executed directly
if __name__ == "__main__":
    main()
