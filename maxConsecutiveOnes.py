# nums= [1,1,0,1,1,1]
# size=[]
# count=0
# for i in range (len(nums)):
#     if nums[i]==1:
#         count +=1 
#         i+=1
        
#     elif nums[i]==0:
#         i+=1
#         size.append(count)
#         # print(size)
#         count=0   
# print(max(size))
                
# nums=[22,345,2,6,7896]
# size=[]
# nos=0
# for i in range (len(nums)):
#     count=0
#     a=nums[i]
#     while a:
#         count+=1
#         a//=10
#         print(a)
#     size.append(count)
# print(size)
# for j in range(len(size)):
#     if size[j]%2==0:
#         nos+=1
# print(nos)


# nums = [-4,-1,0,3,10]
# a=[]
# for i in range (len(nums)):
#     if nums[i]<0:
#         nums[i]*=-1
#     else:
#         nums[i]=nums[i]
#     nums.sort()
# print(nums)

# for i in range(len(nums)-1):
#     for i in range(len(nums)-1):
#         if nums[i]>nums[i+1]:
#             temp=nums[i+1]
#             nums[i+1]=nums[i]
#             nums[i]=temp
#     print(nums) 


# arr = [1,0,0,3,0,4,5,0]
# a=[]
# for i in arr:
#     a.append(i)
#     if i==0:
#         a.append(0)
#         arr.pop(-1)
        
# print(a)
        
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# a=[]
# for i in nums1:
#     a.append(i)
#     if nums1[i]==0:
#         for j in nums2:
#             a.append(j)
#             nums1.pop(-1)
#     a.sort()
# print(a)

# nums=[-4,-1,0,3,10]
# for i in range (0,len(nums)):
#     if nums[i]<0:
#         nums[i]*=-1
#     else:
#         nums[i]=nums[i]
# print(nums)
# s=nums.sort()
# for i in range(0, len(nums)):
#     nums[i]*=nums[i]
# print(nums)


arr = [-2,0,10,-19,4,6,-8]
c=[]
count=0
for i in range(len(arr)):
    a=arr[i]+arr[i]
    if arr[i]%2==0:
        b=arr[i]//2
    else:
        b=None
    # print(a)
    # print(b)
    # for i in range(len(arr)):
    if arr[i]!=0:
        if a in arr or b in arr:
            c.append(1)
        else:
            c.append(0)
        # print(c)
    elif arr[i]==0:
        count+=1

if 1 in c or count==2:
    print(True)
else:
    print(False)