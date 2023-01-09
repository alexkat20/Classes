l = int(input())
w = int(input())
x = int(input())
y = int(input())


if l > w:
    x2 = w - x
    y2 = l - y
else:
    x2 = l - x
    y2 = w - y
print(min((x2, y2, x, y)))
