n=5
for i in range(n):
    for j in range(n):
        if((i in {0,4}) and j in{1,2,3}):
            print("*", end=" ")
        elif(i in {1,2,3} and j in {0,4}):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
