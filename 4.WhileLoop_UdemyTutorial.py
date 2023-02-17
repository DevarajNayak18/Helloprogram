'''#While loop

spam=0
while spam<5:
    print("Hello World")
    spam=spam+1


#comparing with if statement
spam=0
if spam<5:
    print("Hello World")
    spam=spam+1

#Type your name : until i type correct name it must ask the name
name=''
while name != 'your name':
    print("Please Type your name")
    name=input("")
print("Thank you so much")


#using True
name=''
while True:
    print("Please Type your name")
    name=input("")
    if name=='your name':
        break
print("Thank you so much")


#Continue
spam =0
while spam<10:
    print(spam)
    spam+=1
    if spam==4:
        continue

#Break statement
spam =0
while spam<10:
    print(spam)
    spam+=1
    if spam==4:
        break



#Recap
-when the execution reaches the end of a while statements block, it jumps back to the start to re check the condition

-a break statement causes the execution to immediately leave the loop, without re checking the condition
- a continue statement causes the execution to immediately jump back to the start of the loop and re check the condition

'''


