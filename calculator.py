class calci():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self,x,y):
        self.a=x+y
        return self.a

    def sub(self,x,y):
        self.a=x-y
        return self.a

    def mul(self,x,y):
        self.a=x*y
        return self.a

    def div(self,x,y):
        self.a=x/y
        return self.a


n=int(input("enter no. of numericals to be added:"))
for i in range(1,n):
    if i==1:
        x=int(input("enter no.:"))
        y=int(input("enter 2nd no.:"))
        z=input("enter opertion to be performed:")

        if z=='+':
            obj1=calci(x,y)
            a1=obj1.add(x,y)
        elif z=='-':
            obj2=calci(x,y)
            a1=obj2.sub(x,y)
        elif z=='*':
            obj3=calci(x,y)
            a1=obj3.mul(x,y)
        elif z=='/':
            obj4=calci(x,y)
            a1=obj4.div(x,y)
        print(x,z,y,"=",a1)
    else:
        x=a1
        y=int(input("enter next no.:"))
        z=input("enter opertion to be performed:")

        if z=='+':
            obj1=calci(x,y)
            a1=obj1.add(x,y)
        elif z=='-':
            obj2=calci(x,y)
            a1=obj2.sub(x,y)
        elif z=='*':
            obj3=calci(x,y)
            a1=obj3.mul(x,y)
        elif z=='/':
            obj4=calci(x,y)
            a1=obj4.div(x,y)
        print(x,z,y,"=",a1)
