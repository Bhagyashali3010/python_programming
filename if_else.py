a=int(input("enter 1st no,:"))
b=int(input("enter 2nd no,:"))
if a>b :
    print(a, "is greter than" ,b)
else:
    print(b, "is greter than" ,a)



a=int(input("enter no,:"))
if a>0 :
    print(a, "is positive")
elif a<0:
        print(a, "is negative")
elif a==0:
        print(a, "is zero")


a=int(input("enter no,:"))
if (a%2==0):
    print(a, "is even no")
else :
     print(a, "is odd no")  
 

a=int(input("enter no,:"))
if (a%5==0):
     print(a, "is divisible no")
else :
     print(a, "is not divisible no")


days= int(input("enter a integer from 0 to 6:"))
if days==0:
    print ("monday")
elif days==1:
    print ("tuesday")
elif days==2:
    print ("wednesday")
elif days==3:
    print ("thursday")
elif days==4:
    print ("friday")
elif days==5:
    print ("saturday")
elif days==6:
    print("sunday")    


a= int(input("enter no. of month:"))
if (a%2==0):
    if a==2:
       print ("no. of days in month are 28")
    elif a==8:
       print ("no. of days in month are 31")    
    else:
        print("no. of days in the month are 30")
else :
    print ("no. of days in month are 31")          
            

a= int(input ("enter a year:"))
if (a%4==0) and (a%100!=0):
    print(a, "is a leap year")
elif (a%100==0) and (a%400==0):
    print(a, "is a leap year")

else:
    print(a, "is not a leap year")


