'''#range object and list like  Values

for i in [0,1,2,3,4]:
    print(i)


#print range of 4
print(range(4))


#print list of range
print(list(range(0,100,2))) #

#For i in range(len (list))
books=["karva","parva","rose","The time"]
for i in range(len(books)):
    print("index " + str(i) + ' in the book is '+ books[i])


#Multiple Assignment in the List
list=["milk","egg","rose"]
cow=list[0]
chicken=list[1]
plant=list[2]
print(cow)
print(chicken)
print(plant)

#multiple variable and multiple items
name,age,company='dev','26','TS'
print(name)
print(age)
print(company)


#swapping variable
a='madhuri'
b='juli'
a,b=b,a
print(a)
print(b)

#augumented assignement operators
spam=10
spam+=1
print(spam)

#equivalent assignement operators
spam=40
spam=spam+2
print(spam)

#summary
--for loops technically iterate over the values in a list
--the range () functions a list like value, which can be passed to the list() fun
if you need an actual list value
--variable can swap their values using multiple assignment
--augumented assignment operators like +=are used as shortcut











'''