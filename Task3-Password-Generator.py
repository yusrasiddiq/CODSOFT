import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")

# Asking the user for the total length of the password
total_length = int(input("What should be the total length of your password?\n"))

# Asking the user if they want a complex password
while True:
    complex_password = input("Do you want a complex password with letters, symbols, and numbers? (yes/no)\n").lower()
    if complex_password in ['yes', 'no']:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

password_list = []

if complex_password =='yes':
    # Asking for the number of each type of character
    n_letters = int(input("How many letters do you want in your password?\n"))
    n_symbols = int(input("How many symbols do you want in your password?\n"))
    n_numbers = int(input("How many numbers do you want in your password?\n"))

    # Ensuring the total number of characters does not exceed the specified length
    while n_letters + n_symbols + n_numbers > total_length:
        print("The total number of letters, symbols, and numbers exceeds the specified length. Please try again.")
        n_letters = int(input("How many letters do you want in your password?\n"))
        n_symbols = int(input("How many symbols do you want in your password?\n"))
        n_numbers = int(input("How many numbers do you want in your password?\n"))

    # Adding random letters to the password list
    for i in range(n_letters):
        char = random.choice(letters)
        password_list.append(char)

    # Adding random symbols to the password list
    for i in range(n_symbols):
        symbol = random.choice(symbols)
        password_list.append(symbol)

    # Adding random numbers to the password list
    for i in range(n_numbers):
        number = random.choice(numbers)
        password_list.append(number)

    # Filling the remaining length with random letters if necessary
    while len(password_list) < total_length:
        password_list.append(random.choice(letters))

else:
    # If not a complex password, just fill the password with random letters up to the specified length
    for i in range(total_length):
        password_list.append(random.choice(letters))


# Shuffling the password list to randomize the order of characters
random.shuffle(password_list)

# Combining the list of characters into a single string
# password = "".join(password_list)
password =""
for i in password_list :
    password += i

# Printing the generated password
print(f"Your generated password is: {password}")
