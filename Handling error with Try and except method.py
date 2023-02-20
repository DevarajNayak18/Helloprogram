'''#Try
def devidedby(devider):
    return 42/devider
print(devidedby(2))


#error exception
def devidedby(devider):
    return 42/devider
print(devidedby(2))
print(devidedby(0))

#output of above program is error
ZeroDivisionError: division by zero


def devidedby(devider):
    try:
        return 42/devider
    except ZeroDivisionError:
        print("error: you cant devide by zero")
print(devidedby(2))
print(devidedby(12))
print(devidedby(0))
print(devidedby(8))


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


print("enter the number of dogs")
numdogs=input()#you cant give input like six error=invalid literal for int() with base 10: 'six'
if int(numdogs)>=4:
    print("there is lot of dogs")
else:
    print("there is less number of dogs")


#try and except error method

print("enter the number of dogs")
numdogs=input()
try:
    if int(numdogs)>=4:
        print("there is lot of dogs")
    else:
        print("there is less number of dogs")
except ValueError:
    print("You didnt entered number,Please enter the number")

#summary
-- a divide by zero error happens when py devides a number by zero
--error causes the progrm crash
--an error that happens inside a try block will cause code in the except block to execute.that code can handle the error or display a message to the user
so that the program can keep going.




'''













