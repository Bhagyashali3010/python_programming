# def outer():
#     def inner():
#         return "hello , inner"
#     return inner()

# ans = outer()
# print(ans)


# def outer():
#     def inner():
#         return "hello , inner"
#     return inner()

# ans = outer()
# rein = ans()
# print(rein)    

# def fact(ele):
#     facto=1
#     for i in range (1, ele+1):
#         facto*=i
#     return facto

# print((fact(1)), end=" ")
# print((fact(2)), end=" ")
# print((fact(3)), end=" ")
# print((fact(4)), end=" ")
# print((fact(5)), end=" ")
# print((fact(6)), end=" ")


lst=[]
n=int(input("enter no. of elements:"))
for i in range (1, n+1):
    ele= int(input())
    lst.append(ele)
print(lst)

def fact(ele):
    facto=1
    for i in range (1, ele+1):
        facto*=i
    return facto

lst1 =[]
for x in range (0, n):
    no=fact(lst[x])
    
    lst1.append(no)
    x+=1
print(lst1)


# lst=[]
# n=int(input(" no. of elements:"))
# for i in range (1, n+1):
#     ele=int(input())
#     lst.append(ele)
# print(lst)
# m=int(input("enter the element to be count:"))


# def search(lst,n, m):
#         count=lst.count(m)
            
#         return count

# bb=search(lst, n, m)
# print(bb)


# count=0
# num=12345

# def parent():
    
#     def digitcount():
    #     count=0
    #     # num= int(input())
    #     num=12345
    #     while num>0:
    #         num//=10
    #         count+=1
    #     print ("the count of digits is:" ,count)
    # def evendigitcount():
    #     count=0
    #     # num= int(input())
    #     num=12345
    #     lst=map(int, str(num))
    #     for i in lst:
    #         if i%2==0:
    #             count+=1
    #             i+=1
    #     print ("the count of even digits is:",count)
    # def odddigitcount():
    #     count=0
#         # num= int(input())
#         num=12345
#         lst1=map(int, str(num))
#         for i in lst1:
#             if i%2!=0:
#                 count+=1
#         print ("the count of odd digits is:",count)
#     digitcount()
#     evendigitcount()
#     odddigitcount()

# print("first of all")
# parent()



def find():
        lst=[]
        n=int(input("enter njo. of element:"))
        for i in range(0, n):
            ele=int(input())
            lst.append(ele)
        print(lst)
        a=int(input("enter the element to be found:"))
        for i in range(n):
             if (lst[i]==a):
                 print("teh element is at index:",i)         
        return -1
def parent():
    def myindex():
        print("inside the my index block")
        find()
         
    def mypalindrome():
            print("inside the my palindrome block")
            find()
    if c==1:
        myindex()
    elif c==2:
        mypalindrome()

c=int(input("enter the choice:"))
parent()

    

