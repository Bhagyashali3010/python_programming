class A:
    def __init__(self):
        print("a init")
    def fea1(self):
        print("sdf")

class B():
    def __init__(self):
       
        print ("b init")
    def fea1(self):
        print("asd")

class C(A,B):
    def __init__(self):
        print("c init")        

bi=C()
bi.fea1()
bi.fea1()