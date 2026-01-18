#PrimeNyumber Code

StartNumber = input("Enter Your Number" + ">")
EndNumber= input("Enter Your Last Number" + ">")
c=int(1)
primeNumber = "Prime Number:"
# d=int(0)
for a in range(int(StartNumber),int(EndNumber)+1,1):   
    b= int(2)
    d=int(0)
   
    for b in range(b,int(StartNumber)+1,1):
        
        if(int(StartNumber) % b)==0:
            d=d+1
        b=b+1
    
    if(d==1):
        primeNumber = primeNumber + str(StartNumber) + "," 
    
    StartNumber=int(StartNumber)+1     
   
print(primeNumber)   
    # print("b="+str(b))
    # print("c="+str(c))
    