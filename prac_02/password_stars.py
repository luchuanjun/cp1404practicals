def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("请输入密码（Enter password）: ")
    while len(password) < 5:
        print("密码太短！请输入至少5个字符。（Password too short! Please enter at least 5 characters.）")
        password = input("请输入密码（Enter password）: ")
    return password


def print_asterisks(password, symbol='*'):
    print(symbol * len(password))



if __name__ == '__main__':
    main()

