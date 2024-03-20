def encode(password):
    encoded = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded

def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == '2':
            # Placeholder for decode
            print("Decode functionality not implemented yet.")
        elif option == '3':
            break  # Exit
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
