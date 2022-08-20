# get user input
from random import triangular


rows = int(input("Please enter your lucky number: "))

# upper upfront pyramid
for i in range(1, rows + 1):
    # print starting spaces
    for j in range(1, rows - i + 1):
        print(end = ' ')

    # print right number triangle
    for k in range(1, 2*i, 2):
        print(k, end = '')

    # print left reverse alphabet triangle
    for l in range(i-1, 0, -1):
        print(chr(64+l), end = '')
    
    print()

# lower downback reverse pyramid
for i in range(rows - 1, 0, -1):
    # print starting spaces
    for j in range(1, (rows - i + 1)):
        print(end = ' ')

    # print right reverse number triangle
    for k in range(1, 2*i, 2):
        print(k, end = '')

    # print left reverse alphaber reverse triangle
    for l in range(i-1, 0, -1):
        print(chr(64+l), end = '')
        
    print()
