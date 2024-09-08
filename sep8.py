# nums1 = [-1,3,0,0,0,0,0,0]
# m = 2
# nums2 = [0,0,0,1,2,3]
# n = 6
# for i in range (len(nums2)):
#     for j in range (len(nums1)):
#         if  nums2[i]<nums1[j]:
#             if nums2[i]==0 : 
#                 nums1.insert(j, nums2[i])
#                 nums1.pop(-1)
#                 m+=1
#                 break
#             else:
#                 nums1.insert(j, nums2[i])
#                 nums1.pop(-1)
#                 break

#         elif nums1[j]==0 and nums1[j-1]<=nums2[i] and j>=m:
#             # if nums2[i]!=0:
#                 # print(j)
#                 # print(nums1)
#             nums1.insert(j, nums2[i])
#             nums1.pop(-1)
#             print(nums1)
#             # else:
                
#             #     nums1.insert(j, nums2[i])
#             #     nums1.pop(-1)
#             #     m+=1
#             #     print(m)

#             if j==len(nums1)-1:
#                 pass
#             else:
#                 break
        
#         else:
#             pass
#     print(nums1)
        


nums1 = [-1,3,0,0,0,0,0,0]
m = 2
nums2 = [0,0,0,1,2,3]
n = 6
i=0
while m>0 and n>0:
    if nums1[m-1]>=nums2[n-1]:
        nums1[n+m-1]=nums1[m-1]
        m-=1
    else:
        nums1[n+m-1]=nums2[n-1]
        n-=1
print(nums1)