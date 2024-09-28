n=7
nums=[3,5,2,3,8,7,1]
arr=[]
i=0
count={}
if n%2==0:
    while i<n//2:
        a=max(nums)
        b=min(nums)
        c=a+b
        nums.remove(a)
        nums.remove(b)
        arr.append(c)
        i+=1
    print(arr) 
else:
    while i<((n//2)+1):
        if i==0:
            a=max(nums)
            arr.append(a)
            i+=1
        else:
            a=max(nums)
            b=min(nums)
            c=a+b
            arr.append(c)
            i+=1
    print(arr)

for i in range (len(arr)) :
    d=arr.count(arr[i])
    count[arr[i]]=d
print(max(count, key=count.get))
