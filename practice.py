'''#swap two number
a=10
b=20
temp=a#10
a=b#20
b=temp
print(a)
print(b)


#Generate Random Number
import random
x=random.randint(0,10)
print("the random number is : ",format(x))


##Note : 1 kilometer = 0.621371 mile and  1 mile =1.60934 kilomere
# convert kilometer into miles
kilometers=float(input("enter the kilometers : "))
conv_fac=0.621371 #1 kilometer equal to 0.621371 miles
miles=float(kilometers)* float(conv_fac)
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


#Note : 1 kilometer = 0.621371 mile and  1 mile =1.60934 kilomere
#convert miles into kilometer
miles=float(input("enter the miles"))
conv_fac=0.621371 # 1miles   =0.621371 kilomter
kilometers= float(miles) / float(conv_fac)
print(kilometers)


def bubble_sort(array):
    for i in range(len(array)-1,0,-1):#ouline
        for j in range(i):#adjucent
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
array=[10,50,20,30]
bubble_sort(array)
print(array)


#print the given number is positive or negative using if

number=int(input("enter the number : "))
if number > 0:
    print("number is positive")
if number==0:
    print("zero")
if number<0:
    print("number is negative")



number=int(input("enter the number : "))
if number > 0:
    print("number is positive")
elif number==0:
    print("zero")
else:
    print("number is negative")


#using nested if
num=float(input("enter the number : "))
if num>=0:
    if num==0:
        print("zero")
    else:
        print("Positive")
else:
    print("Negative")

numbers=int(input("enter the number"))
if numbers%2==0:
    print("{0} is even ".format(numbers))
else:
    print("{0} is odd ".format(numbers))



import random
print("what is your name?")
name=input(" ")
secret_Number=random.randint(1,5)
print("well,"+ name+" i am thinking secerenumber is between 1 to 2",format(secret_Number))
for guess in range(1,3):
    print("Guess the number")
    guess=int(input(" "))
    if guess>secret_Number:
        print("Guess number is  high")
    elif guess<secret_Number:
        print("Guess number is too low")
    else:
        break
if guess==secret_Number:
    print("good job!, the number guess " +str(guess)+ " is correct")
else:
    print("Nope!, the number guess " +str(guess)


'operators= Boolean data types True or False \n
boolean operators and or '
camparison operator == != <=,>=,<,>

print(23==23)
print(23!=23)
print(23<=28)
print(23>=28)

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(2<1 and 5<1)



#Formate(value,specifiers)
print(format("Hello","#<20"))
print(format("Hello","<20"))
print(format("Hello",">20"))
a=20+10j
b=20+10j
print(a*b)


x=10
y=20
_=(x+y)
print(_+y)#results only in idle shell(_ having last output)



class studnets():
    def __init__(self,name,number,marks):
        self.name=name
        self.number=number
        self.marks=marks
    def display(self):
        print("Hi my name is ",self.name)
        print("Hi my number is ",self.number)
        print("Hi my marks is ",self.marks)
    def grade(self):
        if self.marks>=70:
            print("first class")
        elif self.marks>50:
            print(" second class")
        else:
            print("Fail")
n=int(input("enter the number of students: "))
for i in range(n):
    name=input("enter the name ")
    number=int(input("enter the number "))
    marks=int(input("enter the marks "))
    s=studnets(name, number, marks)
    s.display()
    s.grade()


class final_Result():
    def __init__(self,name,marks):

        self.name=name
        self.marks=marks
    def grade(self):
        result=((int(marks)/600)*100)
        if result>70:
            print("first class")
        elif result<=50:
            print("second class")
        else:
            print("fail")
print("Print my Result")
name=input("enter the name")
marks=input("enter the marks")
s=final_Result(name,marks)
s.grade()


x=int(input("enter the value of x : "))
y=int(input("enter the value of y : "))
sum=x+y
print("the sum of {0} and {1} is {2}".format(x,y,sum))

#format function
print("hello,my name is {fname} and my age is {age} working in {company}".format(fname="devaraj",age="26",company='Thundersoft'))

#implicit

x=20
print(x)
print(type(x))
y=10
z=x+y
print(z)
print(type(z))


#explicit
a=10
b=float(a)
print(b)
print(type(b))

s=3.5
q=complex(s)
print(q)
print(type(q))

m=2+5j
n=str(2+5j)
print(n)



#ceil will close to higher value
import math
x=10.6
y=-13.2
print("the ceil of 10.6 is : ",math.ceil(10.6))
print("the ceil of 13.2 is : ",math.ceil(-13.2))



#floor will close to lower value
import math
x=10.6
y=-13.2
print("the floor of 10.6 is : ",math.floor(10.6))
print("the floor of 13.2 is : ",math.floor(-13.2))
print(math.sqrt(16.5))
#abs(-7)
print(abs)


print(format("Hello"," >3"))

#Diamond pattern
row=int(input("enter the row number : "))
for i in range(row):
    print(" "*(row-i)+" $"*(i+1))
for j in range(row -1):
    print(" "*(j+2)+" $"*(row-1-j))



row=int(input("enter the number of rows : "))
for i in range(row):
    for j in range(4):
        print(" *",end=" ")


n=int(input("enter row : "))
for i in range(n):
    for j in range(n):
        print(" "*(n-1)+" *"*(j+1),end='')
    print()


import time
import subprocess
import operator

class adbLibrary:
    def __init__(self):
        print("my output is ")
    def adbshell(self,adbcommand):
        res=subprocess.run(["adb","shell",adbcommand],shell=True)
        print(res)
        return res
    def adbCmdExeVal(self,expResult,adbcommand):
        res=subprocess.check_output(adbcommand)
        actResult=str(res)
        print(actResult)
        time.sleep(2)

        if operator.contains(actResult,expResult):
            print("Pass")
        else:
            print("Fail")
    def keyevent(self,cmd):
        res=subprocess.run(["adb","shell","input","keyevent",cmd],shell=True)
        print(res)
        return res
    def swipeevent(self,cmd):
        res=subprocess.run(["adb","shell","input","swipe",cmd],shell=True)
        print(res)
        return res
    def logvalidationwithArg(self,adbcmd,expResult,file):
        with open (file,"w+") as f:
            output=subprocess.run(["adb","shell",adbcmd],stdout=f,shell=True,text=True)
            f.seek(0)
            content=f.read()
            print(content)
            f.close()
        if expResult in content:
            print("Pass- string is exist in the file")
        else:
            print("Fail-string doesnt exit in a file")


import sys
from Library import adbLibrary
sys.path.insert(0,"/adbLibrary")
adbcommand="cat  /cproc/cpuinfo"
expResult="Processor"
file="/log.txt"
device=adbLibrary.adbLibrary()
device.logValidationwithArg(expResult,adbcommand,file)


'''
spam={"dress":5,"bottle":3}
print("im bringing " + str(spam.get(" napkin",0))+ " to the picnic")#add assignment















































































