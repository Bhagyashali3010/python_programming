# # arr = [57010,71840,69871,14425,70605]
# # n=len(arr)
# # for i in range(n-1, -1,-1):
# #     if i==n-1:
# #         a=arr[i]
# #         arr[i]=-1
# #     elif i==n-2:
# #         b=arr[i]
# #         arr[i]=a
# #     else:
# #         if a<b:
# #             if b>arr[i]:
# #                 arr[i]=b
                
# #             else:
# #                 max=arr[i]
# #                 arr[i]=b
# #                 b=max
# #         else:
# #             if a>arr[i]:
# #                 arr[i]=a
                
# #             else:
# #                 max=arr[i]
# #                 arr[i]=a
# #                 a=max
# # print(arr)



# #2
# nums=[1,1,1,1,1,1]
# n=len(nums)
# print(n)
# i=0
# count=0
# if n==1:
#     count=1
# elif nums[0]==nums[n-1]:
#     count=1
#     for i in range(n-1,0,-1):
#         nums.remove(nums[i])
# #     if nums[0]==nums[1]:
# #         count=1
# #         nums.remove(nums[1])
# #     else:
# #         count=2
# else:
#     while i<n:
#         if nums[i]==nums[i-1]:
#             nums.remove(nums[i-1])
#             print(nums)
#             # i+=1
#             # count+=1
#             n-=1
#         else:
#             i+=1
#             count+=1
# print(count)
# print(nums)


# nums = [0,1,0,3,0,9]
# a=len(nums)
# i=0
# while i<a:
#     if nums[i]==0:
#         print(nums)
#         nums.remove(nums[i])
#         print(nums)
#         a-=1
#         print(a)
#         nums.append(0)
       
#     else:
#         i+=1
# print(nums)



nums = [0]
# even=0
# odd=0
i=0
a=len(nums)
while i<a:
    if nums[i]%2!=0:
        b=nums[i]
        nums.remove(nums[i])
        a-=1
        nums.append(b)
    else:
        i+=1
    print(nums) 
