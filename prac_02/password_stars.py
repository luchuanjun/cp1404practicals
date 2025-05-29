def main():
    password = get_password()
    print_asterisks(password)

# 获取用户输入密码的函数
def get_password():
    password = input("请输入密码（Enter password）: ")
    while len(password) < 5:
        print("密码太短！请输入至少5个字符。（Password too short! Please enter at least 5 characters.）")
        password = input("请输入密码（Enter password）: ")
    return password

# 打印星号的函数，可选参数symbol默认为 *
def print_asterisks(password, symbol='*'):
    print(symbol * len(password))


# 主函数入口
if __name__ == '__main__':
    main()

