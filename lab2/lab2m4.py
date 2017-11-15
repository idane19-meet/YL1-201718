a = int(input("please enter a number: "))
b = []
x = 2
for i in range(a-2):
    b.append(x)
    x += 1
r = []
for l in b:
    if a%l == 0:
        r.append(l)
if len(r) == 0:
    print("this is a prime number!")
else:
    print("this is not a prime number!")
