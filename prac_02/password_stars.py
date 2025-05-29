def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Enter password: ")
    while len(password) < 5:
        print("Password too short! Please enter at least 5 characters.")
        password = input("Enter password）: ")
    return password

def print_asterisks(password, symbol='*'):
    print(symbol * len(password))

if __name__ == '__main__':
    main()

