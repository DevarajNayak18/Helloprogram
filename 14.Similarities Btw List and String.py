'''
List is mutable values can be changed or new values can be assigned to them.

#in list you access the date iteme and can change since its mutable
l=["a","b","c"]
print(l[0])
#in list you can assign new item.
l=["a","b","c"]
l[0]="hello"
print(l)

#list slicing
l=["a","b","c"]
print(l[-2])

#list slicing
l=["a","b","c","d"]
print(l[1:3])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#string is immutable,values can not be changed or new values can not be assigned to them.
#'str' object does not support item assignment
strg="Hello"
strg[0]="hi"
print(strg)


#Creating new strings from Slicing
strg1="Hello world is super"
strg2=strg1[:5]+' the '+ strg1[6:]
print(strg2)

#differences between mutable and immutable comes up with the reference

spam=[1,2,3,4,5]
cheese=spam
cheese[3]='Hello'
print(cheese)
print(spam)#since same list is reference to both variable you can expect assign chnage in it.



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#immutable values doesnt have this problem bcz they cannot be modified 'in place' they can only replaced by new values.

#passing list in fun calls

def list(cheese):
    cheese.append("hi")
spam=[1,2,3]
list(spam)
print(spam)


#copy
spam=[10,20,30,40]
cheese=spam.copy()
cheese[0]="hello"
print(cheese)
print(spam)



#Deepcopy
import copy
spam=[10,20,30,40]
cheese=copy.deepcopy(spam)
cheese[0]="hello"
print(cheese)
print(spam)

# Line continuation
sentence="hello world " \
    'how are you '\
    'feeling good'
print(sentence)



#Recap
---strings can do a lot of the same things lists can do, but strings are immutable.
--immutable values like strings and tuples cannoot be modified in place
-- mutable values like lists can be modified in place
--variable dont contain lists, they contain reference to lists.
--when passing a list arguments to a function, you are actually passing a list reference.
--changes made to list in the function will effect the list outside the function
--the \ line continuation character can be used to stretch python

'''
