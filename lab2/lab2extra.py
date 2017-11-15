b = int(input("number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = []
for i in a:
    if i < b:
        c.append(i)
print(c)
