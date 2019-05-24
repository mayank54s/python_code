c=int(input("Enter the no"))
a=0
b=1
i=2
print(a,b,sep='\n')
while i<=c:
    d=a+b
    a=b
    b=d
    print(d)
    i+=1
    

    