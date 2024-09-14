nums = [0,0,1,1,1,1,2,3,3]
l=len(nums)
k=0
i=0
while i<l:
    if nums[i]==nums[i+1] and nums[i+1]==nums[i+2]:
      nums.remove(nums[i+2])
      nums.append('_')
      l-=1
    else:
      i+=1
unique=set(nums)
print((len(unique))-1)
print(nums) 
