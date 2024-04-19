arr = [1,0,2,3,0,4,5,0]
a=[]
# for i in arr:
#     a.append(i)
#     if i==0:
#         a.append(0)
#         arr.pop(-1)
# print(a)
b=len(arr)
print(b)
for i in range(len(arr)):
    if arr[i]!=0:
        a.append(arr[i])
    elif arr[i]==0:
        a.append(arr[i]) 
        a.append(0) 
        arr.pop(-1)
    print(a)
        

# nums1 = [1,2,3,0,0,0]
# m = []
# nums2 = [2,5,6]
# n = 3
# for i in nums1:
#     if i==0:
#         for j in nums2:
#             m.append(j)
#             nums1.pop(-1)
#     else:
#         m.append(i)
#     print(m)



# nums = [2, 1, 2, 2, 4]
# val = 2
# count = 0
# a = len(nums)
# i = 0

# while i < a:
#     if nums[i] == val:
#         nums.remove(val)
#         a -= 1
#         nums.append('_')
#     else:
#         i += 1
#         count += 1

# print(count)
# print(nums)
# b=[]
# for i in range (len(nums)):
#     if nums[i]!=val:
#         count+=1
#         b.append(nums[i])
#     else:
#         nums.remove(val)
# print(count)
# print(b)
# print(nums)
