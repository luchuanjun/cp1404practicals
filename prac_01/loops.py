#Odd numbers between 1 and 20
print("Odd numbers from 1 to 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#count down from 20 to 1
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#print n stars on one line
print("c. Print n stars:")
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

#print n lines of increasing stars
print("d. Print n lines of increasing stars:")
for i in range(1, n + 1):
    print('*' * i)
