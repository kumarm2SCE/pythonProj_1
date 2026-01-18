print(''' ********** This is Calculator ********\n''')
print('''Start of your calculator''')
print('''
        For add enter: +
        For multiplication: *
        For division: % 
        For substraction: -       
''')
a=int(input("Enter your 1st Num:"))
b=int(input("Enter your 2nd Num:"))
c=str(input("Enter your operation"))
if(c=="+"):
    print(a+b)
elif(c=="*"):
    print(a*b)
elif(c=="-"):
    if(a>b):
        print(a-b)
    else:
        print(b-a)    
elif(c=="%"):
    if(a>b):
        print(a/b)
    else:
        print(b/a)
else:
    print("defaul no operation")