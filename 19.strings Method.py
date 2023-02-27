'''#case sensitive--upper() and lower()
spam='Hello world!'
print(spam.upper())

spam='HeLLo IndiaNS!'
print(spam.lower())

print("Enter the answer")
answer=input()
#if answer=='yes':
 #   print('play the game')
print(answer=='yes') #True
print(answer=='YES')#False


#islower() and isupper()
print("enter the answer")
spam=input()
print(spam.islower())# if its input is 'yes', output is True else False
print(spam.isupper())# if its input is 'yes', output is True else False
print(spam.islower())# if its input is '', output is False
print('1234'.islower())# if its input is '1234', output is false since its not letter


#first letter is capital then condition is true
print("hello".upper().isupper())
print("hello".lower().islower())

#note below
isalpha()-letters only
isalnum()- letters and numbers only
isdecimal()- numbers only
isspace()-white space only
istitle()-titlecase only


print("Hello".isalpha())#True
print("Hello123".isalpha())#False
print("Hello".isalnum())#True
print("Hello123".isalnum())#True
print("Hello".isdecimal())#False
print("123".isdecimal())#True
print("  ".isspace())#True
print("".isspace())#False
print("Hello world!" [5].isspace())
print("This Is Rocky World".istitle())#True
print("Hello Devaraj".startswith("Hello"))#True
print("Hello Devaraj".startswith("ello"))#False
print("Hello Devaraj".endswith("Devaraj"))#True


#Join the words as list
print(','.join(["cat","rat","mat"]))

print(''.join(["cat","rat","mat"]))#without cama

print('\n'.join(["cat","rat","mat"])) #new line
print('\n\n'.join(["cat","rat","mat"]))#new line \n\n
print("My Name is Rakshith ".split())#Using split function
print("My Name is Rakshith ".split("a")#split before m


#right and left space
print("Hello".ljust(20))#left 20 space
print("Hello".rjust(10))#right 10 space
print("Hello".ljust(10,"*"))
print("Hello".rjust(10,"*"))
print("Hello".center(20,"*"))
print("Hello".center(20,"="))

#strip()
spam="    Hello    "
spam=spam.strip()#strip () fun used to clear space inbetween
print(spam)


spam="Hello There"
spam=spam.replace("e","XYS")#replace () fun used to clear space inbetween
print(spam)


import pyperclip
a=pyperclip.copy("hellio")
b=pyperclip.paste()
print(b)

#String Format
name='devaraj'
age='25'
staying="hyd"
charc=("my name is " +name+ " and my age is around " +age+ " working in "+staying)
print(charc)
'''
name='devaraj'
age='25'
staying="hyd"
charc="my name is %s, and my age is around%s, working in %s," %(name,age,staying)
print(charc)


#string concatenation
ch="Hello"+" Devaraj"
print(ch)

























