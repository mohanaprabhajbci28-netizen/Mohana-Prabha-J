a=int(input("enter the sub 1 marks:"))
b=int(input("enter the sub 2 marks:"))
c=int(input("enter the sub 3 marks:"))
d=int(input("enter the sub 4 marks:"))
tot=a+b+c+d
print("total is",tot)
avg=tot/4
print("average is",avg)
if(avg>75):
    print("Distincton")
elif(avg>=60 and avg<75):
    print("first class")
elif(avg>=50 and avg<60):
    print("second class")
elif(avg>=40 and avg<50):
    print("third class")
else:
    print("fail")
    
