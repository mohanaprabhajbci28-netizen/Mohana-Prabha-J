MyList1 = []
MyList2 = []

print("Enter 10 integers:")
numbers = [int(x) for x in input().split()]

for num in numbers:
    if num % 2 == 0 and num % 3 != 0:
        MyList1.append(num)
        
    if num % 9 == 0:
        MyList2.append(num)

print(*(MyList1))
print(*(MyList2))
