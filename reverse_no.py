i=int(input("Enter the  value of i"))
n=0
a=i
b=i
c=0
while(i>0):
    i=i//1
    c=c+1
print(c)

i=a
while(i>0):
    i=i//10
    c=c+i*pow(10,n-1)
    n+=1
print(c)
    
    
    

    

