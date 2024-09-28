# nums = [3,2,3,3,4,8,4]
# n=len(nums)
# a={}

# for i in nums:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
    

# # a[nums[i]]=c
# print(a)

# m=max(a,key=a.get)

# print(m)

# 2
# nums=[1,2,3]
# arr=set(nums)
# for i in range (0,len(nums)):
#     if nums[i]==arr[i]:
#         print('okk')

# 3
nums = [1,2,3,4,5,6,7]
n=len(nums)
print(n)
k=3

# for j in range(k):
#     a=nums[n-1]
#     for i in range (n-1,-1,-1):
#             # a=nums[n-1]
#             # print(nums[n-1])
#             if i==0:
#                 nums[0]=a
#             else:
#                 nums[i]=nums[i-1]
        
    # else:
    #     nums[i]=nums[i+1]
# print(nums)

for i in range(n-1,k,-1):
    a=nums[i]
    while i>k:
        nums.remove(nums[i])
        nums.insert(0,a)
        print(nums)