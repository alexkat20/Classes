a = int(input())
b = int(input())
c = int(input())

if (a + b) % 2 != 0:
    print('yes')
elif (a + c) % 2 != 0:
    print('yes')
elif (c + b) % 2 != 0:
    print('yes')
else:
    print('no')
