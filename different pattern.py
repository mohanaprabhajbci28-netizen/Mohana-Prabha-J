n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for i in range(n-i):
        print("*", end=" ")
    print()
        
