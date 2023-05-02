'''name='devaraj'
if name=='devaraj':
    print('Hi',name)
print("Done")

#ELSE statement
password='dev123'
if password=='dev123':
    print("access granted")  #if password is correct
else:
    print("incorrect password") #if password is wrong

#elif
name='devking'
age=200
if name=='deva':
    print("name is deva")
elif age>300:
    print("my age is greater than 300")
elif age==100:
    print("my age is 100")
elif age<300:
    print("my age is less than 300 ")


#Enter name by input

print("Enter the name: ")
name=input()
if name:
    print("Thank you for the entering the name ")
else:
    print("you didnt printed a name ")

#if the input name is empty see the result

print("Enter the name: ")
name=input()
if name !=" ":
    print("Thank you for the entering the name ")
else:
    print("you didnt printed a name ")


'''
print(bool("shwjsgjwqd")) #output is True

print(bool("")) #output is False

print(bool(200)) #output is True

print(bool()) #output is False



'''

-An if statemnet can be used to conditionally execute code , depending on whether or not the if statements condition is True or False
-An elif statement can follow an if statement,its block executes if its condition is True and all of the previous condition have been false
-an else statement comes at the end. its block is executed if all the previous statement is false
-the values 0, 0.0 and the empty string are considered to be falsey values .
when used in conditions they are considered false.you can always see for yourself values are Truthly or falsely by passing them to the bool() function 
'''





