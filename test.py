# fact=6
# b = fact/(2*(fact-2))
# print(b)

# nums = [1,1,1,1,1]
# for i in range(len(nums)):
#     if i==0:
#         nums[0]=nums[0]
#     else:
#         nums[i]+=nums[i-1]
# print(nums)


# accounts=[[1,5],[7,3],[3,5]]
# aa=[]
# for i in range (len(accounts)):
#     sum = 0
#     print(accounts[i])
#     for j in range(len(accounts[i])):
#         print(accounts[i][j])
#         sum = sum + accounts[i][j]
#     print(sum)
#     aa.append(sum)
#     print(aa)
# print(max(aa))


# num=14
# count=0
# while num>0:
#     if num%2==0:
#         num1=num//2
#         num=num1
#         count+=1
#     else:
#         num1=num-1
#         num=num1
#         count+=1
# print(count)

head={1,2,3,4,5}
arr=[]
len=0
while (head!=None):
    arr.append(head)
    head=head.next
    len+=1
    print (len)