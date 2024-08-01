# r=int(input("enter r="))
# unit=int(input("enter unit="))
# n=int(input("enter n="))
# arr=[]
# for i in range (n):
#     arr.append(int(input()))
# print(arr)

# def rats(r,n, arr):
#     total=r*unit
#     add=0
#     for i in range (n):
#         total_arr=add+arr[i]
#         add=total_arr 
#     if arr==None:
#         return -1
           
#     elif add<total:
#         return 0
#     else:
#         add=0
#         for i in range (n):
#             add=add+arr[i]
#             if add>=total:
#                 break
#         return (i+1)
# aa=rats(r,n,arr)
# print(aa)


s=input()
i=0
def OBS(s):
    i=0
    while (i>len(s)):
        print(s)
        if s[i+1]=='A':
            if s[i]==1 and s[i+2]==1:
                s[i+2]='1'
            else:
                s[i+2]='0'               
            print(s[i+2])
            print(s)
            i+=2
        elif s[i+1]=='B':
            if s[i]==0 and s[i+2]==0:
                s[i+2]='0'                
            else:
                s[i+2]='0'               
            print(s[i+2])
            print(s)
            i+=2
        elif s[i+1]=='C':
            if (s[i]==1 and s[i+2]==1) or (s[i]==0 and s[i+2]==0):
                s[i+2]='0'               
            else: 
                s[i+2]='1'               
            print(s[i+2])
            print(s)
            i+=2
    return s[i+2]
        
print(OBS(list(s)))              

# r=5
# x=10
# y=8
# x1=20
# y1=16


# s ="erty sdffgg cvbn wertyuiop"
# for i in range (len(s)):
    
