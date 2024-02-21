# def outer():
#     def inner():
#         return "asd"
#     return inner()

# # ans= outer()
# print(outer())


import array as arr 
nos = arr.array( [2, 3, 4, 5])
print(nos)

def fact():
    for i in range(nos):
        facto=1
        for x in range (1, i+1):
            facto*=1
        return facto
    
for y in range(0, nos):
    main=fact(nos(y))
    y+=1
print(y)