class Sum:
    def mySum(self, v1, v2):
        self.v1=v1
        self.v2=v2
        self.v3= v1+v2
        print(self.v3)
        if self.v3%2==0:
            print("even addition")
        else:
            print("odd addition")

    
aa=Sum()
bb=Sum()

(aa.mySum(3,4))
(bb.mySum(8,4))



class student:
    school='GSS'
    def __init__(self, name):
        self.name=name
        print("Hii!! ")

    def intro(self):
        print("welcome", self.name , "from", student.school )

s1=student('sham')
s1.intro()



class IPL:
    year=2024
    def __init__(self,team1, team2):
        self.team1=team1
        self.team2=team2
        print("in year",IPL.year)

    def match(self):
        print("the match is against",self.team1,"and", self.team2)

t1=IPL('chennai','mumbai')
t1.match()



class vehicle:
    def __init__(self, brand, model, year , speed):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=speed
        print(self.model,self.year,self.speed,self.brand)
       
    def accelerate(self):
        print("in first acc")

    def brake(self):
        print("in first brake")
    
    def honk(self):
        print("in first honk")

class v2(vehicle):
    def accelerate(self):
        print("in second acc")

    def honk(self):
        print("in second honk")

c1=vehicle('tata','nexu', 2022, 80)
c2=v2('tata','harrier', 2022, 80)

c1.honk()
c2.honk()


class Cars:
    wheels=5
    def __init__(self):
        print("this is the init")    

    @classmethod
    def round(cls):
        print("the no. of wheels ahe", cls.wheels)

    @staticmethod
    def info():
        print("everythings good")

class Company(Cars):
    pass

Company.round()        
c1=Company()
Company.info()


class A():
    def __init__(self):
        self.v1=2
        self.v2=3
        print(self .v1, self.v2)

    def why(self):
        self.v3=self.v1+self.v2
        print(self.v3) 

class B(A):
    def why(self):
        self.v3=self.v1*self.v2
        print(self.v3)

b1=A()
b1.why()



class cricket():
    def __init__(self, bat, ball, stump):
        self.bat=bat
        self.ball=ball
        self.stump=stump
        print(self.bat, self.ball, self.stump)

    def players(self, num, role1, role2):
        self.num=11
        self.role1=role1
        self.role2=role2
        print(self.num, self.role1, self.role2)

class countries(cricket):
    def info(self, name, wc):
        self.name= name
        self.wc= 2
        print(self.name, self.wc)

class india(countries):
    def play(self,best, finals):
        self.best= 3
        self.finals=7
        print(self.best, self.finals)

cc=india('wooden', 'tennis' , '3' )
cc.play('ms', 7)
cc.info('india',2)
cc.players('11','batsman','baller')


class A:
    pass
class C:
    pass
class B(C, A):
    pass
class D:
    pass
class E(D, B):
    pass
aa=E()
print(E.mro())


class A:
    def __init__(self):
        print("in the class a init")

    def __del__(self):
        print("desturcter is called")

obj1=A()
obj2=obj1
obj3=obj1
obj4=A()


class demo:
    def __init__(self):
        print("cons")
    def __del__(self):
        print("dest")

def fun():
    print("in fun0")
    obj=demo()
    print("end fun")
    return obj
retobj=fun()
print("end code")


