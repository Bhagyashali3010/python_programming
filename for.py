
# for i in range (101):
#     print(i, end=" ")


# for i in range (100, 111):
#     print (i)


# for i in range (1, 101):
#     if (i%2==0):
#         print(i)



# for i in range (1, 101):
#      if (i%2!=0):
         
#          print(i)


# for i in range (100 , 1, -1):
#     print (i)

# a=12
# b= 12
# for i in range (1, 11):
#      print(a,"*",i ,"=",b)
#      b+=12


# a=12
# b=120
# for i in range (10 , 0, -1):
#     print (a,"*",i ,"=",b)
#     b-=12

# sum=0
# for i in range (11):
    
#     sum=sum+i
# print(sum)


# a=10
# while (a>0):
#     print(a)
#     a-=1

# i=0
# n=int(input("enter number:"))
# sum=0
# while (i<(2*n+1)):
#     if i%2==0:
#         sum=sum+i
#     i+=1    
# print(sum)   

# for i in range(21,3,2):
#     print(i)
# i=1
# while(i<15):

# x,y,z=10,20,30
# print(x,y,z)
# d=8/2
# print(d)

# a=1,2,3,30
# print(type(a))


# i=0
# a= int(input("enter no:"))  !!!!!!!!!!!
# sum=0
# while (i<(2*a+1)):
#     if i%2==0:
#         sum+=i
#     i+=1
      
#     print(sum)    


# i=1
# count= 0
# while (count<7):
#     if i%2!=0:
#         count+=1
#         if count==7 :
#             print("7th no. is",i)
#     i+=1


# a=1
# b=1
# while (a<7):
#     print(b)
#     if b%2!=0:
#         b+=b
#     a+=a
#     if a==7:
#         print(b)


count_odd=0
num=0
while (count_odd<7):
    num+=1
    if num % 2 != 0:
        # print(num)
        count_odd+=1
print(num)