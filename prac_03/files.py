name = input("Enter your name: ")
name_file = open('name.txt', 'w')
name_file.write(name)
name_file.close()

name_file = open('name.txt', 'r')
stored_name = name_file.read()
name_file.close()
print(f"Hi {stored_name}!")

with open('numbers.txt', 'r') as file:
    first = int(file.readline())
    second = int(file.readline())
print(first + second)  # 应该是59

total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
         total += int(line.strip())
print(total)
