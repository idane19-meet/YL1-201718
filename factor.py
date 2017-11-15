a = int(input("please enter a number: "))
list1 = []
i = 1
for i in range(a):
    i +=1
    list1.append(i)
number = 1
for j in list1:
    number *= j
print("the factorial of " +str(a) +" is: " + str(number))

