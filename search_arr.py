# arr = [3,1,7,11]
# c=[]
# for i in arr:
#     a=i*2
#     if i%2==0:
#         b=i/2
#     for j in arr:
#         if j==a or j==b:
#             c.append(j) 
#         # else :
#         #     pass
       
# if len(c)==0:
#     print(False)
# else:
#     print(True)


# arr = [3,5,5]
# b=len(arr)
# a=(b//2)
# print(a)
# e=arr[a]
# print(e)
# if len(arr)<3 :
#     print("not a mountain")
# else:
    # for i in range(0,a-1):
    #     for j in range(a+1,b-1):
    #         if arr[j]>arr[j+1]:
    #             flag=1
    #         if arr[i]<arr[i+1] :
    #             flag1=1
    #         else:
    #             flag=0
    # if flag==1 and flag1==1:
    #     print("ture")
    # else : 
    #     print("false")      


arr=[3,6,5,6,7,6,5,3,0]
m=max(arr)
# print(m)
a=arr.index(m)
# print(a)
n=len(arr)

# i=0
if len(arr)<3:
    result1 = False
elif a==n-1:
    result1 =False
elif a==0:
    result1 =False
else:
    for i in range(a-1,-1,-1):
        print(arr[i])
        if arr[i]>=arr[i+1]:
            result1 = False
            break
        else:
            result1 = True

    for i in range(a+1,n,1):
        print(arr[i])
        if arr[i]>=arr[i-1]:
            result2 = False
            break
        else:
            result2 = True
if(result1 and result2):
    print("true")
else:
    print("false")





    
        
        

