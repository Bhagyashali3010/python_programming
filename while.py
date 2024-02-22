# num =0
# count = 0
# while (count<7):
#     num+=1
#     if num%2!=0:
#         count+=1
        
# print (num)    

# a=int(input ("enter a no.:"))
# b=1
# while (a>0):
#     b*=a
#     a-=1
# print(b)

# num=int(input("enter a no.:"))
# count=0
# while (count<10):
#     print (num-1)
#     count+=1
#     num=num-1
#     if count==10:
#         break

# num=int(input ("enter a no.:"))
# b=num
# last=num*11
# while(num<last):
#     print(num,end=" ")
#     num+=b
    

# num=int(input("enter position :"))
# count=0
# i=1
# while (i<(2*num+1)):
#     if i%2==0:
#         count+=1 
#         if count==num:
#             print(i)
#     i+=1


# num=int(input("enter the no.:"))
# sum=0
# while(num>0):
#     sum+=num
#     num-=1
# print(sum)


# num=int(input("enter no.:"))
# i=1
# sum=0
# while (i<(num+1)):
#     if i%2==0:
#         sum+=i
#         print(sum*sum, end=" ")
#     i+=1
#     sum=0


num=int(input("enter a no.:"))
cube=0
i=num
while (0<i<num+1):
    if i%2!=0:
        cube+=i
        print(cube*cube*cube, end=" ")
    i-=1
    cube=0
        
        
          

    
