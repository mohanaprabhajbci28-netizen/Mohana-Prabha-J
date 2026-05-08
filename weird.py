def num(n):
    n=int(input("enter  a number:"))
    if((n%2!=0) or (n%2==0 and 6<=n<=20)):
        print("weird")
    else:
        print("not weird")
return num
