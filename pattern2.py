# num=1
# for i in range (3):
#     for j in range (3):
#         print(num*num, end="\t ")
#         num+=1
#     print() 

# num=65
# for i in range (3):
#     for j in range (3):
#         print(chr(num), end=" ")
#         num+=1
#     print() 
        

# num=int(input("enter no.:"))
# a=num
# for i in range (4):
#     for j in range (4):
#         print(chr(num), end=" ")
#         num+=1
#     num=a
#     print() 

# num=1
# for i in range (3):
#     for j in range (3):
#         print((num*num)+1, end=" ")
#         num+=1
#     print()



# num=1
# for i in range (4):
#     for j in range (4):
#         if num%2!=0:
#             print((num*num), end=" \t")
#         else :
#             print(num, end ="\t ")
#         num+=1
#     print()


# for i in range (4):
#     for j in range (4):
#         print(i+1, end=" ")
#         i+=3
#     print()

# for i in range (4):
#     for j in range (4):
#         if j%2==0:
#             print("$", end=" ")
#         else :
#             print("=", end =" ")
#     print() 


# num=69
# for i in range (5):
#     for j in range (5):
#         print(chr(num), end=" ")
#         num-=1
#     num=69
#     print()


# num=65
# for i in range (3):
#     for j in range (3):
#         if num%2!=0:
#             print(chr(num), end =" ")
#         else :
#             print(chr(num+32), end=" ")
#         num+=1
#     print()

num=68
a=4
for i in range(4):
    for j in range (4):
        print((chr(num))+str(a), end="\t")
        num-=1
        a-=1
    num=68
    a=4
    print()

