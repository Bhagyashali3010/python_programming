# class Sum:
#     def mySum(self, v1, v2):
#         self.v1=v1
#         self.v2=v2
#         self.v3= v1+v2
#         print(self.v3)
#         if self.v3%2==0:
#             print("even addition")
#         else:
#             print("odd addition")

    
# aa=Sum()
# bb=Sum()

# (aa.mySum(3,4))
# (bb.mySum(8,4))



# class student:
#     school='GSS'
#     def __init__(self, name):
#         self.name=name
#         print("Hii!! ")

#     def intro(self):
#         print("welcome", self.name , "from", student.school )

# s1=student('sham')
# s1.intro()



# class IPL:
#     year=2024
#     def __init__(self,team1, team2):
#         self.team1=team1
#         self.team2=team2
#         print("in year",IPL.year)

#     def match(self):
#         print("the match is against",self.team1,"and", self.team2)

# t1=IPL('chennai','mumbai')
# t1.match()



# class vehicle:
#     def __init__(self, brand, model, year , speed):
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.speed=speed
#         print(self.model,self.year,self.speed,self.brand)
       
#     def accelerate(self):
#         print("in first acc")

#     def brake(self):
#         print("in first brake")
    
#     def honk(self):
#         print("in first honk")

# class v2(vehicle):
#     def accelerate(self):
#         print("in second acc")

#     def honk(self):
#         print("in second honk")

# c1=vehicle('tata','nexu', 2022, 80)
# c2=v2('tata','harrier', 2022, 80)

# c1.honk()
# c2.honk()


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