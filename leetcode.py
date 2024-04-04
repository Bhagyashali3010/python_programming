# class Solution(object):
#      def climbStairs(self, n):
#         self.n=n
#         if n < 0:
#             return 0
#         elif n == 0 or n == 1:
#             return 1
#         elif n== 2:
#             print(2)
#         else:
#             fact = 1
#             while(n > 1):
#                 fact *= n
#                 n -= 1
#             # print (fact)
#             rfact= 1
#             while(n-2>1):
#                 rfact *= n
#                 n-=1
#             # print(rfact)
#             b = fact//(2*(rfact))
#             print(b)
# aa=Solution()
# x=int(input("enter:"))
# aa.climbStairs(x)

# # class Solution(object):
# #     def sum(self):
# #         num1=int(input("enter first integer:"))
# #         num2=int(input("enter second integer:"))
# #         num3=num1+num2
# #         print(num3)

# # aa=Solution()
# # aa.sum()   

# # nums=[1,2,3,4]
# # for i in range(len(nums)-1):
# #     print (nums)
# #     # nums[i]+=nums[i+1]
# # print (nums)

# # nums = [1, 2, 3, 4]
# # for i in range(len(nums) - 1):
# #     print(nums)
# #     nums[i] += nums[i + 1]
# # print(nums)

# n=15
# answer=[]
# for i in range (1,n+1):
#     if i%3==0 and i%5==0:
#         answer.append("FizzBuzz")
#     elif i%3==0:
#        answer.append("Fizz")
#     elif i%5==0:
#         answer.append("Buzz")
#     else:
#         answer.append(i)
# print(answer)

num=13
while num>0:
    if num%2==0:
        num1=num//2
        num==num1
        print(num)
    else:
        num1=num-1
        num==num1
        print(num)
