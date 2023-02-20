'''#List=is collection of data items and its mutable and assign data items within parenthasis,its more memory consumed and slower comapre
to tuple and it has many builtin methods
--a list a vlaue that contains multiple values
--the value in the list also called items
--you can access the items in the list with its integer index.
--the index starts at 0, not 1
---you can also use negative indexes. -1 refers to the last item , -2 is the second last item
--you can access multiple items using a slice
--the slice has two indexes, the new lists items start at the first index and go up to, but doesnt include, the second index
--the len() function ,concatanation and replication work the same way with lists that they do with strings
--you can convert any value into list by passing it to the list() functions

#print list
names=["dev",2,2.2,1+2j]
print(names)

#change index value 2
names=["dev",2,2.2,1+2j]
names[2]=10.5
print(names)

#print index 0 of 0
numb=[["cat","bat"],[1,2,3,4,5]]
print(numb[0])
print(numb[0][0])#print first index first index value
print(numb[1])
print(numb[1][2])#print 2nd indexs 3rd index value

#Negative index
list=["cat","rat","bat","chat"]
print(list[-1])
print(list[-2])

#list concatenantion
l=[["hello"]+["devaraj"]]
print(l)


#list concatenation
spam1="devaraj"
spam2="elephant"
l1=["Hello "+ spam1+"likes "+spam2+"in jungle"]
print(l1)


#List slices--->  index=single vlaue     slice=list of values
spam=["rat","mat","cat","bat"]
print(spam[1:3])
print(spam[:-1])


#add multiple items using slicing index
l=[1,2,3,4,5]
l[1:4]=["apple","banana","grapes","orrange"]
print(l)

#delete items  in the list

s=["dev","raj","nayak","king"]
del s[1]
print(s)

#Note: del statement = unassignment statement

#find length of string
print(len("hello"))

#find length of the list
l=[1,2,3,4,5,6]
print(len(l))

#string concatenation
g="Hello "+"world"
print(g)


#mutiply string with 3 times

print("dev "*3)
print([1,2,3,4 ]*3)



#convert string into tuple by using list method
print(list("hello"))


#find words in the list

print('dev' in ["dev","raj","nayak"]) # if string found in the list it will print True
print('ravi' in ["dev","raj","nayak"]) # if string not found in the list it will print False
print('kiran' not in ["dev","raj","nayak"]) # if string not in the list it will print True
'''


