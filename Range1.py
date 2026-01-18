# for x in range(1,8):
#     # print(x)
#     if (x%2 == 0):
#         print(x)
#         if(x==4):
#             break

count=0
for number in range(1,10):
    if number%2==0:
        count +=1
        print(number)
print(f"This is end of {count} for loop")