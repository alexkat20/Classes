"""
Write a program  which prints the deci
mal part of a number. If
decimal part is zero, the program should return
this string: "INTEGER".
"""

a = float(input())

if a % 1 > 0:
    print(f'{a % 1}')
else:
    print('INTEGER')
